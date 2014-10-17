#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified:	2014-10-10 14:39
# Filename:		Weibo.py
__author__='zhangfan'


import re

def Weibo_Content():
	global f
	while True:
		line = f.readline()
		title = line.find(r'<div class="WB_text')#微薄正文标签
		if title > 0:
			end_num = line.find(r'<img')
			content_num = line.find(r'feed_list_content',title,end_num)
			content = line[content_num + 19: end_num]
			content_other_num  = content.find(r'<')
			if content_other_num > 0:
				print content[0:content_other_num]#去掉结尾包含</div>
			else:
				print content
			
		else :
			pass
		if line != '':
			pass
		else:
			break
			f.close()

def Weibo_img():
	global f1
	
	while True:
		line = f1.readline()
		bigcursor_num = line.find(r'<img class="bigcursor') #单独一张图标签
		if bigcursor_num > 0:
			start_img_src = line.find(r'src',bigcursor_num)
			end_len_bigcursor = line.find(r'.jpg',start_img_src)
			small_simple_img_url = line[start_img_src + 5: end_len_bigcursor + 4]
			small_simple_type = re.compile('(thumbnail|square)')

			big_simple_img_url = small_simple_type.sub('bmiddle',small_simple_img_url)
			print big_simple_img_url
			print small_simple_img_url
		else:
			pass
		mulit_img_num = line.find(r'<img alt=')#多图标签
		if mulit_img_num > 0:
			start_mulit_img_src = line.find(r'src',mulit_img_num)
			if line.find(r'.jpg',start_mulit_img_src) != -1:
				end_len_mulit_img = line.find(r'.jpg',start_mulit_img_src)
			else:
				pass
			if line.find(r'.gif',start_mulit_img_src) != -1:
				end_len_mulit_img = line.find(r'.gif',start_mulit_img_src) 
			else:
				pass
			small_mulit_img_url = line[start_mulit_img_src + 5: end_len_mulit_img + 4]
			big_mulit_type = re.compile('(thumbnail|square)')
			big_mulit_img_url = big_mulit_type.sub('bmiddle',small_mulit_img_url)
			print small_mulit_img_url
			print big_mulit_img_url
		else:
			pass
		if line != '':
			pass
		else:
			break
			f.close()

def Weibo_cut():
	map(lambda i: file('weibo_%d.txt' % i[0], 'w').write(i[1]), enumerate(re.findall(r'( <!--//top标题-->.*? <!--top标题-->)', file('hot2.htm').read(), re.S)))
if __name__ == '__main__':
	#Weibo_cut()
	for i in range(9):
		f = file("weibo_%d.txt" % i,'r')
		f1 = file("weibo_%d.txt" % i,'r')
		print "----------------------------------------------"
		Weibo_Content()
		Weibo_img()
		print "----------------------------------------------"
