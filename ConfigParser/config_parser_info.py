#encoding:UTF-8
import ConfigParser
import string

import sys

def config_read():
    config_path = './dbconf.cfg'
    #ConfigParser读取
    cp = ConfigParser.SafeConfigParser()
    print cp.read(config_path)
    print cp.sections()
    print cp.options(cp.sections()[0])
    print cp.get('dbconfig','host')

#================================================

def configparser_write():
    #ConfigParser写入
    # 初始化 ConfigParser
    config_writer = ConfigParser.ConfigParser()
    # 添加 book 节点
    config_writer.add_section("book")
    # book 节点添加 title,author 配置
    config_writer.set("book","title","Python: The Hard Way")
    config_writer.set("book","author","anon")
    # 添加 ematter 节点和 pages 配置
    config_writer.add_section("ematter")
    config_writer.set("ematter","pages",250)
    # 将配置信息输出到标准输出
    config_writer.write(sys.stdout)
    # 将配置文件输出到文件
    config_writer.write(open('new_book.info','w'))


#===============更新、删除节点=====================

def config_parser_update():
    update_config_parser = ConfigParser.ConfigParser()
    update_config_parser.read('new_book.info')
    print "section 信息:",update_config_parser.sections()
    # 更新作者名称
    print "原作者:",update_config_parser.get("book","author")
    # 更改作者姓名为 Jack
    update_config_parser.set("book","author","Jack")
    print "更改后作者名称:",update_config_parser.get("book","author")
    # 如果 ematter 节点存在,则删除
    if update_config_parser.has_section("ematter"):
        update_config_parser.remove_section("ematter")

    # 输出信息
    update_config_parser.write(sys.stdout)
    # 覆盖原配置文件信息
    update_config_parser.write(open('new_book.info','w'))

def base_parser():
    '''
    [DEFAULT]
    info = 数据库地址
    connect_mysql = mysql -h %(host)s -P %(port)s -u %(user)s -p%(passwd)s


    [dbconfig]
    # 数据库读库链接信息
    host=127.0.0.1
    user=root
    passwd=wangquan
    database=banma_finance
    port=3306

    [dbconfig1]
    # 数据库读库链接信息
    host=127.0.0.1
    user=root
    passwd=root
    database=banma_finance
    port=3306
    :return:
    '''
    config_read = ConfigParser.SafeConfigParser()
    print config_read.read('./base_config.info')
    print config_read.sections()
    #dbconfig 中没有info默认读DEFAULT中的info
    print config_read.get('dbconfig','info')
    #connect_mysql = mysql -h %(host)s -P %(port)s -u %(user)s -p%(passwd)s
    #DEFAULT 中connect_mysql语法写成%(host)s这样，在用get方法读取其他节点时会默认替换里面的数据
    print config_read.get('dbconfig','connect_mysql')

if __name__ == '__main__':
    base_parser()