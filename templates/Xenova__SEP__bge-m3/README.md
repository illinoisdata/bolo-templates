---
base_model: BAAI/bge-m3
library_name: transformers.js
license: mit
---

https://huggingface.co/BAAI/bge-m3 with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

You can then use the model to compute embeddings, as follows:

```js
import { pipeline } from '@huggingface/transformers';

// Create a feature-extraction pipeline
const extractor = await pipeline('feature-extraction', 'Xenova/bge-m3');

// Compute sentence embeddings
const texts = ["What is BGE M3?", "Defination of BM25"]
const embeddings = await extractor(texts, { pooling: 'cls', normalize: true });
console.log(embeddings);
// Tensor {
//   dims: [ 2, 1024 ],
//   type: 'float32',
//   data: Float32Array(2048) [ -0.0340719036757946, -0.04478546231985092, ... ],
//   size: 2048
// }

console.log(embeddings.tolist()); // Convert embeddings to a JavaScript list
// [
//   [ -0.0340719036757946, -0.04478546231985092, -0.004497686866670847, ... ],
//   [ -0.015383965335786343, -0.041989751160144806, -0.025820579379796982, ... ]
// ]
```

You can also use the model for retrieval. For example:
```js
import { pipeline, cos_sim } from '@huggingface/transformers';

// Create a feature-extraction pipeline
const extractor = await pipeline('feature-extraction', 'Xenova/bge-m3');

// Define query to use for retrieval
const query = 'What is BGE M3?';

// List of documents you want to embed
const texts = [
  'BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.',
  'BM25 is a bag-of-words retrieval function that ranks a set of documents based on the query terms appearing in each document',
];

// Compute sentence embeddings
const embeddings = await extractor(texts, { pooling: 'cls', normalize: true });

// Compute query embeddings
const query_embeddings = await extractor(query, { pooling: 'cls', normalize: true });

// Sort by cosine similarity score
const scores = embeddings.tolist().map(
  (embedding, i) => ({
    id: i,
    score: cos_sim(query_embeddings.data, embedding),
    text: texts[i],
  })
).sort((a, b) => b.score - a.score);
console.log(scores);
// [
//   { id: 0, score: 0.62532672968664, text: 'BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.' },
//   { id: 1, score: 0.33111060648806, text: 'BM25 is a bag-of-words retrieval function that ranks a set of documents based on the query terms appearing in each document' },
// ]
```

---

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).