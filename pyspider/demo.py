#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-07-02 16:58:25
# Project: taobao_mm

from pyspider.libs.base_handler import *
import os

PAGE_START = 1
PAGE_END = 30
DIR_PATH = '/Users/wangquan/taobao_mm'


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.base_url = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.page_num = PAGE_START  # start crawl page
        self.total_num = PAGE_END  # end crawl page
        self.deal = Deal()

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            print url
            self.crawl(url, callback=self.index_page)
            self.page_num += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.lady-name').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        domain = 'https:' + response.doc('.mm-p-domain-info li > span').text()
        print domain
        self.crawl(domain, callback=self.domain_page)

    def domain_page(self, response):
        name = response.doc('.mm-p-model-info-left-top dd > a').text()
        dir_path = self.deal.mkDir(name)
        brief = response.doc('.mm-aixiu-content').text()
        if dir_path:
            imgs = response.doc('.mm-aixiu-content img').items()
            count = 1
            self.deal.saveBrief(brief, dir_path, name)
            for img in imgs:
                url = img.attr.src
                if url:
                    extension = self.deal.getExtension(url)
                    file_name = name + str(count) + '.' + extension
                    count += 1
                    self.crawl(img.attr.src, callback=self.save_img,
                               save={'dir_path': dir_path, 'file_name': file_name})

    def save_img(self, response):
        content = response.content
        dir_path = response.save['dir_path']
        file_name = response.save['file_name']
        file_path = dir_path + '/' + file_name
        self.deal.saveImg(content, file_path)


class Deal:
    def __init__(self):
        self.path = DIR_PATH
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def mkDir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path

    def saveImg(self, content, path):
        f = open(path, 'wb')
        f.write(content)
        f.close()

    def saveBrief(self, content, dir_path, name):
        file_name = dir_path + "/" + name + ".txt"
        f = open(file_name, "w+")
        f.write(content.encode('utf-8'))

    def getExtension(self, url):
        extension = url.split('.')[-1]
        return extension
