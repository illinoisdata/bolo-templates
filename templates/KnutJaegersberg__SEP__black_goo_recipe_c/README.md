---
license: cc-by-nc-4.0
---
Prompt Example:
```
### System:

You are an AI assistant. User will give you a task. Your goal is to complete the task as faithfully as you can. While performing the task think step-by-step and justify your steps.


### Instruction: 

How do you fine tune a large language model? 

### Response: 

To fine-tune a large language model, we use various techniques to improve its performance and adjust its parameters based on user feedback. These techniques include: 

1. Fine tuning the original model with additional data. For example, adding more training examples or using specialized datasets such as question answering or natural language inference tasks. This helps the model learn new concepts and skills by interacting with additional information sources.
2. Using transfer learning methods to incorporate knowledge from other models that have been pre-trained for specific domains. For instance, using pre-trained embeddings from neural networks trained on text classification tasks like sentiment analysis or question answering to help fine-tuning the main language model.
3. Improving the quality of the training data. We may optimize the training process by increasing the accuracy of provided data sets (e.g., by improving word embedding quality), refining the selection of relevant examples, and/or providing additional supervision signals during training.
4. Incorporating knowledge from external resources such as domain-specific lexicons or domain-specific knowledge bases. For example, incorporating domain-specific rules and facts into the model to help it understand domain-specific terminology and semantics.
5. Employing techniques like dropout regularization and dropout sampling to avoid overfitting and reduce overconfidence in the model's predictions.
6. Utilizing meta-learning methods such as reinforcement learning or self-supervised learning to enable the model to adapt quickly to changing situations without being explicitly programmed.
7. Incorporating human input through crowdsourcing or user testing to validate the model's performance and ensure user satisfaction.
8. Implementing various optimization strategies to improve efficiency and reduce computational costs while maintaining high performance levels.

In conclusion, fine tuning a large language model requires combining various techniques including fine tuning, transfer learning, improved data quality, external resources, meta-learning, optimization strategies, crowd sourcing, and user testing. These approaches aim to improve the model's ability to handle various tasks and provide users with better experiences in their daily interactions with language systems.
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_KnutJaegersberg__black_goo_recipe_c)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 34.19   |
| ARC (25-shot)         | 38.74          |
| HellaSwag (10-shot)   | 66.83    |
| MMLU (5-shot)         | 26.57         |
| TruthfulQA (0-shot)   | 36.54   |
| Winogrande (5-shot)   | 64.72   |
| GSM8K (5-shot)        | 0.68        |
| DROP (3-shot)         | 5.23         |
