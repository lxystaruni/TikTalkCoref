# TikTalkCoref

## Introduction
This repository is the project page for [TikTalkCoref](https://arxiv.org/abs/2504.14321). TikTalkCoref is the first Chinese multimodal coreference resolution dataset for real-world dialogues on social media. Our paper has been accepted by ACL 2025.

<img width="755" alt="TiktalkCoref dataset" src="https://github.com/user-attachments/assets/d3be68a8-e04a-4f56-b384-a4bf32fdd5a9" />

## Data Preparation
Please follow these steps to preprocess your data.
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
