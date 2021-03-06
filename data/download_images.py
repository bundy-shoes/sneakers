import argparse
from pathlib import Path

from data.config import DATA_CSV_NAME, IMAGES_DIR_NAME
from data.utils import download_images, load_data_from_csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", "-o", type=str, required=True)
    args = parser.parse_args()

    directory = Path(args.output_dir)
    df = load_data_from_csv(directory / DATA_CSV_NAME)

    images_output_dir = directory / IMAGES_DIR_NAME
    images_output_dir.mkdir(exist_ok=True)

    download_images(df, output_dir=images_output_dir)
