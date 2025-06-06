import jsonlines
import os
from collections import defaultdict

# 按模态切分
def split_different_modality_annotations(anno_file_path,video_title_path,output_dir):
    fr=jsonlines.open(anno_file_path,'r')
    textual_anno_list=[]
    visual_anno_list=[]
    frt=jsonlines.open(video_title_path,'r')
    title_map = {item['video_id']: item['title'] for item in frt}
    for obj in fr:
        doc_key = obj['doc_key']
        textual_anno={
            'doc_key':doc_key,
            'genre':obj['genre'],
            'sentences':obj['sentences'],
            'clusters':obj['clusters'],
            'clusters_str':obj['clusters_str'],
            'speaker_ids':obj['speaker_ids'],
            'sentence_map':obj['sentence_map'],
            'subtoken_map':obj['subtoken_map'],
            'entity_labels':obj['entity_labels'],
        }
        textual_anno_list.append(textual_anno)
        video_title = title_map.get(doc_key, "Unknown Title")
        visual_anno={
            'doc_key':doc_key,
            'video_title':video_title,
            'video_path':'/data/lxy/datasets/tiktalk_1012/raw_videos/'+doc_key+'.mp4',
            'visual_annotations':obj['visual_annotations']
        }
        # print(visual_anno)
        visual_anno_list.append(visual_anno)

    with jsonlines.open(f"{output_dir}/all.textual.jsonl", 'w') as fw_text, \
         jsonlines.open(f"{output_dir}/all.visual.jsonl", 'w') as fw_visual:
        fw_text.write_all(textual_anno_list)
        fw_visual.write_all(visual_anno_list)

# 按视频类型和所属split切分          
def split_data_by_type_and_split(output_dir, split_file_path):
    all_text_file = f'{output_dir}/all.textual.jsonl'
    all_visual_file = f'{output_dir}/all.visual.jsonl'
    
    all_dir = f'{output_dir}/all'
    celeb_dir = f'{output_dir}/celeb'
    no_celeb_dir = f'{output_dir}/no_celeb'
    
    for dir_path in [all_dir, celeb_dir, no_celeb_dir]:
        os.makedirs(dir_path, exist_ok=True)
    
    with jsonlines.open(split_file_path, 'r') as fs:
        split_data = list(fs)
        video_type_map = {item['video_id']: item['video_type'] for item in split_data}
        split_type_map = {item['video_id']: item['split'] for item in split_data}
    
    global_writers = {
        'train': {
            'textual': jsonlines.open(f'{all_dir}/train.textual.jsonl', 'w'),
            'visual': jsonlines.open(f'{all_dir}/train.visual.jsonl', 'w')
        },
        'val': {
            'textual': jsonlines.open(f'{all_dir}/val.textual.jsonl', 'w'),
            'visual': jsonlines.open(f'{all_dir}/val.visual.jsonl', 'w')
        },
        'test': {
            'textual': jsonlines.open(f'{all_dir}/test.textual.jsonl', 'w'),
            'visual': jsonlines.open(f'{all_dir}/test.visual.jsonl', 'w')
        }
    }
    

    type_writers = {
        'celeb': {
            'train': {
                'textual': jsonlines.open(f'{celeb_dir}/train.textual.jsonl', 'w'),
                'visual': jsonlines.open(f'{celeb_dir}/train.visual.jsonl', 'w')
            },
            'val': {
                'textual': jsonlines.open(f'{celeb_dir}/val.textual.jsonl', 'w'),
                'visual': jsonlines.open(f'{celeb_dir}/val.visual.jsonl', 'w')
            },
            'test': {
                'textual': jsonlines.open(f'{celeb_dir}/test.textual.jsonl', 'w'),
                'visual': jsonlines.open(f'{celeb_dir}/test.visual.jsonl', 'w')
            }
        },
        'no_celeb': {
            'train': {
                'textual': jsonlines.open(f'{no_celeb_dir}/train.textual.jsonl', 'w'),
                'visual': jsonlines.open(f'{no_celeb_dir}/train.visual.jsonl', 'w')
            },
            'val': {
                'textual': jsonlines.open(f'{no_celeb_dir}/val.textual.jsonl', 'w'),
                'visual': jsonlines.open(f'{no_celeb_dir}/val.visual.jsonl', 'w')
            },
            'test': {
                'textual': jsonlines.open(f'{no_celeb_dir}/test.textual.jsonl', 'w'),
                'visual': jsonlines.open(f'{no_celeb_dir}/test.visual.jsonl', 'w')
            }
        }
    }
    
    for file in [all_text_file, all_visual_file]:
        with jsonlines.open(file, 'r') as fa:
            for data in fa:
                video_id = data['doc_key'] if 'doc_key' in data else data['video_id']
                video_type = video_type_map.get(video_id, "Unknown")
                split_type = split_type_map.get(video_id, "Unknown")
                
                if video_type not in ['celeb', 'no_celeb'] or split_type not in ['train', 'val', 'test']:
                    continue
                
                data_key = 'textual' if 'textual' in file else 'visual'

                global_writers[split_type][data_key].write(data)
                
                type_writers[video_type][split_type][data_key].write(data)
    
    for split in global_writers.values():
        for writer in split.values():
            writer.close()
    
    for video_type in type_writers.values():
        for split in video_type.values():
            for writer in split.values():
                writer.close()



anno_file_path='/data/lxy/datasets/tiktalk_1012/offical/all_textual_and_visual_annotations_format.jsonl'
video_title_path='/data/lxy/datasets/tiktalk_1012/offical/video_titles.jsonl'
split_file_path='/data/lxy/datasets/tiktalk_1012/offical/split.jsonl'
output_dir='/data/lxy/datasets/tiktalk_1012/offical/data'
os.makedirs(output_dir, exist_ok=True)  

split_different_modality_annotations(anno_file_path,video_title_path,output_dir)

split_data_by_type_and_split(output_dir,split_file_path)
