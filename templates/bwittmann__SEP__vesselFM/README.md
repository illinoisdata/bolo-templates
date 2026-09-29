---
pipeline_tag: image-segmentation
tags:
- medical
- biology
- clinical
license: other
# license_name: openrail++-m
---

# vesselFM
**TL;DR**: VesselFM is a foundation model for universal 3D blood vessel segmentation in arbitrary imaging domains.
For details, please refer to our [manuscript](https://openaccess.thecvf.com/content/CVPR2025/html/Wittmann_vesselFM_A_Foundation_Model_for_Universal_3D_Blood_Vessel_Segmentation_CVPR_2025_paper.html) and our [GitHub repo](https://github.com/bwittmann/vesselFM).

---
### Checkpoints
We provide the following checkpoints:

- `vesselFM_base.pt`: VesselFM variant pre-trained on our three proposed data sources (D_real, D_drand, and D_flow). This checkpoint will be automatically downloaded in `vesselfm/seg/inference.py`.


### Citing vesselFM
If you find our work useful, please cite:
```bibtex
@InProceedings{Wittmann_2025_CVPR,
    author    = {Wittmann, Bastian and Wattenberg, Yannick and Amiranashvili, Tamaz and Shit, Suprosanna and Menze, Bjoern},
    title     = {vesselFM: A Foundation Model for Universal 3D Blood Vessel Segmentation},
    booktitle = {Proceedings of the Computer Vision and Pattern Recognition Conference (CVPR)},
    month     = {June},
    year      = {2025},
    pages     = {20874-20884}
}
```