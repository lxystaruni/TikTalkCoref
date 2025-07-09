# TikTalkCoref
[![arXiv](https://img.shields.io/badge/arXiv-2504.14321-b31b1b.svg)](https://arxiv.org/abs/2504.14321)
## Introduction
TikTalkCoref is the first Chinese multimodal coreference resolution dataset for real-world social media dialogues. The dataset comprises 1,012 dialogues with 519.65 minutes of video duration, containing 1,435 coreference clusters, 2,179 mentions, and 958 visual bounding boxes. Our work has been accepted for publication at ACL 2025.

<div align="center">
  <img width="755" alt="TiktalkCoref dataset" src="https://github.com/user-attachments/assets/d3be68a8-e04a-4f56-b384-a4bf32fdd5a9" />
</div>

## Data Preparation
### Annotation Files
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
  - `cur_frame`: Frames containing mentioned persons in the dialogue (only one frame annotated per person).
  - `celebrity`: Celebrity name (if not celebrity, it is set to "none").
- `data/split.jsonl`: Split file contains the videos' type `celebrity/non-celebrity` and their corresponding dataset split `train/dev/test`.
  
  ```json
  {"video_id": "7017744338322984225", "video_type": "celeb", "split": "test"}
  {"video_id": "7017732620826021132", "video_type": "no_celeb", "split": "test"}
  ```
### Step 1: Data Splitting
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
The videos are from Douyin (TikTok China). Due to copyright restrictions, please contact us at staruni065007@gmail.com for original video downloads if needed. 

## Data Comparison
The comparison of TikTalkCoref with other multimodal coreference resolution datasets is shown in the table below.
<img width="1380" alt="image" src="https://github.com/user-attachments/assets/859d3939-a7b4-4396-ac72-9851051f31c7" />



## License

This dataset is based on [TikTalk](https://github.com/RUC-AIMind/TikTalk) (MIT License, Copyright (c) 2023 RUC-AIMind), with additional annotation collected by SudaNLP.  The original data remains under the MIT License.
