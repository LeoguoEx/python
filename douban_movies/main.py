from request import UrlRequests
from data_manager import DataManager

def main(url):

    data_manager = DataManager()
    request = UrlRequests()
    request.setRequestEndAction(data_manager.parseHtml)
    request.addNeedRequestUrl(url)
    


    '''    
    data = DouBanMovie();
    html = etree.parse('黑豹 (豆瓣).htm', etree.HTMLParser())
    data.parseHtml(html)
    data.print()
    
    
    request = UrlRequests()
    request.addNeedRequestUrl('https://movie.douban.com/subject/3878007/?from=subject-page')
    request.addNeedRequestUrl('111')
    request.addNeedRequestUrl('https://movie.douban.com/subject/6390825/?from=showing')
    request.addNeedRequestUrl('https://movie.douban.com/subject/3168101/?from=subject-page')
    request.addNeedRequestUrl('000')

    while(request.requestNext()):
        request.request()
    '''

if __name__ == "__main__":
    main()