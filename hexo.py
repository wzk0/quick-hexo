import os
import sys
import platform
import time
import requests
import json

def do(what):
	if what=='quit':
		sys.exit(1)
	if what=='restart':
		os.system('python3 hexo.py')
	if what=='clean':
		os.system('hexo clean')

def ls(ll,num,icon):
	print(icon*num+'\n')
	for l in ll:
		print(l,end='\n\n')
	print(icon*num+'\n')

def show_ls(names):
	lenth=len(names)-1
	zero=0
	while zero<=lenth:
		print(str(zero)+'. '+str(names[zero])+'\n')
		zero+=1

def get_ls(path):
	ls=os.listdir(path)
	dic={}
	for l in ls:
		dic[str(ls.index(l))]=l
	return dic

def check(system):
	os.system('clear')
	if system=='Windows':
		print('此脚本部分功能不支持'+system+'系统!\n')
	else:
		print("当前系统为: "+system+",检测通过!\n")
	if os.path.exists('source/_posts/*.tar.gz'):
		os.system('rm -rf source/_posts/*.tar.gz')
	if not os.path.exists('firstrun'):
		print('检测到这是你第一次运行此脚本,请开始进行以下配置:')
		repo=input('\n请输入远端Git仓库地址(存放备份文章或重要文件):')
		commit=input('\n请输入每次上传时的commit:')
		auto_post_up=input('\n请选择是否在上传完成后自动备份文章(y/n):')
		auto_pack=input('\n请选择是否在修改配置或模板文件后自动打包(y/n):')
		auto_pack_up=input('\n请选择是否将打包后的文件自动上传到远端Git仓库(y/n):')
		pack_name=input('\n请输入打包后的文件名:')
		editor=input('\n请输入要使用的终端文本编辑器(nano,vi...):')
		pack_manager=input('\n请输入要使用的包管理器(apt,yum...):')
		sudo=input('\n请选择是否需要sudo(y/n):')
		proxy=input('\n请选择是否优先选择代理(y/n):')
		git=input('\n请选择是否在导入远端文章时保留git历史(y/n):')
		better=input('\n请选择导入文章时的本地(l)或远端(c)文章的优先度(l/c):')
		data={'repo':repo,'commit':commit,'auto_post_up':auto_post_up,'auto_pack':auto_pack,'auto_pack_up':auto_pack_up,'pack_name':pack_name,'editor':editor,'pack_manager':pack_manager,'sudo':sudo,'proxy':proxy,'git':git,'better':better}
		with open('data.json','w')as f:
			f.write(json.dumps(data,ensure_ascii=False))
		os.system('touch firstrun && clear')
	else:
		pass

def desktop():
	check(platform.system())
	print('已经完成所有配置啦!\n')
	print('感谢使用Quick Hexo辅助脚本!\n\n功能列表如下:\n')
	ll=['0. 更新		1. 安装所需一切','2. 新建		3. 编辑','4. 预览		5. 上传到GitHub','6. 备份文章	7. 主题','8. 导入文章	9. 列出内容','10. 清理缓存	11. 打包重要文件','re. 重新配置	q. 退出','s. 设置']
	ls(ll,31,'#')

def backup(data):
	commit=data['commit']
	repo=data['repo']
	if os.path.exists('source/_posts/.git'):
		action="git add * . && git commit -m '"+commit+"' && git push -u origin main"
		os.chdir("source/_posts")
		os.system(action)
	else:
		os.chdir("source")
		os.system('git clone '+repo+' temp_posts')
		action='mv _posts/*.md temp_posts && rm -rf _posts && mv temp_posts _posts'
		os.system(action)
		backup(data)
	print('\n文章备份完成!')

def packup(data):
	pack_name=data['pack_name']
	auto_pack_up=data['auto_pack_up']
	print('该功能将对以下文件进行打包:\n')
	ll=['根目录的配置文件','特定主题的配置文件','所有文章','所有模板文件','特定主题的资产(本地图片等)','脚本配置文件','出于大小考虑,不会对文章仓库的git进行备份']
	show_ls(ll)
	print('目前已有的主题:\n')
	dic=get_ls('themes')
	show_ls(list(dic.values()))
	name=input('请输入需要备份的主题序号:')
	theme=dic[name]
	os.system('mkdir temp_dir && cp data.json hexo.py firstrun _config.yml temp_dir && mv temp_dir/_config.yml temp_dir/网站的配置文件_config.yml')
	os.system('cp themes/'+theme+'/_config.yml temp_dir/'+theme+'的主题配置文件_config.yml')
	if os.path.exists('_config.'+theme+'.yml'):
		os.system('cp _config.'+theme+'.yml temp_dir/根目录存放的'+theme+'主题配置文件_config.'+theme+'.yml')
	else:
		pass
	os.system('cp -r themes/'+theme+'/source temp_dir/'+theme+'主题的资产source')
	os.system('cp -r source temp_dir/网站的页面及文章source && rm -rf temp_dir/网站的页面及文章source/_posts/.git && cp -r scaffolds temp_dir/网站的模板scaffolds')
	os.chdir('temp_dir')
	readme='首先感谢使用此脚本!不然你也不会得到这个压缩包,更不会得到里面的这个自述文件 -- 就是你现在正在阅读的这个!\n\n现在介绍一下该怎么处理这个压缩包吧!\n\n首先应该将文件或文件夹移动到应该存放的地方,这点参照文件前面的说明即可.例如:\n\n将 根目录存放的'+theme+'主题的配置文件 这个文件放在 网站的根目录,网站的配置文件 也放在网站的根目录即可.\n\n[规律: 网站或者根目录开头的放在网站根目录,'+theme+'主题开头的放在 theme/'+theme+' 文件夹!\n例外的情况,如data.json,firstrun,hexo.py文件也放在根目录即可!]\n\n第二步,将放在相应位置的这些文件或文件夹重命名,将名称前面的中文去掉即可!\n\nBye~~'
	with open('README','w')as f:
		f.write(readme)
	os.system('tar -czvf '+pack_name+'.tar.gz *')
	os.chdir('..')
	if os.path.exists(pack_name+'.tar.gz'):
		rm=input('\n检测到本地存在备份文件,是/否(y/n)覆盖:')
		if rm=='y':
			os.system('rm -rf '+pack_name+'.tar.gz')
		else:
			do('quit')
	os.system('mv temp_dir/'+pack_name+'.tar.gz . && rm -rf temp_dir')
	if auto_pack_up=='y':
		os.system('cp '+pack_name+'.tar.gz source/_posts/')
		backup(data)
		os.system('rm -rf source/_posts/'+pack_name+'.tar.gz')
		print('\n打包并上传完成,请查看'+pack_name+'.tar.gz中的README文件!')
	else:
		print('\n打包完成,请查看'+pack_name+'.tar.gz中的README文件!')

def update(what,data):
	sudo=data['sudo']
	proxy=data['proxy']
	if what=='n':
		if sudo=='y':
			action="sudo npm update --location=global && sudo npm install --location=global n && sudo n stable"
		else:
			action="npm update --location=global && npm install --location=global n && n stable"
		os.system(action)
	if what=='s':
		l='https://raw.githubusercontent.com/wzk0/quick-hexo/main/hexo.py'
		if proxy=='y':
			url='https://ghproxy.com/'+l
		else:
			url=l
		r=requests.get(url)
		with open('hexo.py', 'w') as f:
			f.write(r.text)
	print('\n更新完成!')

def download(data):
	sudo=data['sudo']
	pack_manager=data['pack_manager']
	editor=data['editor']
	if sudo=='y':
		action="sudo "+pack_manager+" install git nodejs npm "+editor+" -y && sudo npm install http-server --location=global && sudo npm install hexo-cli --location=global && sudo npm install hexo-deployer-git --location=global"
	else:
		action=pack_managerg+" install git nodejs npm "+editor+" -y && npm install http-server --location=global npm install hexo-cli --location=global && npm install hexo-deployer-git --location=global"
	os.system(action)
	print('\n安装完成!')

def new(data):
	editor=data['editor']
	ll=['0. 网站','1. 文章','2. 页面']
	ls(ll,6,'#')
	choose=input('请输入序号:')
	os.system('clear')
	if choose=='0':
		name=input('请输入网站(文件夹)名:')
		action='hexo init '+name+' && cp hexo.py data.json firstrun '+name
		os.system(action)
		print('\n新建网站完成!若要在新网站'+name+'中进行操作,请在退出脚本后执行 cd '+name+' && python3 hexo,py')
	if choose=='1':
		name=input("请输入文章(链接地址)名:")
		action='hexo new '+name
		os.system(action)
		choose=input('\n是/否(y/n)直接编辑:')
		if choose=='y':
			action=editor+' source/_posts/'+name+'.md'
			os.system(action)
		else:
			print('\n稍后可输入 '+editor+' source/_posts/'+name+'.md 进行编辑!')
	if choose=='2':
		name=input('请输入网页(链接地址)名:')
		action="hexo new page "+name
		os.system(action)
		choose=input('\n是/否(y/n)直接编辑:')
		if choose=='y':
			action=editor+' source/'+name+'/index.md'
			os.system(action)
		else:
			print('\n稍后可输入 '+editor+' source/'+name+'/index.md 进行编辑!')

def edit(data):
	editor=data['editor']
	auto_pack=data['auto_pack']
	def edt(path):
		os.system(editor+' '+path)
	dic={'0':'_config.yml','2':'scaffolds/post.md','3':'scaffolds/page.md'}
	ll=['0. 网站配置	1. 主题配置','2. 文章模板	3. 页面模板','4. 文章		5. 页面']
	ls(ll,27,'#')
	choose=input('请输入序号:')
	os.system('clear')
	if choose in dic.keys():
		edt(dic[choose])
		if auto_pack=='y':
			print('\n检测到修改了配置或模板文件,开始进入自动打包流程.\n')
			packup(data)
		else:
			pass
	else:
		if choose=='1':
			ll=os.listdir('themes')
			show_ls(ll)
			dic=get_ls('themes')
			choose=input('请输入主题前的序号:')
			edt('themes/'+dic[choose]+'/_config.yml')
		if choose=='4':
			ll=os.listdir('source/_posts')
			show_ls(ll)
			dic=get_ls('source/_posts')
			choose=input('请输入文章前的序号')
			edt('source/_posts/'+dic[choose])
		if choose=='5':
			ll=os.listdir('source')
			show_ls(ll)
			dic=get_ls('source')
			choose=input('请输入页面前的序号')
			edt('source/'+dic[choose]+"/index.md")
		else:
			pass
	print('\n编辑完成!')

def preview(data):
	ll=['本地静默启动','本地非静默启动(方便查看情况)','局域网静默启动(请清楚自己的IP)','局域网非静默启动','杀死进程']
	show_ls(ll)
	choose=input('请输入序号:')
	os.system('clear')
	def get_act(choose):
		if choose=='0':
			return 'nohup hexo s &'
		if choose=='1':
			return 'hexo s'
		if choose=='2':
			return 'nohup http-server &'
		if choose=='3':
			return 'http-server'
		if choose=='4':
			return 'fuser -k -n tcp 8080 && fuser -k -n tcp 4000'
		else:
			pass
	if choose in '23':
		os.system('hexo g')
		os.chdir('public')
		os.system(get_act(choose))
	else:
		os.system(get_act(choose))
	print('\n完成!')

def upload(data):
	auto_post_up=data['auto_post_up']
	os.system('hexo g -d')
	time.sleep(2)
	if auto_post_up=='y':
		backup(data)
	print('\n上传完成!')

def theme(data):
	proxy=data['proxy']
	l='https://raw.githubusercontent.com/wzk0/quick-hexo/main/theme.dict'
	if proxy=='y':
		url='https://ghproxy.com/'+l
	else:
		url=l
	d=requests.get(url)
	dic=eval(d.text)
	v=[]
	for l in list(dic.values()):
		ll=l.replace('/','的')
		v.append(ll)
	show_ls(v)
	ids=input('请输入序号以安装主题:')
	def gc(nm,ids):
		if proxy=='y':
			os.system('git clone https://ghproxy.com/https://github.com/'+list(dic.values())[int(ids)]+' themes/'+nm)
		else:
			os.system('git clone https://github.com/'+list(dic.values())[int(ids)]+' themes/'+nm)
	nm=list(dic.keys())[int(ids)]
	gc(nm,ids)
	print('\n安装完成!')

def putin(data):
	better=data['better']
	repo=data['repo']
	git=data['git']
	os.chdir('source')
	os.system('git clone '+repo+' temp_repo')
	if git=='y':
		if better=='l':
			action='mv _posts/*.md temp_repo && rm -rf _posts && mv temp_repo _posts'
		if better=='c':
			action='mv temp_repo/*.md _posts && mv _posts/*.md temp_repo && rm -rf _posts && mv temp_repo _posts'
		os.system(action)
	else:
		if better=='l':
			action='mv _posts/*.md temp_repo && mv temp_repo/*.md _posts && rm -rf temp_repo'
		if better=='c':
			action='mv temp_repo/*.md _posts && rm -rf temp_repo'
		os.system(action)
	print('\n导入完成!')

def lst(data):
	print('所有文章如下:\n')
	os.system('hexo list post')
	print('\n所有页面如下:\n')
	os.system('hexo list page')
	print('\n列出完成!')

def clean(data):
	do('clean')
	print('\n清理完成!')

def re():
	sure=input('确认清除所有旧配置(y/n):')
	if sure=='y':
		os.system('rm -rf firstrun data.json')
		print('\n旧配置清理完成!请重启脚本以重写配置.')
	else:
		print('\n操作取消!')

def q():
	print('ByeBye~~')
	do('quit')

def s(data):
	editor=data['editor']
	os.system(editor+' data.json')

def main():
	desktop()
	with open('data.json','r')as f:
		dt=f.read()
	data=json.loads(dt)
	choose=input('请输入序号:')
	os.system('clear')
	if choose=='0':
		ll=['n. 更新nodejs及npm','s. 更新脚本']
		ls(ll,18,'#')
		what=input('请输入序号:')
		update(what,data)
	if choose=='1':
		download(data)
	if choose=='2':
		new(data)
	if choose=='3':
		edit(data)
	if choose=='4':
		preview(data)
	if choose=='5':
		upload(data)
	if choose=='6':
		backup(data)
	if choose=='7':
		theme(data)
	if choose=='8':
		putin(data)
	if choose=='9':
		lst(data)
	if choose=='10':
		clean(data)
	if choose=='11':
		packup(data)
	if choose=='re':
		re()
	if choose=='q':
		q()
	if choose=='s':
		s(data)

main()