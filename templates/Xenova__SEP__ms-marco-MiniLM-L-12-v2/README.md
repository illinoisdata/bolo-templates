---
base_model: cross-encoder/ms-marco-MiniLM-L-12-v2
library_name: transformers.js
---

https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-12-v2 with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

**Example:** Information Retrieval w/ `Xenova/ms-marco-MiniLM-L-12-v2`.
```js
import { AutoTokenizer, AutoModelForSequenceClassification } from '@huggingface/transformers';

const model = await AutoModelForSequenceClassification.from_pretrained('Xenova/ms-marco-MiniLM-L-12-v2');
const tokenizer = await AutoTokenizer.from_pretrained('Xenova/ms-marco-MiniLM-L-12-v2');

const features = tokenizer(
    ['How many people live in Berlin?', 'How many people live in Berlin?'],
    {
        text_pair: [
            'Berlin has a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.',
            'New York City is famous for the Metropolitan Museum of Art.',
        ],
        padding: true,
        truncation: true,
    }
)

const scores = await model(features);
console.log(scores);
// quantized:   [ 9.597102165222168, -11.141762733459473 ]
// unquantized: [ 9.450557708740234, -11.160483360290527 ]
```

---

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).