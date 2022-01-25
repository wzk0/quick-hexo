#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#模块
import os
import sys
import platform

#快捷方式
def o(action):
	os.system(action)
def p(str):
	print(str)
def n():
	p("\n")
def q():
	sys.exit(1)
def re():
	action = "python3 hexo.py"
	o(action)

#检测
if platform.system() == 'Windows':
  	p('此脚本不支持Windows系统')
  	q()
else:
  	p("当前系统为: " + platform.system() + ",检测通过!")
try:
	import requests
	p("模块已安装 可以输入 update 进行更新!")
	n()
except ImportError:
	o("pip3 install requests")
	re()

#定义类
class Hexo(object):

	def __init__(self,num):
		self.num=num

	def Desktop(self):
		p("Hexo辅助脚本")
		p("由便当手打制作！")
		n()
		p("0) 更新node和npm	1) 安装Hexo所需的一切")
		p("2) 新建			3) 编辑")
		p("4) 预览			5) 上传(到Github)")
		p("6) 备份文章		7) 主题")
		p("8) 导入文章		9) 列出内容")
		p("10) 清理缓存		11) 退出")
		n()
		p("脚本使用编辑器:nano")
		p("用法:\nCtrl O保存 之后提示是否以原文件名保存 Ctrl X退出(用了就清楚了)")

	def Update(self):
		url = "https://raw.githubusercontent.com/wzk0/quick-hexo/main/hexo.py"
		r = requests.get(url)
		with open('hexo.py', 'w') as f:
			f.write(r.text)
		act = "chmod +x hexo.py"
		o(act)
		p("更新完毕！你现在可以通过 ./hexo.py 启动程序")

	def UpdateNode(self):
		print("是否需要sudo权限(Termux用户请输入n)?")
		sudo = input("y/n:")
		n()
		if sudo == "y":
			action = "sudo npm update -g && sudo npm install -g n && sudo n stable"
		if sudo == "n":
			action = "npm update -g && npm install -g n && n stable"
		o(action)

	def Download(self):
		pkg = input("请输入你的包管理器(apt/yum/pkg/其他):")
		n()
		print("是否需要sudo权限(Termux用户请输入n)?")
		sudo = input("y/n:")
		n()
		if sudo == "y":
			action = "sudo " + pkg + " install git nodejs npm nano -y && sudo npm install http-server -g && sudo npm install hexo-cli -g && sudo npm install hexo-deployer-git --save"
		if sudo == "n":
			action = pkg + " install git nodejs npm nano -y && npm install http-server -g npm install hexo-cli -g && npm install hexo-deployer-git --save"
		o(action)

	def New(self):
		p("0) 网站	1) 文章")
		p("2) 页面")
		n()
		key = input("请输入序号:")
		n( )
		if key == "0":
			websitename = input("请输入网站(文件夹)名[最好是简短难忘的]:")
			action = "hexo init " + websitename + " && cp hexo.py " + websitename
			o(action)
			p("新建网站完成！请在退出脚本后执行 cd " + websitename + " && python3 hexo.py")
			q()
		if key == "1":
			textname = input("请输入文章(链接地址)名[最好是英文字母]:")
			action = "hexo new " + textname
			o(action)
			p("是/否直接编辑?")
			choose = input("y/n:")
			if choose == "y":
				action = "nano ./source/_posts/" + textname + ".md"
				o(action)
			else:
				re()
		if key == "2":
			pagename = input("请输入网页名[最好是英文字母](实际上是链接地址):")
			action = "hexo new page " + pagename
			o(action)
			p("是/否直接编辑?")
			choose = input("y/n:")
			if choose == "y":
				action = "nano ./source/" + pagename + "/index.md"
				o(action)
			else:
				action = "python3 hexo.py"
				o(action)

	def Edit(self):
		p("0) 网站配置     1) 主题配置")
		p("2) 文章模板     3) 页面模板")
		p("4) 文章         5) 页面")
		n()
		key = input("请输入序号:")
		n()
		if key == "0":
			action = "nano _config.yml"
			o(action)
		if key == "1":
			p("目前已安装的主题:")
			n()
			action = "ls ./themes"
			o(action)
			n()
			themesname = input("请输入想要编辑的主题名:")
			action = "nano ./themes/" + themesname + "/_config.yml"
			o(action)
		if key == "2":
			action = "nano ./scaffolds/post.md"
			o(action)
		if key == "3":
			action = "nano ./scaffolds/page.md"
			o(action)
		if key == "4":
			p("目前已有的文章:")
			n()
			action = "ls ./source/_posts"
			o(action)
			n()
			choose = input("请输入要编辑的文章Title:")
			action = "nano ./source/_posts/" + choose + ".md"
			o(action)
		if key == "5":
			p("目前已有的页面:")
			n()
			action = "hexo list page"
			o(action)
			n()
			choose = input("请输入要编辑的页面Title:")
			action = "nano ./source/" + choose + "/index.md"
			o(action)

	def Preview(self):
		p("1) 本地静默启动				2) 本地非静默启动(方便查看情况)")
		p("3) 局域网静默启动(请清楚自己的IP)				4) 局域网非静默启动")
		action1 = "nohup hexo s &"
		action2 = "hexo s"
		action3 = "hexo g && nohup http-server &"
		action4 = "hexo g && http-server"
		n()
		hexos = input("请选择启动方式:")
		n()
		if hexos == "1":
			o(action1)
			p("现在可以在 http://localhost:4000 查看网站预览了")
		if hexos == "2":
			o(action2)
			p("现在可以在 http://localhost:4000 查看网站预览了")
		if hexos == "3":
			os.chdir("./public")
			o(action3)
		if hexos == "4":
			os.chdir("./public")
			o(action4)

	def Upload(self):
		o("hexo g -d")

	def Backup(self):
		choose = input("是否是第一次使用此功能(y/n):")
		n()
		if choose == "y":
			github = input("请输入将上传的文章存放的仓库地址:")
			sh = "git init\ngit add *.md .\ngit commit -m '博客文章备份'\ngit branch -M main\ngit remote add origin " + github + "\ngit push -u origin main"
			with open('./source/_posts/git.sh','w') as f:
				f.write(sh)
			action = "sh git.sh"
			os.chdir("./source/_posts/")
			o(action)
			q()
		if choose == "n":
			action = "git add *.md .\ngit commit -m '博客文章备份'\ngit push -u origin main"
			os.chdir("./source/_posts/")
			o(action)
			q()

	def Theme(self):
		gc = "git clone "
		ayer = gc + "https://github.com/Shen-Yu/hexo-theme-ayer.git ./themes/ayer"
		next = gc + "https://github.com/theme-next/hexo-theme-next ./themes/next"
		matery = gc + "https://github.com/blinkfox/hexo-theme-matery.git ./matery"
		apollo = gc + "https://github.com/pinggod/hexo-theme-apollo.git ./themes/apollo"
		flex = gc + "https://github.com/miiiku/hexo-theme-flexblock.git ./themes/flex-block"
		p("可快速安装的主流主题:")
		p("0) ayer    1) next")
		p("2) matery  3) apollo")
		p("4) flex-block")
		n()
		nz = input("请输入主题序号或其他主题仓库https地址:")
		n()
		if nz == "0":
			o(ayer)
		if nz == "1":
			o(next)
		if nz == "2":
			o(matery)
		if nz == "3":
			o(apollo)
		if nz == "4":
			o(flex)
		else:
			action = gc + nz + ".git ./themes"
			o(action)

	def PutIn(self):
		git = input("请输入备份文章仓库地址:")
		p("是否删除之前的所有文章(去重):")
		rm = ("y/n:")
		if rm == "y":
			o("rm -rf ./source/_posts")
		action = "git clone " + git + " temp"
		o(action)
		mv = "mv ./temp/*.md ./source/_posts/"
		o(mv)
		deltemp = "rm -rf temp"
		o(deltemp)

	def List(self):
		act = "hexo list post"
		p("目前已有的文章:")
		o(act)
		action = "hexo list page"
		p("目前已有的页面:")
		o(action)

	def Clean(self):
		act = "hexo clean"
		o(act)

	def Quit(self):
		q()

member = Hexo(666)
member.Desktop()
n()
num = input("请输入序号:")
n()
if num == "update":
	member.Update()
if num == "quit":
	member.Quit()
if num == "0":
	member.UpdateNode()
if num == "1":
	member.Download()
if num == "2":
	member.New()
if num == "3":
	member.Edit()
if num == "4":
	member.Preview()
if num == "5":
	member.Upload()
if num == "6":
	member.Backup()
if num == "7":
	member.Theme()
if num == "8":
	member.PutIn()
if num == "9":
	member.List()
if num == "10":
	member.Clean()
if num == "11":
	member.Quit()
else:
	re()





