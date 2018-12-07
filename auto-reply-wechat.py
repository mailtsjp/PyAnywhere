#!/usr/bin/env python
# -- coding: utf-8 --
import itchat, time, re, sys, urllib2, json
from urllib import quote,unquote,urlencode
from itchat.content import *
@itchat.msg_register([TEXT])
def text_reply(msg):
    global index
    index = index + 1
    if index == 1:
        m1 = unicode('我已经休息或者在上课,下面的内容是我的语言机器人自动回复的','gb2312')
        itchat.send((m1),msg['FromUserName'])
        m2 = unicode('对了,它比较粗鲁,请不要轻易说脏话','gb2312')
        itchat.send((m2),msg['FromUserName'])    
    else:
	    m = quote(msg['Text'].encode('utf8'))
	    #http://api.qingyunke.com/api.php?key=free&appid=0&msg=  
	    #url = 'http://sandbox.api.simsimi.com/request.p?key=9470057a-909b-4e6c-a25d-19e0834d6667&lc=zh&ft=1.0&text='+m
	    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='+m
	    print url
	    raw = urllib2.urlopen(url)
	    try:
	      data = json.loads(raw.read().decode('utf-8'))
	      #print data['response']
	      print data['content']
	      itchat.send((data['content']), msg['FromUserName'])
	    except:
	        pass	  
@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def pic_reply(msg):
    itchat.send((unicode('图片不错','gb2312')),msg['FromUserName'])
    #itchat.send('@img@1.jpg', msg['FromUserName'])
if __name__ == '__main__':
    default_encoding = 'utf-8'
    index = 0
    if sys.getdefaultencoding() != default_encoding:
        itchat.auto_login(enableCmdQR=False,hotReload=True)
        itchat.run()