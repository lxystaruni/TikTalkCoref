
# Multimodal Coreference Resolution for Chinese Social Media Dialogues: Dataset and Benchmark Approach

[![arXiv](https://img.shields.io/badge/arXiv-2504.14321-b31b1b.svg)](https://arxiv.org/abs/2504.14321)

Implementation of the paper `Multimodal Coreference Resolution for Chinese Social Media Dialogues: Dataset and Benchmark Approach`. The paper has been accepted in ACL 2025.

<div align="center">
  <img width="700" alt="TiktalkCoref dataset" src="https://github.com/user-attachments/assets/d3be68a8-e04a-4f56-b384-a4bf32fdd5a9" />
</div>

## Abstract

Multimodal coreference resolution (MCR) aims to identify mentions referring to the same entity across different modalities, such as text and visuals, and is essential for understanding multimodal content. In the era of rapidly growing multimodal content and social media, MCR is particularly crucial for interpreting user interactions and bridging text-visual references to improve communication and personalization. However, MCR research for real-world dialogues remains unexplored due to the lack of sufficient data resources. To address this gap, we introduce TikTalkCoref, the first Chinese multimodal coreference dataset for social media in real-world scenarios, derived from the popular Douyin short-video platform. This dataset pairs short videos with corresponding textual dialogues from user comments and includes manually annotated coreference clusters for both person mentions in the text and the coreferential person head regions in the corresponding video frames. We also present an effective benchmark approach for MCR, focusing on the celebrity domain, and conduct extensive experiments on our dataset, providing reliable benchmark results for this newly constructed dataset. 

## Requirements

Pytorch == 1.10.1

transformers == 4.44.0

## Data Statistic

Statistic of TikTalkCoref is shown in the table below. Note that the statistical results in this table differ slightly from those reported in the paper due to our corrections of some annotation errors.

| Dataset            | Dialog | Duration(min) | Mention | Cluster | Bounding box |
|:------------------:|:------:|:-------------:|:-------:|:-------:|:------------:|
| TikTalkCoref       | 1012   | 519.65        | 2,179   | 1,435   | 955          |
| TikTalkCoref-celeb | 338    | 158.33        | 731     | 488     | 426          |

## Data Files

### 1. Annotation Files

- `data/all_textual_and_visual_annotations_format.jsonl`: Annotation file containing both textual and visual annotations.

  ```json
  {
    "doc_key": "6939175744706776354",
    "genre": "wb",
    "sentences": [["这", "个", "男", "生", "能", "接", "受", "她", "有", "儿", "子", "吗"], ["节", "目", "里", "可", "以", "仅", "限", "节", "目", "里"]], 
    "clusters": [[[0, 3]], [[7, 7]], [[9, 10]]], 
    "clusters_str": [["这个男生"], ["她"], ["儿子"]], 
    "speaker_ids": [["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]],
    "sentence_map": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    "subtoken_map": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]],
    "entity_labels": ["C1", "C2", "none"], 
    "visual_annotations": [
      {
        "cur_frame": 270, 
        "cur_frame_path": "/data/lxy/datasets/tiktalk_1012/frames/6939175744706776354/6939175744706776354_270_1.jpg",
        "bbox": [226, 357, 366, 547],
        "box_labels": "C1",
        "celebrity": "吴永恩", 
        "region_image_path": "/data/lxy/datasets/tiktalk_1012/faces_all/6939175744706776354_270_1_C1.jpg"
      },
      {
        "cur_frame": 364,
        "cur_frame_path": "/data/lxy/datasets/tiktalk_1012/frames/6939175744706776354/6939175744706776354_364_1.jpg",
        "bbox": [54, 361, 255, 588],
        "box_labels": "C2",
        "celebrity": "王子文",
        "region_image_path": "/data/lxy/datasets/tiktalk_1012/faces_all/6939175744706776354_364_1_C2.jpg"
      }
    ]
  }
  ```
  
  - `doc_key`:  Video ID (string).
  - `genre`: Text type.
  - `clusters`: Grouped mentions which refer to the same person and singletons.
  - `entity_labels`: Visual entity' label corresponding to each cluster (if no corresponding visual entity, it is set to "none").
  - `cur_frame`: Frame ID (only one frame annotated per person).
  - `celebrity`: Celebrity name (if not celebrity, it is set to "none").
- `data/split.jsonl`: Split file contains the videos' type `celebrity/non-celebrity` and their corresponding dataset split `train/dev/test`.
  
  ```json
  {"video_id": "7017744338322984225", "video_type": "celeb", "split": "test"}
  {"video_id": "7017732620826021132", "video_type": "no_celeb", "split": "test"}
  ```

### 2. Videos

You can see an example video of TikTalkCoref from [here](https://github.com/user-attachments/assets/e608b78b-d7c0-42f9-bd6f-f4edf4760ca6).
The videos of TikTalkCoref are from Douyin (TikTok China). Due to copyright restrictions, please contact us at staruni065007@gmail.com for original video downloads if needed.

## Data Processing​

### Step 1. Data Splitting

Execute the following command in your terminal:

```bash
python tools/data_split.py
```

Output file：

```
data/
├── all.textual.jsonl
├── all.visual.jsonl
├── all/                     # Global split files
│   ├── train.textual.jsonl
│   ├── train.visual.jsonl
│   ├── (...other splits)
├── celeb/                   # Celebrity data
│   ├── (...split files)
└── no_celeb/                # Non-celebrity data
    ├── (...split files)
```

## License

This dataset is based on [TikTalk](https://github.com/RUC-AIMind/TikTalk) (MIT License, Copyright (c) 2023 RUC-AIMind), with additional annotation collected by SudaNLP.  The original data remains under the MIT License.

## Citation

```bibtex
@inproceedings{Li-2025-TikTalkCoref,
  title     = {Multimodal Coreference Resolution for Chinese Social Media Dialogues: Dataset and Benchmark Approach},
  author    = {Xingyu Li, Chen Gong and Guohong Fu},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = aug,
  year      = {2025},
  publisher = {Association for Computational Linguistics},
  address   = {Vienna, Austria},  
  pages     = {xxx--xxx},           
  url       = {https://aclanthology.org/2025.acl-long.xxx}, 
  doi       = {10.18653/v1/2025.acl-long.xxx}                
}
```
