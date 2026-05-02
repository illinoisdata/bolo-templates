---
license: cc-by-nc-4.0
language:
- en
- cs
- de
- eu
- fa
- fr
- nl
- pt
- ru
- es
- zh
library_name: transformers
tags:
- discourse
---

---

# IsaNLP RST Parser v3

This repository hosts several versions of the IsaNLP RST Parser. For more details, visit the [GitHub repository](https://github.com/tchewik/isanlp_rst). 

Supported languages (all): English (eng), Czech (ces), German (deu), Basque (eus), Persian (fas), French (fra), Dutch (nld), Brazilian Portuguese (por), Russian (rus), Spanish (spa), and Chinese (zho).

## Performance

The following table summarizes the end-to-end performance metrics of different model versions across various corpora:


| Tag / Branch | Languages   | Train Data          | Test Data       | Seg  | S    | N    | R    | Full  |
|-------------- |------------ |---------------------|-----------------|------|------|------|------|-------|
| `rstdt`       | eng         | eng.rst.rstdt       | eng.rst.rstdt       | 97.8 | 75.6 | 65.0 | 55.6 | 53.9  |
| `gumrrg`      | eng, rus    | eng.erst.gum, rus.rst.rrg    | eng.erst.gum        | 95.5 | 67.4 | 56.2 | 49.6 | 48.7  |
|               |             |                     | rus.rst.rrg         | 97.0 | 67.1 | 54.6 | 46.5 | 45.4  |
| `rstreebank`  | rus         | rus.rrt             | rus.rst.rrt         | 92.1 | 66.2 | 53.1 | 46.1 | 46.2  |
| `unirst`      | all         | all                 | ces.rst.crdt     | 94.5 | 59.1 | 41.2 | 28.6 | 28.0 |
|               |             |                     | deu.rst.pcc      | 96.5 | 67.3 | 47.4 | 34.1 | 32.1 |
|               |             |                     | eng.erst.gum     | 95.3 | 67.3 | 55.6 | 48.5 | 47.4 |
|               |             |                     | eng.rst.oll      | 92.5 | 55.7 | 39.0 | 27.5 | 26.3 |
|               |             |                     | eng.rst.rstdt    | 98.1 | 76.7 | 65.5 | 55.2 | 53.6 |
|               |             |                     | eng.rst.sts      | 91.2 | 43.3 | 31.3 | 19.4 | 18.7 |
|               |             |                     | eng.rst.umuc     | 88.8 | 52.6 | 40.6 | 26.2 | 25.8 |
|               |             |                     | eus.rst.ert      | 92.5 | 66.0 | 50.3 | 34.9 | 34.7 |
|               |             |                     | fas.rst.prstc    | 94.7 | 63.0 | 50.2 | 40.8 | 40.7 |
|               |             |                     | fra.sdrt.annodis | 91.3 | 58.6 | 48.9 | 30.6 | 30.3 |
|               |             |                     | nld.rst.nldt     | 98.0 | 61.8 | 49.8 | 36.8 | 35.8 |
|               |             |                     | por.rst.cstn     | 93.9 | 68.4 | 52.8 | 44.9 | 44.5 |
|               |             |                     | rus.rst.rrg      | 96.4 | 67.4 | 54.0 | 46.3 | 45.1 |
|               |             |                     | rus.rst.rrt      | 90.7 | 63.0 | 49.0 | 42.3 | 42.2 |
|               |             |                     | spa.rst.rststb   | 93.4 | 63.5 | 50.3 | 36.0 | 36.0 |
|               |             |                     | spa.rst.sctb     | 85.5 | 55.1 | 46.8 | 39.1 | 39.1 |
|               |             |                     | zho.rst.gcdt     | 93.0 | 64.5 | 50.7 | 45.9 | 44.6 |
|               |             |                     | zho.rst.sctb     | 95.4 | 67.5 | 51.5 | 39.9 | 39.9 |

## Usage

To use the IsaNLP RST Parser with Hugging Face, follow the library [readme](https://github.com/tchewik/isanlp_rst/blob/master/README.md).

## Citation

If you use the IsaNLP RST Parser in your research, please cite our work as follows:

- **For versions `gumrrg`, `rstdt`, and `rstreebank`:** 
  ```bibtex
  @inproceedings{
   chistova-2024-bilingual,
   title = "Bilingual Rhetorical Structure Parsing with Large Parallel Annotations",
   author = "Chistova, Elena",
   booktitle = "Findings of the Association for Computational Linguistics ACL 2024",
   month = aug,
   year = "2024",
   address = "Bangkok, Thailand and virtual meeting",
   publisher = "Association for Computational Linguistics",
   url = "https://aclanthology.org/2024.findings-acl.577",
   pages = "9689--9706"
  }
  ```

- **For `unirst`:**
  ```bibtex
    @inproceedings{chistova-2025-bridging,
    title = "Bridging Discourse Treebanks with a Unified Rhetorical Structure Parser",
    author = "Chistova, Elena",
    booktitle = "Proceedings of the 6th Workshop on Computational Approaches to Discourse, Context and Document-Level Inferences (CODI 2025)",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.codi-1.17/",
    pages = "197--208"
   }
  ```