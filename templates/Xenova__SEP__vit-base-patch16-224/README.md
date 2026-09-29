---
base_model: google/vit-base-patch16-224
library_name: transformers.js
---

https://huggingface.co/google/vit-base-patch16-224 with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

**Example:** Perform image classification with `Xenova/vit-base-patch16-224`
```js
import { pipeline } from '@huggingface/transformers';

const classifier = await pipeline('image-classification', 'Xenova/vit-base-patch16-224');
const urls = [
    'https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/tiger.jpg',
    'https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/cats.jpg',
];
const output = await classifier(urls);
// [
//   { label: 'tiger, Panthera tigris', score: 0.6074584722518921 },
//   { label: 'Egyptian cat', score: 0.8246098756790161 }
// ]
```

---

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).