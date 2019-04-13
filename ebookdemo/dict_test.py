# -*- coding: utf-8 -*-
import sys

from ebookdemo.items import EbookdemoItem
import json


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


if __name__ == '__main__':
    f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()

    # main_dict = EbookdemoItem()
#     # chapter_dict = EbookdemoItem()
#     # chapter_dict['chapter_name'] = '第一章 明天'
#     # chapter_dict['chapter_content'] = '雨，连绵下了多日，仍然没有停的意思。    收拾了乱七八糟的玉简、书册后，张凡走到窗前，望着接天的雨帘久久无语，最终化作了一声长叹'
#     #
#     # chapter_dict_2 = EbookdemoItem()
#     # chapter_dict_2['chapter_name'] = '第二章 大开山门'
#     # chapter_dict_2['chapter_content'] = '雨，连绵下了多日，仍然没有停的意思。    收拾了乱七八糟的玉简、书册后，张凡走到窗前，望着接天的雨帘久久无语，最终化作了一声长叹'
#     #
#     # if main_dict.get('chapter_list', None) is None:
#     #     print('not have chapter_list')
#     #     main_dict['chapter_list'] = [chapter_dict, chapter_dict_2]
#     #
#     # print(main_dict['chapter_list'][-1])
#     #
#     # list = [1, 2, 3, 4]
#     # it = iter(list)  #生成迭代对象
#     # for x in it:
#     #     print(x, end="\n")

# print(dict(chapter_dict))
