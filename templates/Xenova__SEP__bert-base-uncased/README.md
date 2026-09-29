---
base_model: bert-base-uncased
library_name: transformers.js
---

https://huggingface.co/bert-base-uncased with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

**Example:** Perform masked language modelling (a.k.a. "fill-mask").

```js
import { pipeline } from '@huggingface/transformers';

const unmasker = await pipeline('fill-mask', 'Xenova/bert-base-uncased');
const output = await unmasker('The goal of life is [MASK].');
```

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).