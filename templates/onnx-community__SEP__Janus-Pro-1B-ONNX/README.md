---
license: mit
base_model:
- deepseek-ai/Janus-Pro-1B
pipeline_tag: any-to-any
library_name: transformers.js
tags:
- text-to-image
- image-to-text
- image-text-to-text
---

https://huggingface.co/deepseek-ai/Janus-Pro-1B with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

**Example:** Image+text to text

```js
import { AutoProcessor, MultiModalityCausalLM } from "@huggingface/transformers";

// Load processor and model
const model_id = "onnx-community/Janus-Pro-1B-ONNX";
const processor = await AutoProcessor.from_pretrained(model_id);
const model = await MultiModalityCausalLM.from_pretrained(model_id);

// Prepare inputs
const conversation = [
  {
    role: "<|User|>",
    content: "<image_placeholder>\nConvert the formula into latex code.",
    images: ["https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/quadratic_formula.png"],
  },
];
const inputs = await processor(conversation);

// Generate response
const outputs = await model.generate({
  ...inputs,
  max_new_tokens: 150,
  do_sample: false,
});

// Decode output
const new_tokens = outputs.slice(null, [inputs.input_ids.dims.at(-1), null]);
const decoded = processor.batch_decode(new_tokens, { skip_special_tokens: true });
console.log(decoded[0]);
```

**Example:** Text to image

```js
import { AutoProcessor, MultiModalityCausalLM } from "@huggingface/transformers";

// Load processor and model
const model_id = "onnx-community/Janus-Pro-1B-ONNX";
const processor = await AutoProcessor.from_pretrained(model_id);
const model = await MultiModalityCausalLM.from_pretrained(model_id);

// Prepare inputs
const conversation = [
  {
    role: "<|User|>",
    content: "A stunning princess from kabul in red, white traditional clothing, blue eyes, brown hair",
  },
];
const inputs = await processor(conversation, { chat_template: "text_to_image" });

// Generate response
const num_image_tokens = processor.num_image_tokens;
const outputs = await model.generate_images({
  ...inputs,
  min_new_tokens: num_image_tokens,
  max_new_tokens: num_image_tokens,
  do_sample: true,
});

// Save the generated image
await outputs[0].save("test.png");
```