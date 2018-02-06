#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='test',
    version='1.0.0.dev',
    description=(
        '<项目的简单描述>'
    ),
    long_description=open('README.rst').read(),
    author='<wangquan>',
    author_email='<13126655557@163.com>',
    maintainer='<wangquan>',
    maintainer_email='<13126655557@163.com>',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='<项目的网址，我一般都是github的url>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)


#!/usr/bin/env python
from setuptools import setup

# setup(
#     name='hive-executor-py',
#     version='1.0.0.dev1',
#     description='A hive client python project',
#     url='https://github.com/calvinjiang/hive-executor-py',
#     author='Calvin Jiang',
#     author_email='jianghuachinacom@163.com',
#     license='MIT',
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Intended Audience :: Developers',
#         'Topic :: Software Development :: Build Tools',
#         'License :: OSI Approved :: MIT License',
#         'Programming Language :: Python :: 2.6',
#         'Programming Language :: Python :: 2.7',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#     ],
#     keywords='hive client python',
#     packages=['hive'],
# )