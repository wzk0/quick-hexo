import os
import sys

def hh():
  print("\n")
print("\nHexo辅助脚本")
print("由便当手打制作！")
print("\n0) 更新node和npm  1) 安装Hexo所需的一切")
print("2) 新建           3) 编辑")
print("4) 预览           5) 上传(到Github)")
print("6) 备份文章       8) 退出\n")

type = input("请输入序号:")
hh()

if type == "0":
  action = "npm update -g && npm install -g n && n stable"
  os.system(action)

if type == "1":
  action = "apt install git && apt install nodejs && apt install nano && npm install hexo-cli -g && npm install hexo-deployer-git --save"
  os.system(action)

if type == "2":
  print("0) 网站     1) 文章")
  print("2) 页面")
  hh()
  key = input("请输入序号:")
  hh()
  if key == "0":
    wangzhanname = input("请输入网站名[最好是简短难忘的](实际上是文件夹名):")
    action = "hexo init " + wangzhanname + " && cp hexo.py " + wangzhanname
    os.system(action)
    print("新建网站完成！")
  if key == "1":
    textname = input("请输入文章名[最好是英文字母](实际上是链接地址):")
    action = "hexo new " + textname
    os.system(action)
    print("是/否直接编辑?")
    choose = input("y/n:")
    if choose == "y":
      action = "nano ./source/_posts/" + textname + ".md"
      os.system(action)
  if key == "2":
    pagename = input("请输入网页名[最好是英文字母](实际上是链接地址)")
    action = "hexo new page " + pagename
    os.system(action)
    print("是/否直接编辑?")
    choose = input("y/n:")
    if choose == "y":
      action = "nano ./source/" + pagename + "/index.md"
      os.system(action)
    else:
      action = "python hexo.py"
      os.system(action)

if type == "3":
  print("0) 网站配置     1) 主题配置")
  print("2) 文章模板     3) 页面模板")
  print("4) 文章         5) 页面")
  hh()
  key = input("请输入序号:")
  hh()
  if key == "0":
    action = "nano _config.yml"
    os.system(action)
  if key == "1":
    print("目前已安装的主题:")
    hh()
    action = "ls ./themes"
    os.system(action)
    hh()
    themesname = input("请输入想要编辑的主题名:")
    action = "nano ./themes/" + themesname + "/_config.yml"
    os.system(action)
  if key == "2":
    action = "nano ./scaffolds/post.md"
    os.system(action)
  if key == "3":
    action = "nano ./scaffolds/page.md"
    os.system(action)
  if key == "4":
    print("目前已有的文章:")
    hh()
    action = "ls ./source/_posts"
    os.system(action)
    hh()
    choose = input("请输入要编辑的文章Title:")
    action = "nano ./source/_posts/" + choose + ".md"
    os.system(action)
  if key == "5":
    print("目前已有的页面:")
    hh()
    action = "hexo list page"
    os.system(action)
    hh()
    choose = input("请输入要编辑的页面Title:")
    action = "nano ./source/" + choose + "/index.md"
    os.system(action)

if type == "4":
  action = "nohup hexo s &"
  os.system(action)
  print("现在可以在 http://localhost:4000 查看网站预览")

if type == "5":
  action = "hexo g -d"
  os.system(action)

if type == "6":
  choose = input("是否是第一次使用此功能(y/n):")
  hh()
  if choose == "y":
    github = input("请输入要上传的Git仓库地址(格式:git@github.com:xxx/xxx.git):")
    sh = "git init\ngit add *.md .\ngit commit -m '博客文章提交'\ngit branch -M main\ngit remote add origin " + github + "\ngit push -u origin main"
    with open('./source/_posts/git.sh','w') as f:
      f.write(sh)
    action = "sh git.sh"
    os.chdir("./source/_posts/")
    os.system(action)
    sys.exit(1)
  if choose == "n":
    action = "git add *.md .\ngit commit -m '博客文章提交'\ngit push -u origin main"
    os.chdir("./source/_posts/")
    os.system(action)
    sys.exit(1)

if type == "8":
  sys.exit(1)

else:
  action = "python hexo.py"
  os.system(action)