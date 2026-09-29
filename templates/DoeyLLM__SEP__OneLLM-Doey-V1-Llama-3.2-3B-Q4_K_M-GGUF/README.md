---
base_model: DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B
tags:
- llama-cpp
- gguf-my-repo
---

# DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B-Q4_K_M-GGUF
This model was converted to GGUF format from [`DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B`](https://huggingface.co/DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B) for more details on the model.


# **How to Use DoeyLLM / OneLLM-Doey-V1-Llama-3.2-3B-Instruct**

This guide explains how to use the **DoeyLLM** model on both app (iOS) and PC platforms.

---

## **App (iOS): Use with OneLLM**

OneLLM brings versatile large language models (LLMs) to your device—Llama, Gemma, Qwen, Mistral, and more. Enjoy private, offline GPT and AI tools tailored to your needs.

With OneLLM, experience the capabilities of leading-edge language models directly on your device, all without an internet connection. Get fast, reliable, and intelligent responses, while keeping your data secure with local processing.

### **Quick Start for iOS**

Follow these steps to integrate the **DoeyLLM** model using the OneLLM app:

1. **Download OneLLM**  
   Get the app from the [App Store](https://apps.apple.com/us/app/onellm-private-ai-gpt-llm/id6737907910) and install it on your iOS device.

2. **Load the DoeyLLM Model**  
   Use the OneLLM interface to load the DoeyLLM model directly into the app:
   - Navigate to the **Model Library**.
   - Search for `DoeyLLM`.
   - Select the model and tap **Download** to store it locally on your device.
3. **Start Conversing**  
   Once the model is loaded, you can begin interacting with it through the app's chat interface. For example:
   - Tap the **Chat** tab.
   - Type your question or prompt, such as:
     > "Explain the significance of AI in education."
   - Receive real-time, intelligent responses generated locally.

### **Key Features of OneLLM**
- **Versatile Models**: Supports various LLMs, including Llama, Gemma, and Qwen.
- **Private & Secure**: All processing occurs locally on your device, ensuring data privacy.
- **Offline Capability**: Use the app without requiring an internet connection.
- **Fast Performance**: Optimized for mobile devices, delivering low-latency responses.

For more details or support, visit the [OneLLM App Store page](https://apps.apple.com/us/app/onellm-private-ai-gpt-llm/id6737907910).

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B-Q4_K_M-GGUF --hf-file onellm-doey-v1-llama-3.2-3b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B-Q4_K_M-GGUF --hf-file onellm-doey-v1-llama-3.2-3b-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B-Q4_K_M-GGUF --hf-file onellm-doey-v1-llama-3.2-3b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo DoeyLLM/OneLLM-Doey-V1-Llama-3.2-3B-Q4_K_M-GGUF --hf-file onellm-doey-v1-llama-3.2-3b-q4_k_m.gguf -c 2048
```