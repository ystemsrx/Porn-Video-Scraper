import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import logging
from tqdm import tqdm
import re

import urllib.parse

# Custom keywords
positive_keywords = []
negative_keywords = []

# Search keywords
search_words = []

# Website URL
base_url = 'https://www.jieav.com'

# Control the number of videos to download, enter 0 to run indefinitely, enter a number > 0 to download a specific number of videos
download_limit = 0

# Set log level to ERROR to disable most log outputs
logging.basicConfig(level=logging.ERROR)

def download_and_convert_m3u8(url, output_file):
    retries = 2
    while retries > 0:
        try:
            print(f"Downloading and converting {url} to {output_file}...")
            total_duration = get_m3u8_duration(url)
            with tqdm(total=total_duration, desc=f"Converting {output_file}", unit='s', dynamic_ncols=True) as pbar:
                process = subprocess.Popen(
                    ['ffmpeg', '-i', url, '-c', 'copy', output_file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                    encoding='utf-8'
                )
                for line in process.stdout:
                    duration = parse_duration(line)
                    if duration:
                        pbar.update(duration - pbar.n)
                process.wait()
                if process.returncode == 0:
                    print(f"Converted to {output_file}")
                    return True
                else:
                    print(f"Error during conversion: {line}")
        except Exception as e:
            print(f"Error during conversion: {e}")
        retries -= 1
        print(f"Retrying... ({2 - retries} attempts left)")
    print(f"Failed to convert {url}")
    return False

def get_m3u8_duration(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        duration = 0
        for line in content.splitlines():
            if line.startswith("#EXTINF"):
                duration += float(line.split(":")[1].split(",")[0])
        return int(duration)
    except Exception as e:
        print(f"Error getting m3u8 duration: {e}")
        return 0

def parse_duration(line):
    match = re.search(r'time=(\d+:\d+:\d+.\d+)', line)
    if match:
        time_str = match.group(1)
        h, m, s = map(float, time_str.split(':'))
        return int(h * 3600 + m * 60 + s)
    return 0

def process_page(driver, page_url, page_name, video_count, download_folder):
    print(f"Analyzing page: {page_url}")
    driver.get(page_url)
    time.sleep(5)  # Wait for the page to load completely
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    video_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and (href.endswith('.m3u8') or href.endswith('.mp4')):
            video_links.append(href)

    if not video_links:
        print(f"No video links found on {page_url}")
    else:
        for video_link in video_links:
            if video_count[0] == download_limit and download_limit > 0:
                return  # Stop downloading when reaching the download limit

            video_url = video_link if video_link.startswith('http') else base_url + video_link
            file_name = os.path.join(download_folder, page_name + '.mp4')
            if video_url.endswith('.m3u8'):
                if not download_and_convert_m3u8(video_url, file_name):
                    continue  # Skip downloading failed videos
            else:
                if not download_file(video_url, file_name):
                    continue  # Skip downloading failed videos

            video_count[0] += 1  # Update the download count

def download_file(url, file_name):
    retries = 2
    while retries > 0:
        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            with open(file_name, 'wb') as f, tqdm(
                desc=file_name,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in response.iter_content(chunk_size=1024):
                    size = f.write(data)
                    bar.update(size)
            print(f"Downloaded {file_name}")
            return True
        except requests.RequestException as e:
            print(f"Error during download: {e}")
            retries -= 1
            print(f"Retrying... ({2 - retries} attempts left)")
    print(f"Failed to download {url}")
    return False

def search_and_process(driver, search_word, video_count):
    page_num = 1
    download_folder = os.path.join(os.getcwd(), search_word)
    os.makedirs(download_folder, exist_ok=True)

    while True:
        search_url = f"{base_url}/tabs/{urllib.parse.quote(search_word)}.html"
        if page_num > 1:
            search_url = f"{base_url}/tabs/{urllib.parse.quote(search_word)}-{page_num}.html"
        print(f"Searching with URL: {search_url}")
        driver.get(search_url)
        time.sleep(5)  # Wait for the search results to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        if not soup.find_all('a'):
            print(f"No more pages for {search_word}")
            break

        for link in soup.find_all('a'):
            if video_count[0] == download_limit and download_limit > 0:
                return  # Stop downloading when reaching the download limit

            href = link.get('href')
            if href and 'play' in href and href.endswith('.html'):
                page_url = base_url + href if href.startswith('/') else base_url + '/' + href
                driver.get(page_url)
                time.sleep(5)  # Wait for the page to load completely
                page_soup = BeautifulSoup(driver.page_source, 'html.parser')
                meta_description = page_soup.find('meta', {'name': 'description'})
                page_name = meta_description.get('content', '').strip() if meta_description else href.split('/')[-1].replace('.html', '')

                # Check positive and negative keywords
                if positive_keywords and not any(keyword in page_name for keyword in positive_keywords):
                    print(f"Skipping {page_name} due to missing positive keywords.")
                    continue
                if negative_keywords and any(keyword in page_name for keyword in negative_keywords):
                    print(f"Skipping {page_name} due to presence of negative keywords.")
                    continue

                process_page(driver, page_url, page_name, video_count, download_folder)
                print(f"Returning to search results for {search_word}")

        page_num += 1

def main():
    print(f"Reading {base_url}")

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Use headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")  # Set log level

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(base_url)
    time.sleep(5)  # Wait for the page to load completely

    video_count = [0]  # Track the number of downloaded videos

    def check_keywords_and_process(link, video_count):
        href = link.get('href')
        if href and 'play' in href and href.endswith('.html'):
            page_url = base_url + href if href.startswith('/') else base_url + '/' + href
            driver.get(page_url)
            time.sleep(5)  # Wait for the page to load completely
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            meta_description = soup.find('meta', {'name': 'description'})
            page_name = meta_description.get('content', '').strip() if meta_description else href.split('/')[-1].replace('.html', '')

            # Check positive and negative keywords
            if positive_keywords and not any(keyword in page_name for keyword in positive_keywords):
                print(f"Skipping {page_name} due to missing positive keywords.")
                return
            if negative_keywords and any(keyword in page_name for keyword in negative_keywords):
                print(f"Skipping {page_name} due to presence of negative keywords.")
                return

            process_page(driver, page_url, page_name, video_count, os.getcwd())

    if search_words:
        for word in search_words:
            if video_count[0] == download_limit and download_limit > 0:
                break  # Stop downloading when reaching the download limit
            search_and_process(driver, word, video_count)
    else:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for link in soup.find_all('a'):
            if video_count[0] == download_limit and download_limit > 0:
                break  # Stop downloading when reaching the download limit

            check_keywords_and_process(link, video_count)

    driver.quit()

if __name__ == '__main__':
    main()
