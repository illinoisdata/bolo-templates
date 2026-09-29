---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
---
# Prem-1B-SQL (HuggingFace)

- Read the blogpost [here](https://blog.premai.io/prem-1b-sql-fully-local-performant-slm-for-text-to-sql/)
- PremSQL Library | [GitHub](https://github.com/premAI-io/premsql)

Prem-1B-SQL is one of the very first series of fully local Text-to-SQL models developed by Prem AI. Being a 1B parameter model
it easily fits on low GPU devices (and CPU devices when quantized). We believe that AI assisted data analysis should be a Local first
approach. Because exposing Databases to third-party closed-source models can lead to data security breaches. We will be publishing some
of the public benchmark results of this model very soon. We will also be iterating on this model for more better results.

- **Developed by:** [Prem AI](https://www.premai.io/)
- **License:** [MIT]

## Results

We evaluated our model on two popular benchmark datasets: BirdBench and Spider. BirdBench consists of a public validation dataset (with 1534 data points) and a private test dataset. Spider comes up with only a public validation dataset. Here are the results:

| Dataset                  | Execution Accuracy |
| ------------------------ | ------------------ |
| BirdBench (validation)   | 46%                |
| BirdBench (private test) | 51.54%             |
| Spider                   | 85%                |

The BirdBench dataset is distributed across different difficulty levels. Here is a detailed view of the private results across different difficulty levels.

| Difficulty  | Count | EX    | Soft F1 |
| ----------- | ----- | ----- | ------- |
| Simple      | 949   | 60.70 | 61.48   |
| Moderate    | 555   | 47.39 | 49.06   |
| Challenging | 285   | 29.12 | 31.83   |
| Total       | 1789  | 51.54 | 52.90   |

Here is a more detailed comparison of popular closed- and open-source models.

| Model                             | # Params (in Billion) | BirdBench Test Scores |
| --------------------------------- | --------------------- | --------------------- |
| AskData + GPT-4o (current winner) | NA                    | 72.39                 |
| DeepSeek coder 236B               | 236                   | 56.68                 |
| GPT-4 (2023)                      | NA                    | 54.89                 |
| **PremSQL 1B (ours)**             | 1                     | 51.4                  |
| Qwen 2.5 7B Instruct              | 7                     | 51.1                  |
| Claude 2 Base (2023)              | NA                    | 49.02                 |

## How to use Prem-1B-SQL

Since it is a model built upon transformers, so it can be directly used with transformers. However running Text-to-SQL is not as simple
as running normal LLMs. The reason lies in model input prompt formations which is tightly coupled with databases. So we have developed PremSQL,
a fully open source library which is:

- **Local-First**: Avoid third-party closed-source providers and keep your data secure.
- **Customizable Datasets**: Create, fine-tune, and evaluate models with built-in or custom datasets.
- **Robust Executors and Evaluators**: Easily connect to databases and assess model performance.
- **Advanced Generators**: Convert natural language prompts into executable SQL queries.
- **Error Handling and Self-Correction**: Automatically correct SQL queries during inference.
- **Fine-Tuning Support**: Fine-tune models with LoRA, QLoRA, or full fine-tuning strategies.
- **End-to-End Pipelines**: Seamlessly integrate all components for autonomous data analysis.

To install PremSQL just create a new environment and type:

```bash
pip install -U premsql
```

Please [check out our documentation](https://docs.premai.io/premsql/introduction) to know about more details of the library usage.

### Running Prem-1B-SQL using PremSQL BaseLine Agent

The easiest way to use this model is through PremSQL pipelines. All you need to do is provide the database path (in case of SQLite databases)
or provide the DB connection URI. After this, all you need to do is, connect it with the model. Here is how you do that:

```python
from premsql.agents import BaseLineAgent
from premsql.generators import Text2SQLGeneratorOllama
from premsql.agents.tools import SimpleMatplotlibTool
from premsql.executors import SQLiteExecutor

text2_sqlmodel = Text2SQLGeneratorHF(
    model_or_name_or_path="prem-research/prem-1B-SQL",
    experiment_name="test_generators",
    device="cuda:0",
    type="test"
)

analyser_and_plotter = Text2SQLGeneratorHF(
    model_or_name_or_path="meta-llama/Llama-3.2-1B-Instruct",
    experiment_name="test_generators",
    device="cuda:0",
    type="test"
)

agent = BaseLineAgent(
    session_name="testing_hf",
    db_connection_uri="sqlite:////path/to/your/database.sqlite",
    specialized_model1=model,
    specialized_model2=model,
    plot_tool=SimpleMatplotlibTool(),
    executor=SQLiteExecutor()
)

response = agent(
    "/query what all tables are present inside the database"
)
response.show_dataframe()
```

Under the hood, it automatically connects with your Database and do all the heavy lifting like prompt creation, execution etc for you.

### Running Prem-1B-SQL using PremSQL Generators

You can also run the model using PremSQL Generators. This is helpful when you want to do generations in
bulk on some dataset. Here is an example:

```python
from premsql.generators import Text2SQLGeneratorHF
from premsql.datasets import Text2SQLDataset

# Define a dataset
dataset = bird_dataset = Text2SQLDataset(
    dataset_name='bird', split="validation", force_download=False,
    dataset_folder="/path/to/dataset"
).setup_dataset(num_rows=10, num_fewshot=3)

# Define a generator
generator = Text2SQLGeneratorHF(
    model_or_name_or_path="prem-research/prem-1B-SQL",
    experiment_name="test_generators",
    device="cuda:0",
    type="test"
)

# Generate on the full dataset
responses = generator.generate_and_save_results(
    dataset=bird_dataset,
    temperature=0.1,
    max_new_tokens=256
)

print(responses)
```

### Using Execution guided Decoding

This strategy executes the generated SQL against the DB and, if it fails, uses the error message for correction, repeating until it gets a valid result or the retries run out.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/637b0075806b18943e4ba357/_5rdIQZwyaUFb84xKW_AV.png)

```python
from premsql.executors import SQLiteExecutor

executor = SQLiteExecutor()
response = generator.generate_and_save_results(
    dataset=bird_dataset,
    temperature=0.1,
    max_new_tokens=256,
    force=True,
    executor=executor,
    max_retries=5 # this is optional (default is already set to 5)
)
```

You can also fine-tune Prem-1B-SQL using HuggingFace Transformers and with [PremSQL Tuners](https://docs.premai.io/premsql/tuners) as well.
Please [check out our documentation](https://docs.premai.io/premsql/introduction) to know about more about PremSQL and all the features
we provide.

## Datasets used to train the model

Prem-1B-SQL is trained using the following datasets:

1. [BirdBench Training dataset](https://bird-bench.github.io/) | Uploaded on [PremSQL datasets on HF](https://huggingface.co/datasets/prem-research/birdbench)
2. [Spider dataset](https://yale-lily.github.io/spider) | Uploaded on [PremSQL datasets on HF](https://huggingface.co/datasets/prem-research/spider)
3. [Domain specialization dataset, gathered and uploaded to PremSQL datasets](https://huggingface.co/datasets/prem-research/domains)
4. [Gretel AI synthetic dataset](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql?row=0)

Additionally we made error handling datasets on top of these datasets to make the model learn from its errors and self correct them.

## Evaluation results of Prem-1B-SQL

The results of Prem-1B-SQL on some public benchmarks will be published soon.