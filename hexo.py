#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import requests
import sys

def o(action):
  os.system(action)

def p(str):
  print(str)

if not os.path.exists("_config.yml"):
  p("请在一个hexo文件夹中执行此脚本！")
  sys.exit(1)

def hh():
  p("\n")
p("\nHexo辅助脚本")
p("由便当手打制作！")
p("\n0) 更新node和npm  1) 安装Hexo所需的一切")
p("2) 新建           3) 编辑")
p("4) 预览           5) 上传(到Github)")
p("6) 备份文章       7) 主题")
p("8) 导入文章       9) 退出\n")
p("脚本使用编辑器:nano 用法:\nCtrl O保存 之后提示是否以原文件名保存 Ctrl X退出(用了就清楚了)")
hh()

type = input("请输入序号:")
hh()

if type == "update":
  url = "https://raw.githubusercontent.com/wzk0/quick-hexo/main/hexo.py"
  r = requests.get(url)
  with open('hexo.py', 'w') as f:
    f.write(r.text)
  act = "chmod +x hexo.py"
  o(act)
  p("更新完毕！你现在可以通过 ./hexo.py 启动程序")

if type == "0":
  action = "npm update -g && npm install -g n && n stable"
  o(action)

if type == "1":
  action = "apt install git && apt install nodejs && apt install nano && npm install hexo-cli -g && npm install hexo-deployer-git --save"
  o(action)

if type == "2":
  p("0) 网站     1) 文章")
  p("2) 页面")
  hh()
  key = input("请输入序号:")
  hh()
  if key == "0":
    wangzhanname = input("请输入网站名[最好是简短难忘的](实际上是文件夹名):")
    action = "hexo init " + wangzhanname + " && cp hexo.py " + wangzhanname
    o(action)
    p("新建网站完成！")
  if key == "1":
    textname = input("请输入文章名[最好是英文字母](实际上是链接地址):")
    action = "hexo new " + textname
    o(action)
    p("是/否直接编辑?")
    choose = input("y/n:")
    if choose == "y":
      action = "nano ./source/_posts/" + textname + ".md"
      o(action)
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

if type == "3":
  p("0) 网站配置     1) 主题配置")
  p("2) 文章模板     3) 页面模板")
  p("4) 文章         5) 页面")
  hh()
  key = input("请输入序号:")
  hh()
  if key == "0":
    action = "nano _config.yml"
    o(action)
  if key == "1":
    p("目前已安装的主题:")
    hh()
    action = "ls ./themes"
    o(action)
    hh()
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
    hh()
    action = "ls ./source/_posts"
    o(action)
    hh()
    choose = input("请输入要编辑的文章Title:")
    action = "nano ./source/_posts/" + choose + ".md"
    o(action)
  if key == "5":
    p("目前已有的页面:")
    hh()
    action = "hexo list page"
    o(action)
    hh()
    choose = input("请输入要编辑的页面Title:")
    action = "nano ./source/" + choose + "/index.md"
    o(action)

if type == "4":
  action1 = "nohup hexo s &"
  action2 = "hexo s"
  hexos = input("是否静默启动(y/n):")
  if hexos = "y":
    o(action1)
  if hexos = "n":
    o(action2)
  p("现在可以在 http://localhost:4000 查看网站预览了")

if type == "5":
  action = "hexo g -d"
  o(action)

if type == "6":
  choose = input("是否是第一次使用此功能(y/n):")
  hh()
  if choose == "y":
    github = input("请输入要上传的Git仓库地址(格式:git@github.com:xxx/xxx.git):")
    sh = "git init\ngit add *.md .\ngit commit -m '🦄✨🌈'\ngit branch -M main\ngit remote add origin " + github + "\ngit push -u origin main"
    with open('./source/_posts/git.sh','w') as f:
      f.write(sh)
    action = "sh git.sh"
    os.chdir("./source/_posts/")
    o(action)
    sys.exit(1)
  if choose == "n":
    action = "git add *.md .\ngit commit -m '🦄✨🌈'\ngit push -u origin main"
    os.chdir("./source/_posts/")
    o(action)
    sys.exit(1)

if type == "7":
  gc = "git clone "
  ayer = gc + "https://github.com/Shen-Yu/hexo-theme-ayer.git ./themes/ayer"
  next = gc + "https://github.com/theme-next/hexo-theme-next ./themes/next"
  matery = gc + "https://github.com/blinkfox/hexo-theme-matery.git"
  apollo = gc + "https://github.com/pinggod/hexo-theme-apollo.git ./themes/apollo"
  flex = gc + "https://github.com/miiiku/hexo-theme-flexblock.git ./themes/flex-block"
  p("可快速安装的主流主题:")
  p("0) ayer    1) next")
  p("2) matery  3) apollo")
  p("4) flex-block")
  hh()
  nz = input("请输入主题序号或自定义仓库https地址:")
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

if type == "8":
  git = input("请输入git仓库地址:")
  action = "git clone " + git + " temp"
  o(action)
  mv = "mv ./temp/*.md ./source/_posts/"
  o(mv)
  deltemp = "rm -rf temp"
  o(deltemp)

if type == "9":
  sys.exit(1)

else:
  action = "python3 hexo.py"
  o(action)
