# Spider - Web Image Scraper

## Overview
The **Spider** program is a simple Python-based web scraper designed to recursively download images from a given URL. It supports configurable recursion depth and allows you to save the downloaded images to a specified directory.

## Features
- Download images with extensions: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`.
- Recursively scrape images from linked pages up to a configurable depth.
- Save images to a specified directory (default: `./data/`).

## Requirements
Ensure you have Python installed (version 3.8 or later). Install the necessary Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

### Command Syntax
```bash
python spider.py [-r] [-l DEPTH] [-p PATH] URL
```

### Options
- `-r`: Enable recursive scraping (default depth: 5).
- `-l DEPTH`: Set the maximum depth level for recursion (only works with `-r`).
- `-p PATH`: Specify the directory to save downloaded images (default: `./data/`).
- `URL`: The starting URL to scrape.

### Examples

#### Download all images from a single webpage
```bash
python spider.py https://example.com
```

#### Recursively scrape images with default depth (5 levels)
```bash
python spider.py -r https://example.com
```

#### Recursively scrape images with a custom depth of 3
```bash
python spider.py -r -l 3 https://example.com
```

#### Save images to a custom directory
```bash
python spider.py -r -l 2 -p ./my_images/ https://example.com
```

## Notes
- Ensure the URL you provide is valid and accessible.
- Respect websites' `robots.txt` policies and scrape responsibly.

## Troubleshooting
- If the program doesn't download any images, check if the site loads images dynamically with JavaScript. This script does not support scraping JavaScript-rendered content.
- Make sure the specified output path exists or can be created.

## Resource

https://docs.python.org/3/library/argparse.html