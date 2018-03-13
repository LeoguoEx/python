from data import DouBanMovie
from lxml import etree

def main(baseUrl = "", param = ""):
    data = DouBanMovie();
    html = etree.parse('黑豹 (豆瓣).htm', etree.HTMLParser())
    data.parseHtml(html)
    data.print()

if __name__ == "__main__":
    main()