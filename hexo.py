from requests import get
from json import loads,dumps
from time import strftime,localtime
from os import path,system,chdir,listdir
from getpass import getuser
from sys import exit
from random import choice

user_name=str(getuser())
clone_address='https://ghproxy.com/https://github.com/'
theme_address='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/quick-hexo/main/theme.json'
update_program_address='https://ghproxy.com/https://raw.githubusercontent.com/wzk0/quick-hexo/main/hexo.py'
setting_data_file='setting_data.json'
raw_number=6
tip_list=['在修改完网站配置文件后记得时常备份🤔','一些程序相关的变量放在9~15行😎','建议开启自动备份文章功能🥳']

##美观输出列表元素, 可用tip_list变量设置一行要输出多少个列表元素.
def list_print(raw_list):
	for element in range(len(raw_list)):
		print(str(element)+'. '+str(raw_list[element]),end='  │  ') if (element+1)%raw_number!=0 else print(str(element)+'. '+str(raw_list[element])+'  │\n')

##可使用标签的print函数, 用来显示不同的颜色.
def new_print(string,theme=''):
	print('\033[1;32m%s\033[0m'%string) if theme=='success' else (print('\033[1;34m%s\033[0m'%string) if theme=='info' else (print('\033[1;31m%s\033[0m'%string) if theme=='danger' else print(string)))

##读取配置文件.
def get_from_json(json_file):
	try:
		with open(json_file,'r')as file:
			return loads(file.read())
	except:
		new_print('配置文件损坏! 已删除当前配置文件, 请重启程序重新进行配置!','danger')
		system('rm %s'%setting_data_file)

##配置(动词)文件.
def setting():
	backup_repo=input('\n请输入备份仓库地址(存放备份文章或重要文件, 最好是空白仓库. 默认使用main分支):')
	editor=input('\n请输入要使用的编辑器或完整启动路径(nano, vim...):')
	auto_upload_posts=True if input('\n是/否(y/n)在每次上传(到Github Pages)后自动上传文章以备份:')=='y' else False
	setting_data={'backup_repo':backup_repo,'auto_upload_posts':auto_upload_posts,'pack_name':user_name+'的网站数据.tar.gz','editor':editor+' '}
	new_print('\n配置完成. 欢迎%s!'%user_name,'success')
	with open(setting_data_file,'w')as file:
		file.write(dumps(setting_data,ensure_ascii=False))

##启动检测与读取, 同时随机输出一句小提示.
def check():
	system('clear')
	new_print('这可能不是一个hexo文件夹.','danger') if not path.exists('_config.yml') else new_print('这是一个hexo文件夹!','info')
	(setting() if input('\n没有检测到配置文件, 现在是/否(y/n)进行配置:')=='y' else exit()) if not path.exists(setting_data_file) else new_print('正在读取配置...','info')
	system('rm -rf .temp') if path.exists('.temp') else (system('mkdir drafts') if not path.exists('drafts') else new_print('配置读取完成!','success'))
	new_print('%s\n'%choice(tip_list),'info')
	return get_from_json(setting_data_file)

##初始化草稿(draft), 类似hexo的hexo new xxx指令.
def init_draft(post_name):
	time_now=strftime("%Y-%m-%d %H:%M:%S",localtime())
	with open('drafts/%s.md'%post_name,'r')as file:
		new_file=file.read().replace("{{ title }}",post_name).replace("{{ date }}",time_now)
	with open('drafts/%s.md'%post_name,'w')as file:
		file.write(new_file)

##创建类.
class new():
	item_list=['网站','文章','页面','草稿','草稿=>文章']
	def website():
		website_name=input('请输入网站文件夹名称:')
		system('hexo init %s && cp %s %s && cd %s'%(website_name,path.basename(__file__),website_name,website_name))
	def post(editor):
		post_name=input('请输入新建文章名称(建议为英文):')
		system('hexo new %s'%post_name)
		system(editor+'source/_posts/%s.md'%post_name) if input('是/否(y/n)现在编辑:')=='y' else new_print('编辑指令: %ssource/_posts/%s.md'%(editor,post_name),'info')
	def page(editor):
		page_name=input('请输入新建页面名称(建议为英文):')
		system('hexo new page %s'%page_name)
		system(editor+'source/%s/index.md'%page_name) if input('是/否(y/n)现在编辑:')=='y' else new_print('编辑指令: %ssource/%s/index.md'%(editor,page_name),'info')
	def draft(editor):
		draft_name=input('请输入新建草稿名称(建议为英文):')
		system('cp scaffolds/post.md drafts/%s.md'%draft_name)
		init_draft(draft_name)
		system(editor+'drafts/%s.md'%draft_name) if input('是/否(y/n)现在编辑:')=='y' else new_print('编辑指令: %sdrafts/%s.md'%(editor,draft_name),'info')
	def draft_to_post():
		draft=listdir('drafts')
		draft.sort()
		list_print(draft)
		system('mv drafts/%s source/_posts/'%draft[int(input('\n\n请输入要转为文章的草稿前的序号:'))])
		new_print('完成!','success')

##编辑类.
class edit():
	item_list=['网站配置','主题配置','文章模板','页面模板','文章','页面','草稿']
	def website_config(editor):
		system(editor+'_config.yml')
	def theme_config(editor):
		themes=[]
		[themes.append(theme) for theme in listdir('themes') if theme[0]!='.']
		themes.sort()
		list_print(themes)
		system(editor+'themes/%s/_config.yml'%themes[int(input('\n\n请输入要编辑的主题配置前的序号:'))])
	def post_scaffold(editor):
		system(editor+'scaffolds/post.md')
	def page_scaffold(editor):
		system(editor+'scaffolds/page.md')
	def post(editor):
		post=[]
		[post.append(one_post) for one_post in listdir('source/_posts') if one_post[-2:]=='md']
		post.sort()
		list_print(post)
		system(editor+'source/_posts/%s'%post[int(input('\n\n请输入要编辑的文章前的序号:'))])
	def page(editor):
		page=listdir('source')
		page.remove('_posts')
		page.sort()
		list_print(page)
		system(editor+'source/%s/index.md'%page[int(input('\n\n请输入要编辑的页面前的序号:'))])
	def draft(editor):
		draft=listdir('drafts')
		draft.sort()
		list_print(draft)
		system(editor+'drafts/%s'%draft[int(input('\n\n请输入要编辑的文章前的序号:'))])

##删除类.
class delete():
	item_list=['文章','页面','草稿','主题']
	def post():
		post=[]
		[post.append(one_post) for one_post in listdir('source/_posts') if one_post[-2:]=='md']
		post.sort()
		list_print(post)
		[system('rm source/_posts/%s'%post[int(one_post)]) for one_post in input('\n\n请输入要删除的文章前的序号(多个序号可用空格隔开):').split(' ')]
	def page():
		page=listdir('source')
		page.remove('_posts')
		page.sort()
		list_print(page)
		[system('rm -rf source/%s'%page[int(one_page)]) for one_page in input('\n\n请输入要删除的页面前的序号(多个序号可用空格隔开):').split(' ')]
	def draft():
		draft=listdir('drafts')
		draft.sort()
		list_print(draft)
		[system('rm drafts/%s'%draft[int(one_draft)]) for one_draft in input('\n\n请输入要删除的草稿前的序号(多个序号可用空格隔开):').split(' ')]
	def theme():
		themes=[]
		[themes.append(theme) for theme in listdir('themes') if theme[0]!='.']
		themes.sort()
		list_print(themes)
		[system('rm -rf themes/%s && rm *%s*.yml'%(themes[int(one_theme)],themes[int(one_theme)])) for one_theme in input('\n\n请输入要删除的主题前的序号(多个序号可用空格隔开):').split(' ')]

##预览类.
class preview():
	item_list=['本地预览','局域网预览(需安装http-server)']
	def local():
		system('hexo s')
	def lan():
		system('hexo clean && hexo g')
		chdir('public')
		system('http-server')

##数据类.
class hexo_data():
	item_list=['详细数据','数字数据']
	def ordinary():
		system('hexo list post && hexo list page')
	def simplify():
		post=[]
		[post.append(one_post) for one_post in listdir('source/_posts') if one_post[-2:]=='md']
		page=listdir('source')
		page.remove('_posts')
		themes=[]
		[themes.append(theme) for theme in listdir('themes') if theme[0]!='.']
		draft=listdir('drafts')
		new_print('当前共有文章%s篇, 草稿%s篇, 页面%s个, 下载了%s个主题.'%(len(post),len(draft),len(page),len(themes)),'info')

##上传页面到Github Pages函数.
def upload_page(auto_upload_posts,backup_repo):
	if auto_upload_posts:
		new_print('由于开启了自动备份, 正在上传文章备份...','info')
		backup.post(backup_repo)
	else:
		pass
	system('hexo g -d')

##备份类.
class backup():
	item_list=['备份文章','备份所有重要数据']
	def post(backup_repo):
		system('git clone %s .backup_repo --depth 1 && rm .backup_repo/*.md && cp source/_posts/*.md .backup_repo'%backup_repo) if not path.exists('.backup_repo') else system('rm .backup_repo/*.md && cp source/_posts/*.md .backup_repo')
		system('cp -r drafts .backup_repo')
		chdir('.backup_repo')
		system("git add * . && git commit -m '%s备份' && git push -u origin main"%strftime("%Y-%m-%d %H:%M:%S",localtime()))
		new_print('文章备份完成!','success')
	def all_data(pack_name,backup_repo):
		(system('rm %s'%pack_name) if input('检测到曾经的备份文件, 是/否(y/n)删除:')=='y' else exit()) if path.exists(pack_name) else system('mkdir .temp')
		[system('cp -r %s .temp'%fold) for fold in ['source','scaffolds','drafts','themes']]
		[system('cp %s .temp'%file) for file in ['package.json','setting_data.json','_config*.yml']]
		with open('.temp/recovery.sh','a')as sh:
			[sh.write('rm -rf ../%s\n'%rm_fold) for rm_fold in ['source','scaffolds','drafts','themes']]
			[sh.write('rm ../%s\n'%rm_file) for rm_file in ['package.json','setting_data.json','_config*.yml']]
			sh.write('mv * .. && cd .. && npm install && rm -rf %s && rm %s && rm recovery.sh'%(pack_name[:-7],pack_name))
		chdir('.temp')
		system('chmod +x recovery.sh && tar czvf %s . && mv %s ..'%(pack_name,pack_name))
		new_print('备份完成! 已将网站所有重要文件打包至%s, 可在解压后使用sh recovery.sh一键恢复网站(在已有的网站内运行会清除原网站的所有数据, 建议在新网站运行).'%pack_name,'success')

##主题类.
class themes():
	item_list=['推荐主题','自定义主题']
	def recommend():
		global theme_address
		global clone_address
		theme_list=list(loads(get(theme_address)).items())
		theme_list.sort()
		list_print([theme_name[0] for theme_name in theme_list])
		theme_id=input('\n\n请输入要下载的主题前的序号:')
		system('git clone %s%s themes/%s --depth 1'%(clone_address,theme_list[int(theme_id)][1],theme_list[int(theme_id)][0]))
	def diy_theme():
		system('git clone %s%s themes/%s --depth 1'%(clone_address,input('请输入主题仓库链接:'),input('\n请输入主题名(在themes文件夹中的名称):')))

##重新配置程序函数.
def program_setting(editor):
	system('rm %s'%setting_data_file)
	setting()

##更新程序.
def program_update():
	new_print('正在获取更新...')
	with open(path.basename(__file__),'w')as new_program:
		new_program.write(get(update_program_address))
	new_print('更新完成!','success')

def program_exit():
	new_print('Bye~ 这里有个提示: %s'%choice(tip_list),'info')
	exit()

##main函数, 整个骨架.
def main():
	user_setting=check()
	list_print(['新建','编辑','删除','预览','数据','上传到Page','备份','主题','重新配置程序','更新程序','退出'])
	action=input('\n\n请输入序号以进行操作:')
	system('clear')
	if action=='0':
		list_print(new.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		new.website() if new_action=='0' else (new.post(user_setting['editor']) if new_action=='1' else (new.page(user_setting['editor']) if new_action=='2' else (new.draft(user_setting['editor']) if new_action=='3' else (new.draft_to_post() if new_action=='4' else exit()))))
	if action=='1':
		list_print(edit.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		edit.website_config(user_setting['editor']) if new_action=='0' else (edit.theme_config(user_setting['editor']) if new_action=='1' else (edit.post_scaffold(user_setting['editor']) if new_action=='2' else (edit.page_scaffold(user_setting['editor']) if new_action=='3' else (edit.post(user_setting['editor']) if new_action=='4' else (edit.page(user_setting['editor']) if new_action=='5' else (edit.draft(user_setting['editor']) if new_action=='6' else exit()))))))
	if action=='2':
		list_print(delete.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		delete.post() if new_action=='0' else (delete.page() if new_action=='1' else (delete.draft() if new_action=='2' else (delete.theme() if new_action=='3' else exit())))
	if action=='3':
		list_print(preview.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		preview.local() if new_action=='0' else (preview.lan() if new_action=='1' else exit())
	if action=='4':
		list_print(hexo_data.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		hexo_data.ordinary() if new_action=='0' else (hexo_data.simplify() if new_action=='1' else exit())
	if action=='5':
		upload_page(user_setting['auto_upload_posts'],user_setting['backup_repo'])
	if action=='6':
		list_print(backup.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		backup.post(user_setting['backup_repo']) if new_action=='0' else (backup.all_data(user_setting['pack_name'],user_setting['backup_repo']) if new_action=='1' else exit())
	if action=='7':
		list_print(themes.item_list)
		new_action=input('\n\n请输入序号以进行操作:')
		system('clear')
		themes.recommend() if new_action=='0' else (themes.diy_theme() if new_action=='1' else exit())
	if action=='8':
		program_setting(user_setting['editor'])
	if action=='9':
		program_update()
	if action=='10':
		program_exit()
main()