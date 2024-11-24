from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
def scrape_youtube():
    url = "https://www.youtube.com/feed/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    videos = soup.find_all("a", {"id": "video-title"})
    return [{"title": v.text.strip(), "link": f"https://youtube.com{v['href']}"} for v in videos[:5]]
def scrape_amazon():
    headers = {"User-Agent": "Your User-Agent"}
    url = "https://www.amazon.com/s?k=laptop"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("span", {"class": "a-size-medium"})
    return [{"title": item.text.strip()} for item in items[:5]]
@app.route("/")
def home():
    youtube_data = scrape_youtube()
    amazon_data = scrape_amazon()
    return render_template("scraper.html", youtube=youtube_data, amazon=amazon_data)
if __name__ == "__main__":
    app.run(debug=True)
