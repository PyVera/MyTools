#引入模块
import url_manager, html_downloader, html_parser, html_output, sys

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  #url管理器
        self.downloader = html_downloader.HtmlDownLoader()  #下载器
        self.parser = html_parser.HtmlParser()  #解析器
        self.out_put = html_output.HtmlOutput()  #输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  #调用url管理器，将入口url添加，url管理器中就拥有了带爬取的url
        #编写爬虫循环
        while self.urls.has_new_url():  #调用url管理器，当有新url时
            try:
                new_url = self.urls.get_new_url()  #调用url管理器，获取相关url
                print("craw %d : %s" % (count, new_url))
                headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"} #添加headers，将爬虫伪装成游览器
                html_content = self.downloader.download(new_url, retry_count=2, headers=headers)  #调用下载器，下载页面
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8") #调用解析器，解析数据，获取批量url和数据
                self.urls.add_new_urls(new_urls) #调用url管理器，将批量新url添加入url管理器，构成循环
                self.out_put.collect_data(new_data) #调用输出器，收集数据
                if count == 30: #爬取30个
                    break
                count = count + 1
            except:  #异常处理
                print("craw failed!")
        self.out_put.output_html() #调用输出器，输出数据

# 编写__mail__函数，设置要爬取的入口url
if __name__ == "__main__":
    rootUrl = "http://baike.baidu.com/item/Python"  #入口url
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)  #启动爬虫
