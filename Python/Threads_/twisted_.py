from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):
    print('all_done')
    reactor.stop()


def one_done(contents):
    print('one_done')


deferred_list = []

url_list = [
            'http://www.bing.com',
            'http://www.baidu.com',
            'http://www.github.com',
            ]

for url in url_list:
    # 发送HTTP请求
    deferred = getPage(bytes(url, encoding='utf8'))