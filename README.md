[中文](./README.zh.md)

# Porn-Video-Scraper

## Overview
This script is designed to download and convert videos from the pornographic website "jieav.com". It utilizes Selenium for web navigation, BeautifulSoup for HTML parsing, and FFmpeg for video conversion. The script can be configured to search for specific keywords, download a limited number of videos, and handle both M3U8 and MP4 video formats.

## Features
- **Web Scraping**: Uses Selenium and BeautifulSoup to navigate and parse HTML pages.
- **Video Download**: Supports downloading both M3U8 and MP4 video formats.
- **Video Conversion**: Converts M3U8 streams to MP4 using FFmpeg.
- **Keyword Filtering**: Allows specifying positive and negative keywords to filter video downloads.
- **Progress Tracking**: Utilizes `tqdm` for displaying download and conversion progress.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- FFmpeg
- Tqdm
- WebDriver Manager

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/ystemsrx/Porn-Video-Scraper
   cd VideoScraperDownloader
   ```

2. **Install Python Dependencies**
   ```sh
   pip install selenium beautifulsoup4 requests tqdm webdriver-manager
   ```

3. **Install FFmpeg**
   - Windows: Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add to PATH.
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

## Configuration
- **Positive Keywords**: Add keywords to `positive_keywords` list to include videos that match these keywords.
- **Negative Keywords**: Add keywords to `negative_keywords` list to exclude videos that match these keywords.
- **Search Keywords**: Add search terms to `search_words` list to search specific videos.
- **Download Limit**: Set `download_limit` to control the number of videos to download (0 for unlimited).

## Usage
1. **Set Configuration**: Update the script with your desired configuration for keywords, download limit, and other settings.
2. **Run the Script**:
   ```sh
   python Porn-Video-Scraper.py
   ```
## GUI Version
This script also includes a GUI version for easier use. The GUI allows you to configure settings, start downloads, and monitor progress through a user-friendly interface. Run `python Porn-Video-Scraper-GUI.py`.

## Functions

### `download_and_convert_m3u8(url, output_file)`
Downloads and converts M3U8 streams to MP4.

### `get_m3u8_duration(url)`
Fetches the duration of an M3U8 stream.

### `parse_duration(line)`
Parses duration from FFmpeg output.

### `process_page(driver, page_url, page_name, video_count, download_folder)`
Processes a webpage to find and download videos.

### `download_file(url, file_name)`
Downloads a file from a given URL.

### `search_and_process(driver, search_word, video_count)`
Searches for videos based on a keyword and processes the results.

### `main()`
Main function that initializes the web driver and starts the download process.

## Logging
The script uses Python's `logging` module. Log level is set to `ERROR` to minimize log output. Adjust log level as needed for debugging.

## VPN Requirement
If you are accessing this script from mainland China, a VPN is required to reach the target website and download the videos.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
This script is intended for educational purposes only. The user is responsible for complying with all applicable laws and regulations regarding the downloading and use of content from the internet.
