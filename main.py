import feedparser
import os
from datetime import datetime

# Simple AI Daily Digest Bot - OpenAI Skills Studio
def fetch_news():
    print("🤖 Fetching AI News...")
    feed = feedparser.parse("https://news.ycombinator.com/rss")
    news = []
    for entry in feed.entries[:5]:
        news.append(f"- {entry.title}: {entry.link}")
    return news

def generate_digest(news):
    print("✨ Generating Digest...")
    digest = f"# AI Daily Digest - {datetime.now().strftime('%Y-%m-%d')}\n\n"
    digest += "## Top AI News Today\n"
    for n in news:
        digest += n + "\n"
    
    digest += "\n## Python Jobs / Internships\n"
    digest += "- Check LinkedIn: search 'Python Internship'\n"
    digest += "- Check Wellfound: wellfound.com/role/l/python\n"
    
    digest += "\n\nThis digest saves 1 hour daily by summarizing everything!"
    digest += "\n\nBuilt by Ramya - B.Tech AIML"
    return digest

def main():
    news = fetch_news()
    digest = generate_digest(news)
    
    with open("daily_digest.md", "w") as f:
        f.write(digest)
    
    print(digest)
    print("\n✅ Digest saved to daily_digest.md")

if __name__ == "__main__":
    main()
