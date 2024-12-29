[English](./README.md)

# 色情视频抓取器

**想看小说？**：使用我的小说抓取脚本[Porn Novel Scraper](https://github.com/ystemsrx/Porn-Novel-Scraper)

## 概述
此脚本旨在从色情网站“jieav.com”下载和转换视频。它使用 Selenium 进行网页导航，使用 BeautifulSoup 进行 HTML 解析，并使用 FFmpeg 进行视频转换。脚本可以配置为搜索特定关键字、下载有限数量的视频，并处理 M3U8 和 MP4 视频格式。

懒得看README的用户可以[在此](https://github.com/ystemsrx/Porn-Video-Scraper/releases)前往Releases下载可执行文件直接运行（Windows）。

## 特点
- **网页抓取**：使用 Selenium 和 BeautifulSoup 进行网页导航和解析。
- **视频下载**：支持下载 M3U8 和 MP4 视频格式。
- **视频转换**：使用 FFmpeg 将 M3U8 流转换为 MP4。
- **关键字过滤**：允许指定正面和负面关键字以过滤视频下载。
- **进度跟踪**：使用 `tqdm` 显示下载和转换进度。

## 需求
- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- FFmpeg
- Tqdm
- WebDriver Manager

## 安装
1. **克隆仓库**
   ```sh
   git clone https://github.com/ystemsrx/Porn-Video-Scraper.git
   cd VideoScraperDownloader
   ```

2. **安装 Python 依赖**
   ```sh
   pip install selenium beautifulsoup4 requests tqdm webdriver-manager
   ```

3. **安装 FFmpeg**
   - Windows: 从 [FFmpeg.org](https://ffmpeg.org/download.html) 下载并添加到 PATH。
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

## 配置
- **正面关键字**：在 `positive_keywords` 列表中添加关键字以包含匹配这些关键字的视频。
- **负面关键字**：在 `negative_keywords` 列表中添加关键字以排除匹配这些关键字的视频。
- **搜索关键字**：在 `search_words` 列表中添加搜索词以搜索特定视频。
- **下载限制**：设置 `download_limit` 以控制要下载的视频数量（0 表示无限制）。

## 使用
1. **设置配置**：根据您的关键字、下载限制和其他设置更新脚本。
2. **运行脚本**：
   ```sh
   python Porn-Video-Scraper.py
   ```
## GUI 版本
此脚本还包括一个GUI版本，以便更轻松地使用。GUI 允许您配置设置、开始下载并通过用户友好的界面监控进度。运行`Porn-Video-Scraper-GUI.py`

## 日志记录
脚本使用 Python 的 `logging` 模块。日志级别设置为 `ERROR` 以最小化日志输出。根据需要调整日志级别以进行调试。

## VPN 要求
如果您从中国大陆访问此脚本，需要使用 VPN 才能访问目标网站并下载视频。

## 许可证
此项目根据 MIT 许可证授权。有关详细信息，请参阅 LICENSE 文件。

## 免责声明
此脚本仅用于教育目的。用户有责任遵守所有有关从互联网下载和使用内容的适用法律和法规。
