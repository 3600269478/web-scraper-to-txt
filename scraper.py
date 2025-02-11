import requests
from bs4 import BeautifulSoup

# 目标网站URL
URL = "https://example.com"  # 替换为你想要抓取的网站地址

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取所有段落文本
        paragraphs = soup.find_all('p')
        text_content = '\n'.join([p.get_text() for p in paragraphs])
        
        return text_content
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

if __name__ == "__main__":
    content = scrape_website(URL)
    if content:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(content)
