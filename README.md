# Quick-Hexo

> 一个辅助hexo使用的脚本.

## 什么是hexo?

一个强大的静态博客框架,官方网站: https://hexo.io .

我的博客用的也是这个框架: https://wzk0.github.io .

## 使用

首先确定电脑上有`python3`,`wget`:

```
apt update && apt upgrade

apt install python3 wget -y
```

然后获取脚本:

```
wget https://raw.githubusercontent.com/wzk0/quick-hexo/main/hexo.py
```

以及安装`requests`依赖:

```
pip3 install requests
```

界面如下:

![配置过程](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202208082055694.png)

![主页面](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202208082055885.png)

## 注意

此脚本默认认为`导入文章`功能中,远端仓库与`备份文章`仓库是同一个仓库.

## 开发

使用了如下模块:

> os,sys,platform,time,requests,json.

首先进行启动检查 => 主要是`检查系统`,`检查垃圾`,`检查是否第一次运行`.

> 对于`检查是否第一次运行`的方法是 => 在第一次运行时创建`firstrun`文件,若没有`firstrun`文件,则开始进入`配置环节`.

`配置环节`对输入文字创建对应的`data.json`文件,并在检测`firstrun`通过时读取.

`配置环节`变量如下:

```
data={'repo':repo,'commit':commit,'auto_post_up':auto_post_up,'auto_pack':auto_pack,'auto_pack_up':auto_pack_up,'pack_name':pack_name,'editor':editor,'pack_manager':pack_manager,'sudo':sudo,'proxy':proxy,'git':git,'better':better}
```

```
repo: 文章备份仓库
commit: 提交过程中的commit
auto_post_up: 是否自动上传文章
auto_pack: 是否自动打包
auto_pack_up: 打包文件是否自动上传
pack_name: 打包文件名
editor: 默认编辑器
pack_manager: 默认包管理器
sudo: 是否需要root权限
proxy: 是否优先选择代理
git: 导入远端文章时是否保留git历史
better: 导入文章时的本地(l)或远端(c)文章的优先度
```

随后进行选择,每个小环节都为一个函数,此脚本整体为一个`hexo.main()`函数.

## 最后

Bye~