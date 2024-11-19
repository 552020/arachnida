import os
import sys
import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_metadata(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            print(f"\n=== Metadata for {image_path} ===")
            # Extract basic image info
            print(f"Format: {img.format}")
            print(f"Mode: {img.mode}")
            print(f"Size: {img.size}")

            # Try to extract EXIF metadata
            exif_data = img._getexif()
            if exif_data is None:
                print("No EXIF metadata found.")
                return

            # Parse EXIF metadata
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                if tag_name == "GPSInfo":
                    gps_data = {GPSTAGS.get(k, k): v for k, v in value.items()}
                    print(f"{tag_name}: {gps_data}")
                else:
                    print(f"{tag_name}: {value}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract metadata from image files.")
    parser.add_argument("files", nargs="+", help="Paths to image files to process")
    args = parser.parse_args()

    for image_path in args.files:
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue
        # Check if the file has a valid extension
        if not image_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            print(f"Unsupported file type: {image_path}")
            continue
        extract_metadata(image_path)

if __name__ == "__main__":
    main()
