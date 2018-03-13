from data import DouBanMovie
from lxml import etree
from request import UrlRequests

def main(baseUrl = "", param = ""):
    '''
    data = DouBanMovie();
    html = etree.parse('黑豹 (豆瓣).htm', etree.HTMLParser())
    data.parseHtml(html)
    data.print()
    '''
    request = UrlRequests()
    request.addNeedRequestUrl('https://movie.douban.com/subject/3878007/?from=subject-page')
    request.addNeedRequestUrl('111')
    request.addNeedRequestUrl('https://movie.douban.com/subject/6390825/?from=showing')
    request.addNeedRequestUrl('https://movie.douban.com/subject/3168101/?from=subject-page')
    request.addNeedRequestUrl('000')

    while(request.requestNext()):
        request.request()

if __name__ == "__main__":
    main()