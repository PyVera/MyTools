# 输出器
# 这里简单用一个 WEB 页面把爬取的所有存在在 datas 列表的数据以 Table 输出。
import time

class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    #拥有收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    #用于以列表形式输出
    def output_html(self):
        file_name = time.strftime("%Y-%m-%d_%H:%M:%S")  #建立文件输出对象
        with open("out_%s.html" % file_name, "w") as f_out:
            f_out.write("<html>")  #编写<html>标签
            f_out.write(r'<head>'
                        r'<link rel="stylesheet" '
                        r'href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" '
                        r'integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" '
                        r'crossorigin="anonymous"></head>')  #编写<head>及其闭合标签
            f_out.write("<body>")  #编写<body>标签
            f_out.write(r'<table class="table table-bordered table-hover">')  #编写<table>标签

            item_css = ['active', 'success', 'warning', 'info']
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                f_out.write(r'<tr class="'+item_css[index]+r'">')
                f_out.write('<td>%s</td>' % data["url"])  #创建行
                f_out.write('<td>%s</td>' % data["title"])
                f_out.write('<td>%s</td>' % data["summary"])
                f_out.write("</tr>")

            f_out.write("</table>") #编写<table>闭合标签
            f_out.write("</body>") #编写<body>闭合标签
            f_out.write("</html>") #编写<html>闭合标签
