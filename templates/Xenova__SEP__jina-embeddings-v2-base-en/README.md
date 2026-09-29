---
base_model: jinaai/jina-embeddings-v2-base-en
library_name: transformers.js
pipeline_tag: feature-extraction
---

https://huggingface.co/jinaai/jina-embeddings-v2-base-en with ONNX weights to be compatible with Transformers.js.

## Usage with 🤗 Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

```js
import { pipeline, cos_sim } from '@huggingface/transformers';

// Create feature extraction pipeline
const extractor = await pipeline('feature-extraction', 'Xenova/jina-embeddings-v2-base-en', {
    dtype: "fp32"  // Options: "fp32", "fp16", "q8", "q4"
});

// Generate embeddings
const output = await extractor(
    ['How is the weather today?', 'What is the current weather like today?'],
    { pooling: 'mean' }
);

// Compute cosine similarity
console.log(cos_sim(output[0].data, output[1].data));  // 0.9341313949712492 (unquantized) vs. 0.9022937687830741 (quantized)
```

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).