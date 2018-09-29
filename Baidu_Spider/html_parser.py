# 解析器

import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, url, content, html_encode="utf-8"):
        if url is None or content is None:  #参数判断
            return
        soup = BeautifulSoup(content, "html.parser", from_encoding=html_encode)  #content带入soup
        new_urls = self._get_new_urls(url, soup)  #解析，建立本地方法_get_new_urls
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        #解析获取所有词条url
        #href="/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975"
        links = soup.find_all("a", href=re.compile(r"/item/\w+"))  #写入正则表达式
        for link in links:
            url_path = link["href"]  #获取列表中链接
            new_url = urljoin(url, url_path) #将两个url拼接成相对应的完整url
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup):
        #解析获取title和summary两个数据
        data = {"url": url}  #字典
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")  #得到标题的标签
        data["title"] = title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div", class_="lemma-summary")  #得到简介内容
        data["summary"] = summary_node.get_text()
        return data
