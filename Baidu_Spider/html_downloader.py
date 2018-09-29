# 下载器

from http import cookiejar
from urllib import request, error
from urllib.parse import urlparse

class HtmlDownLoader(object):
    def download(self, url, retry_count=2, headers=None, proxy=None, data=None):
        if url is None:
            return None
        try:
            req = request.Request(url, headers=headers, data=data)  #获取url
            cookie = cookiejar.CookieJar()  #创建cookie容器
            cookie_process = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener()  #创建operner
            if proxy:
                proxies = {urlparse(url).scheme: proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = opener.open(req).read()  #下载内容
        except error.URLError as e:
            print('HtmlDownLoader download error:', e.reason)
            content = None
            if retry_count > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    #说明是 HTTPError 错误且 HTTP CODE为5XX 范围说明是服务器错误，可以尝试再次下载
                    return self.download(url, retry_count-1, headers, proxy, data)
        return content  #返回下载内容
