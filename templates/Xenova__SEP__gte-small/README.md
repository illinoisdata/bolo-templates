---
base_model: thenlper/gte-small
library_name: transformers.js
---

https://huggingface.co/thenlper/gte-small with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

You can then use the model to compute embeddings like this:

```js
import { pipeline } from '@huggingface/transformers';

// Create a feature-extraction pipeline
const extractor = await pipeline('feature-extraction', 'Xenova/gte-small');

// Compute sentence embeddings
const sentences = ['That is a happy person', 'That is a very happy person'];
const output = await extractor(sentences, { pooling: 'mean', normalize: true });
console.log(output);
// Tensor {
//   dims: [ 2, 384 ],
//   type: 'float32',
//   data: Float32Array(768) [ -0.053555335849523544, 0.00843878649175167, ... ],
//   size: 768
// }

// Compute cosine similarity
import { cos_sim } from '@huggingface/transformers';
console.log(cos_sim(output[0].data, output[1].data))
// 0.9798319649182318
```

You can convert this Tensor to a nested JavaScript array using `.tolist()`:
```js
console.log(output.tolist());
// [
//   [ -0.053555335849523544, 0.00843878649175167, 0.06234041228890419, ... ],
//   [ -0.049980051815509796, 0.03879701718688011, 0.07510733604431152, ... ]
// ]
```

By default, an 8-bit quantized version of the model is used, but you can choose to use the full-precision (fp32) version by specifying `{ dtype: 'fp32' }` in the `pipeline` function:
```js
const extractor = await pipeline('feature-extraction', 'Xenova/gte-small', { 
    dtype: 'fp32'  // Options: "fp32", "fp16", "q8", "q4"
});
```

---

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).