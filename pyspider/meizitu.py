#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-07-07 23:48:09
# Project: meizitu

from pyspider.libs.base_handler import *
import os, pprint, json

PAGE_START = 1
PAGE_END = 30
DIR_PATH = '/Users/wangquan/meizitu_crawler'


class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.base_url = 'http://www.mmjpg.com/home/'
        self.page_num = PAGE_START  # start crawl page
        self.total_num = PAGE_END  # end crawl page
        self.deal = Deal()

    @every(minutes=24 * 60)
    def on_start(self):
        # 首页
        while self.page_num <= self.total_num:
            url = self.base_url + str(self.page_num)
            print "step 1"
            print url
            self.crawl(url, callback=self.index_page, fetch_type='js')
            self.page_num += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        # 首页cell
        for each in response.doc('li a').items():
            print "step 2"
            first_url = each.attr.href
            print first_url
            self.crawl(first_url, callback=self.detail_page, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        # 详情页页码
        print "step 3"
        end_page = response.doc('.page > a').text().split(" ")[-2]

        image_list = int(end_page)
        print image_list
        for image_page in range(1, image_list + 1):
            page_url = '%s/%s' % (response.url, image_page)
            self.crawl(page_url, callback=self.download_image, fetch_type='js')

    def download_image(self, response):
        # 详情页info
        print "step 4"
        detail_info = {
            "url": response.url,
            "title": response.doc('title').text(),
            "date": response.doc('.info').text(),
            "end_page": response.doc('.page > a').text().split(" ")[-2],
            "image_url": response.doc('.content img').items()
        }
        pprint.pprint(detail_info)
        name = detail_info['title'].split('(')[0].split('_')[0]
        imgs = response.doc('.content img').items()
        # 创建文件夹
        dir_path = self.deal.mkDir(name)
        # 存储model_info
        self.deal.saveBrief(detail_info['url'] + detail_info['title'] + detail_info['date'], dir_path, name)
        # 存储img
        imgs = response.doc('.content img').items()
        for img in imgs:
            url = img.attr.src
            if url:
                extension = self.deal.getExtension(url)
                file_name = ''.join(detail_info['url'].split('/')[-3:]) + '.' + extension
                print file_name
                self.crawl(url, callback=self.save_img,
                           save={'dir_path': dir_path, 'file_name': file_name})

    def save_img(self, response):
        # 下载
        print 'step 5'
        content = response.content
        dir_path = response.save['dir_path']
        file_name = response.save['file_name']
        file_path = dir_path + '/' + file_name
        self.deal.saveImg(content, file_path)
        print file_path


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