---
license: creativeml-openrail-m
datasets:
- yahma/alpaca-cleaned
language:
- en
base_model:
- HuggingFaceTB/SmolLM2-135M
tags:
- llama
- 135M
pipeline_tag: text-generation
---

## SmolLM2-135M-GGUF

| File Name                       | Size  | Quantization Level | Description                                                                                         |
|---------------------------------|-------|---------------------|-----------------------------------------------------------------------------------------------------|
| `SmolLM2-135M.F16.gguf`         | 271MB | FP16               | Full precision 16-bit floats, offering the best accuracy, suitable for high-performance setups.      |
| `SmolLM2-135M.Q4_K_M.gguf`      | 105MB | Q4                 | Quantized to 4-bit, prioritizes memory efficiency and faster inference, with a trade-off in accuracy. |
| `SmolLM2-135M.Q5_K_M.gguf`      | 112MB | Q5                 | Balanced quantization at 5-bit, offering a compromise between memory use and model accuracy.        |
| `SmolLM2-135M.Q8_0.gguf`        | 145MB | Q8                 | 8-bit quantization, designed for moderate performance with improved accuracy over lower-bit models.  |

# Run with Ollama 🦙

## Overview

Ollama is a powerful tool that allows you to run machine learning models effortlessly. This guide will help you download, install, and run your own GGUF models in just a few minutes.

## Table of Contents

- [Download and Install Ollama](#download-and-install-ollama)
- [Steps to Run GGUF Models](#steps-to-run-gguf-models)
  - [1. Create the Model File](#1-create-the-model-file)
  - [2. Add the Template Command](#2-add-the-template-command)
  - [3. Create and Patch the Model](#3-create-and-patch-the-model)
- [Running the Model](#running-the-model)
- [Sample Usage](#sample-usage)

## Download and Install Ollama🦙

To get started, download Ollama from [https://ollama.com/download](https://ollama.com/download) and install it on your Windows or Mac system.

## Steps to Run GGUF Models

### 1. Create the Model File
First, create a model file and name it appropriately. For example, you can name your model file `metallama`.

### 2. Add the Template Command
In your model file, include a `FROM` line that specifies the base model file you want to use. For instance:

```bash
FROM Llama-3.2-1B.F16.gguf
```

Ensure that the model file is in the same directory as your script.

### 3. Create and Patch the Model
Open your terminal and run the following command to create and patch your model:

```bash
ollama create metallama -f ./metallama
```

Once the process is successful, you will see a confirmation message.

To verify that the model was created successfully, you can list all models with:

```bash
ollama list
```

Make sure that `metallama` appears in the list of models.

---

## Running the Model

To run your newly created model, use the following command in your terminal:

```bash
ollama run metallama
```

### Sample Usage

In the command prompt, you can execute:

```bash
D:\>ollama run metallama
```

You can interact with the model like this:

```plaintext
>>> write a mini passage about space x
Space X, the private aerospace company founded by Elon Musk, is revolutionizing the field of space exploration.
With its ambitious goals to make humanity a multi-planetary species and establish a sustainable human presence in
the cosmos, Space X has become a leading player in the industry. The company's spacecraft, like the Falcon 9, have
demonstrated remarkable capabilities, allowing for the transport of crews and cargo into space with unprecedented
efficiency. As technology continues to advance, the possibility of establishing permanent colonies on Mars becomes
increasingly feasible, thanks in part to the success of reusable rockets that can launch multiple times without
sustaining significant damage. The journey towards becoming a multi-planetary species is underway, and Space X
plays a pivotal role in pushing the boundaries of human exploration and settlement.
```

---

## Conclusion

With these simple steps, you can easily download, install, and run your own models using Ollama. Whether you're exploring the capabilities of Llama or building your own custom models, Ollama makes it accessible and efficient.


- This README provides clear instructions and structured information to help users navigate the process of using Ollama effectively. Adjust any sections as needed based on your specific requirements or additional details you may want to include.