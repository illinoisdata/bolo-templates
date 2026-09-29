---
base_model: LiheYoung/depth-anything-small-hf
library_name: transformers.js
pipeline_tag: depth-estimation
---

https://huggingface.co/LiheYoung/depth-anything-small-hf with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

**Example:** Depth estimation with `Xenova/depth-anything-small-hf`.

```js
import { pipeline } from '@huggingface/transformers';

// Create depth-estimation pipeline
const depth_estimator = await pipeline('depth-estimation', 'Xenova/depth-anything-small-hf');

// Predict depth map for the given image
const url = 'https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/bread_small.png';
const output = await depth_estimator(url);
// {
//   predicted_depth: Tensor {
//     dims: [350, 518],
//     type: 'float32',
//     data: Float32Array(181300) [...],
//     size: 181300
//   },
//   depth: RawImage {
//     data: Uint8Array(271360) [...],
//     width: 640,
//     height: 424,
//     channels: 1
//   }
// }
```

You can visualize the output with:

```js
output.depth.save('depth.png');
```

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b253b7ac5ecaae3d1efe0c/Zj77mcNlZS3TmlT5wKaAO.png)

---

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).