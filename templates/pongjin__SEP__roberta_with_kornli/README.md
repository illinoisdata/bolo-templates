---
license: apache-2.0
datasets:
- kor_nli
language:
- ko
metrics:
- accuracy
pipeline_tag: zero-shot-classification
---

**This model has been referred to the following link : https://github.com/Huffon/klue-transformers-tutorial.git**

해당 모델은 위 깃허브를 참고하여 klue/roberta-base 모델을 kor_nli 의 mnli, xnli로 파인튜닝한 모델입니다.   
| train_loss | val_loss | acc | epoch | batch | lr |
| --- | --- | --- | --- | --- | --- |
| 0.326 | 0.538 | 0.811 | 3 | 32 | 2e-5 |


RoBERTa와 같이 token_type_ids를 사용하지 않는 모델의 경우, zero-shot pipeline을 바로 적용할 수 없습니다(transformers==4.7.0 기준)  
따라서 다음과 같이 변환하는 코드를 넣어줘야 합니다. 해당 코드 또한 위 깃허브의 코드를 수정하였습니다.  

```python
class ArgumentHandler(ABC):
    """
    Base interface for handling arguments for each :class:`~transformers.pipelines.Pipeline`.
    """

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class CustomZeroShotClassificationArgumentHandler(ArgumentHandler):
    """
    Handles arguments for zero-shot for text classification by turning each possible label into an NLI
    premise/hypothesis pair.
    """

    def _parse_labels(self, labels):
        if isinstance(labels, str):
            labels = [label.strip() for label in labels.split(",")]
        return labels

    def __call__(self, sequences, labels, hypothesis_template):
        if len(labels) == 0 or len(sequences) == 0:
            raise ValueError("You must include at least one label and at least one sequence.")
        if hypothesis_template.format(labels[0]) == hypothesis_template:
            raise ValueError(
                (
                    'The provided hypothesis_template "{}" was not able to be formatted with the target labels. '
                    "Make sure the passed template includes formatting syntax such as {{}} where the label should go."
                ).format(hypothesis_template)
            )

        if isinstance(sequences, str):
            sequences = [sequences]
        labels = self._parse_labels(labels)

        sequence_pairs = []
        for label in labels:
            # 수정부: 두 문장을 페어로 입력했을 때, `token_type_ids`가 자동으로 붙는 문제를 방지하기 위해 미리 두 문장을 `sep_token` 기준으로 이어주도록 함
            sequence_pairs.append(f"{sequences} {tokenizer.sep_token} {hypothesis_template.format(label)}")

        return sequence_pairs, sequences
```

이후 classifier를 정의할 때 이를 적용해야 됩니다.  
```python
classifier = pipeline(
    "zero-shot-classification",
    args_parser=CustomZeroShotClassificationArgumentHandler(),
    model="pongjin/roberta_with_kornli"
)
```
#### results
```python
sequence = "배당락 D-1 코스피, 2330선 상승세...외인·기관 사자"	
candidate_labels =["외환",'환율', "경제", "금융", "부동산","주식"]

classifier(
    sequence,
    candidate_labels,
    hypothesis_template='이는 {}에 관한 것이다.',
)

>>{'sequence': '배당락 D-1 코스피, 2330선 상승세...외인·기관 사자',
 'labels': ['주식', '금융', '경제', '외환', '환율', '부동산'],
 'scores': [0.5052872896194458,
  0.17972524464130402,
  0.13852974772453308,
  0.09460823982954025,
  0.042949128895998,
  0.038900360465049744]}
```