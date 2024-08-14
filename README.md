[中文](./README.zh.md)

# Porn-Video-Scraper

## Overview
This script is designed to download and convert videos from the pornographic website "jieav.com". It utilizes Selenium for web navigation, BeautifulSoup for HTML parsing, and FFmpeg for video conversion. The script can be configured to search for specific keywords, download a limited number of videos, and handle both M3U8 and MP4 video formats.

Users who are too lazy to read the README can [click here](https://github.com/ystemsrx/Porn-Video-Scraper/releases) to go to the Releases section and download the executable file to run it directly (Windows).

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

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
This script is intended for educational purposes only. The user is responsible for complying with all applicable laws and regulations regarding the downloading and use of content from the internet.
