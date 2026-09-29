---
license: apache-2.0
library_name: perception-encoder
pipeline_tag: image-feature-extraction
---
# Model Details

[\[📃 Tech Report\]](https://arxiv.org/abs/2504.13181)
[\[📂 Github\]](https://github.com/facebookresearch/perception_models/)

Perception Encoder (PE) is a state-of-the-art encoder for image and video understanding trained via simple vision-language learning. It was introduced in "[Perception Encoder: The best visual embeddings
are not at the output of the network](https://ai.meta.com/research/publications/perception-encoder-the-best-visual-embeddings-are-not-at-the-output-of-the-network/)".

**Model Developer**: Meta

**Model Overview**: Perception Encoder (PE) is a family of large-scale vision encoder models with state-of-the-art performance on a large variety of vision tasks. By using a robust contrastive pretraining recipe and finetuning on synthetically aligned videos, PE not only outperforms all existing models on classification and retrieval, but it also internally produces strong, general features that scale for downstream tasks. PE unlocks the ability for large-scale contrastive pretraining to transfer to downstream tasks with alignment tuning to capitalize on those general features.

<img src="https://huggingface.co/facebook/PE-Core-G14-448/resolve/main/docs/pe_image1.png" style="width: 100%; margin: 0 auto; display: block;" />


## Perception Encoder: Language
PE lang takes the strong language performance from the intermediate layers of PE core and further aligns for language modeling following [PLM](https://huggingface.co/papers/2504.13180). We specifically tuned PE lang to be versatile for any multimodal langugage modeling use case, including using different language model decoders (e.g., Llama / Qwen) and using different eval settings (e.g., native res / tiling). PE lang performs particularly well on OCR and document tasks.

We release two PE Lang checkpoints, L14-448 and G14-448. Here are their results our benchmark setting with frozen encoder with 2.6M SFT datamix, using 448px _only_ (i.e., _with no tiling_) and Llama 3.1 8B as the decoder:

| Encoder | Checkpoint | Doc VQA (val) | InfoQA (val) | TextVQA | MVBench | PerceptionTest (val) | EgoSchema (val) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **L/14** 448px | [PE-Lang-L14-448](https://huggingface.co/facebook/PE-Lang-L14-448) | 81.9 | 46.4 | 73.0 | 52.3 | 54.7 | 59.8 |
| **G/14** 448px | [PE-Lang-G14-448](https://huggingface.co/facebook/PE-Lang-G14-448) | 84.4 | 48.3 | 75.2 | 52.4 | 56.0 | 62.0 |



Here is a sample of the performance obtainable by using PE Core G aligned further with [PLM-8B](https://huggingface.co/facebook/Perception-LM-8B) (*stage 3*) using 36+1 image tiles / 32 video frames with Llama 3.1 8B as the decoder:

| Model | Encoder | Doc VQA (test) | InfoQA (test) | TextVQA | MVBench | PerceptionTest (test) | EgoSchema (test) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| PLM-8B | [PE-Core-G14-448](https://huggingface.co/facebook/PE-Core-G14-448)* | 94.6 | 78.8 | 86.5 | 77.1 | 82.7 | 68.8 | 

\* The PE-Core-G14-448 checkpoint was further trained using tiling. We will release the tiling aligned checkpoint soon.

See the paper for full performance evaluations and fair comparisons to other models. 

# How to use

## Model loading code
We provide the model loading code in https://github.com/facebookresearch/perception_models
You can find more details in the GitHub repo.


# Citation
If you find our code useful for your research, please consider citing:
    
```
@article{bolya2025PerceptionEncoder,
  title={Perception Encoder: The best visual embeddings are not at the output of the network},
  author={Daniel Bolya and Po-Yao Huang and Peize Sun and Jang Hyun Cho and Andrea Madotto and Chen Wei and Tengyu Ma and Jiale Zhi and Jathushan Rajasegaran and Hanoona Rasheed and Junke Wang and Marco Monteiro and Hu Xu and Shiyu Dong and Nikhila Ravi and Daniel Li and Piotr Doll{\'a}r and Christoph Feichtenhofer},
  journal={arXiv},
  year={2025}
}

@article{cho2025PerceptionLM,
  title={PerceptionLM: Open-Access Data and Models for Detailed Visual Understanding},
  author={Jang Hyun Cho and Andrea Madotto and Effrosyni Mavroudi and Triantafyllos Afouras and Tushar Nagarajan and Muhammad Maaz and Yale Song and Tengyu Ma and Shuming Hu and Hanoona Rasheed and Peize Sun and Po-Yao Huang and Daniel Bolya and Suyog Jain and Miguel Martin and Huiyu Wang and Nikhila Ravi and Shashank Jain and Temmy Stark and Shane Moon and Babak Damavandi and Vivian Lee and Andrew Westbury and Salman Khan and Philipp Kr\"{a}henb\"{u}hl and Piotr Doll{\'a}r and Lorenzo Torresani and Kristen Grauman and Christoph Feichtenhofer},
  journal={arXiv},
  year={2025}
}
```