from PIL import Image
from io import BytesIO
import base64
import os
import csv

def write_image_data(writer, image_id, image_path):
    """Convert image to Base64 and write to TSV with image_id"""
    with Image.open(image_path) as img:
        with BytesIO() as buffer:
            img.save(buffer, format=img.format)
            writer.writerow([
                image_id,
                base64.b64encode(buffer.getvalue()).decode('utf-8')
            ])

def process_images_to_tsv(image_dir, output_tsv):
    """Write images in TSV file"""
    with open(output_tsv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                write_image_data(
                    writer,
                    os.path.splitext(filename)[0],
                    os.path.join(image_dir, filename)
                )

if __name__ == '__main__':
    process_images_to_tsv(
        image_dir='/data/lxy/datasets/tiktalk_1012/faces_all',
        output_tsv='/data/lxy/datasets/tiktalk_1012/image_base64.tsv'
    )
