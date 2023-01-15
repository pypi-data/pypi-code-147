# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_setu_customization']

package_data = \
{'': ['*'], 'nonebot_plugin_setu_customization': ['font/*', 'html/*']}

install_requires = \
['Jinja2>=3.0.0,<4.0.0',
 'Pillow>=9.0.0,<10.0.0',
 'apscheduler>=3.7.0,<4.0.0',
 'beautifulsoup4>=4.0.0,<5.0.0',
 'httpx-socks>=0.7.0,<0.8.0',
 'httpx>=0.22.0,<0.23.0',
 'nonebot-adapter-onebot>=2.0.0,<3.0.0',
 'nonebot2>=2.0.0rc1,<3.0.0',
 'starlette>=0.19.0,<0.20.0',
 'ujson>=5.0.0,<6.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-setu-customization',
    'version': '1.4.6',
    'description': 'Nonebot2 可动态管理API并带网页浏览的setu插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/store">\n  <img src="https://user-images.githubusercontent.com/44545625/209862575-acdc9feb-3c76-471d-ad89-cc78927e5875.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n</p>\n\n<div align="center">\n\n# nonebot_plugin_setu_customization\n\n_✨ Nonebot2 可动态管理API并带网页浏览的setu插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://opensource.org/licenses/MIT">\n    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license">\n  </a>\n  <a href="https://v2.nonebot.dev/">\n    <img src="https://img.shields.io/static/v1?label=nonebot&message=v2rc1%2B&color=green" alt="nonebot2">\n  </a>\n  <img src="https://img.shields.io/static/v1?label=python+&message=3.9%2B&color=blue" alt="python">\n</p>\n\n## 简介\n可以动态增删网络上的图片API接口，也可以载入本地图库链接对外提供图片API接口，支持接口分类管理，不再受限于单个API出图，如果服务器有公网IP还可以在网页浏览图片。  \n\n<img width="300" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/soutu.jpg"/><img width="300" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/tutu_web.jpg"/>  <img width="300" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/tutu_test.jpg"/>\n\n\n## 安装\n\n使用nb-cli安装\n```bash\n# 如果没找到这个插件，使用nb plugin list 刷新缓存\nnb plugin install nonebot_plugin_setu_customization\n```\n\n或者  \n直接把插件clone下来，把nonebot_plugin_setu_customization文件夹放进去plugins目录\n\n## 配置\n在bot对应的.env文件修改\n\n```bash\n# 必填项\n# api超时，这个时间建议设置一分钟以上，否则发图多的时候容易超时报错\napi_timeout=60\n# 机器人的QQ号（由于开发者多gocq连接，所以有这个设置）\ntutu_bot_qqnum = 114514\n# 管理员的QQ号（别问我为什么要另外写）\ntutu_admin_qqnum = 114514\n\n# 非必填项\n# 图片下载模式，true则nonebot下载，false则协议端下载\ntutu_img_local_download = true\n# 图图命令CD时间（秒）\ntutu_cooldown = 3\n# 搜图结果链接有效时间（分钟）\nweb_view_time = 10\n# R18类别的名称\ntutu_r18_name = R18\n# 本地图片库的路径\ntutu_local_api_path = data/tutu_local_img_lib/\n# 本地库二次元文件名称\ntutu_self_anime_lib =  self_anime\n# 本地库三次元文件名称\ntutu_self_cosplay_lib = self_cosplay\n# 插件数据文件名\ntutu_data_filename = tutu_data.json\n# 自定义字体文件路径（要填真实路径，这里只是举个例子）\ntutu_font_path = __file__/font/msyh.ttf\n# 网页访问地址，就是nonebot的监听地址和端口号，如 http://hahaha.com:80\ntutu_site_url = http://127.0.0.1:8080\n# pixiv图片反代地址，自己可以看看哪个快用哪个 https://i.pixiv.re/ 、 https://i.pixiv.cat/ 、 https://i.loli.best/ 、 https://c.jitsu.top/\ntutu_pixiv_proxy = https://i.pixiv.re/\n# http代理地址，如 http://127.0.0.1:1234\ntutu_http_proxy = None\n# socks5代理地址，如 socks5://127.0.0.1:1234\ntutu_socks5_proxy = None\n# 使用网页访问时，新浪图片反代地址，不用网页浏览可不填，如 http://img.example.top:514\ntutu_sina_img_proxy = https://i0.wp.com/tvax1.sinaimg.cn/\n# 使用网页访问时，微信图片反代地址，不用网页浏览可不填，如 http://img.example.top:114\ntutu_wx_img_proxy = None\n# 使用网页访问时，B站图片反代地址，不用网页浏览可不填，如 http://img.example.top:514\ntutu_bili_img_proxy = None\n# 爬取文章图片时，图片的宽或高小于多少忽略爬取\ntutu_crawler_min_width =  500\ntutu_crawler_min_height =  500\n# 自动爬取功能，文章url文件放置路径\ntutu_crawler_file_path = tutu_crawler/\n# 自动爬取功能，检测文章标题，含有其中关键字则忽略爬取\ntutu_crawler_keyword = ["删", "薪", "敏感", "暂停", "停更", "图包"]\n```\n\n## 目录\ndata/tutu_data.json 存储群白名单信息，api接口信息，合并发送开关  \ndata/tutu_local_img_lib/ 存储用户自己上传的图片url文件，如下图  \n<img width="600" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/local_img_lib.jpg"/>\n\n如果要自己爬图入库的看readme的《文章图片爬取》  \ntutu_crawler/ 自动爬取文章图片用的，里面放待爬取的文章url文件，还是看readme的《文章图片爬取》  \n\n## 命令  \n| 指令 | 说明 |\n|:-----:|:----:|\n| 图图 | 机器人出图（好友私聊，群聊要添加白名单） |\n| 图图帮助 | 查看图图命令的更多使用姿势 |\n| 搜图 | 查看搜图命令使用姿势（好友私聊，群聊要添加白名单） |\n| （下面都是管理员命令） | （发送命令有使用格式） |\n| 图图插件群管理 | 增删群白名单 |\n| 图图插件接口测试 | 测试接口连接情况和返回的数据 |\n| 图片测试 | 测试某张图能否正常发出来 |\n| 文章爬取 | 爬取微信文章或B站专栏的图片 |\n| 爬取合并 | 是否将爬取结果合并发送，默认合并 |\n| 图片序号 | 每张发出来的图片都有一个序号，可查看之前发送的图片url |\n| 图片删除 | 删除本地库的某张图片 |\n| 开爬 | 上传指定格式的文件让nb爬，详情看readme的《文章图片爬取》 |\n\n## 网页搜图（需要公网）\nhttp://127.0.0.1:8080/soutu （具体域名和端口看你nb绑定的地址）  \n\n## 自定义图片url关键字替换\n在data_handle.py文件里面的 url_diy_replace 函数，如果有其他更好的反代地址或其他需求可以自行调整\n<img width="600" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/url_diy_replace.jpg"/>\n\n## 使用示例、导入api和图片库\n**二次元图片api**  \nhttp://api.tangdouz.com/sjdmbz.php  \nhttps://api.dujin.org/pic/yuanshen/  \nhttps://api.mtyqx.cn/tapi/random.php  \nhttps://www.dmoe.cc/random.php  \nhttps://setu.yuban10703.xyz/setu  \nhttps://api.ixiaowai.cn/api/api.php  \nhttps://tuapi.eees.cc/api.php?category=dongman&type=302  \nhttps://api.yimian.xyz/img/  \nhttp://api.iw233.cn/api.php?sort=random  \nhttps://image.anosu.top/pixiv/direct  \nhttps://api.lolicon.app/setu/v2  \nhttps://moe.anosu.top/img/?sort=pixiv  \nhttps://moe.anosu.top/img/?sort=setu  \n\n**R18图片api**  \nhttps://setu.yuban10703.xyz/setu?r18=1  \nhttps://image.anosu.top/pixiv/direct?r18=1  \nhttps://api.lolicon.app/setu/v2?r18=1  \nhttps://moe.anosu.top/img/?sort=r18  \n\n**三次元图片api**  \n没收集到好的，但是我爬了很多，在仓库的tutu_local_img_lib文件夹，下载放进去data/tutu_local_img_lib/里面，没事来看看有没有更新，里面也有二次元的\n\n**本地图片库**  \n即data/tutu_local_img_lib/中的图片，放入图片url文件后，使用命令“图图插件接口管理 刷新本地”进行导入  \n访问接口url如果没有在.env配置tutu_site_url，就是nonebot的地址和端口号，如绑定的host=127.0.0.1，port=8080，就是http://127.0.0.1:8080/img_api?fw=1&fn=<filename\\>\n| 参数 | 说明 |\n|:-----:|:----:|\n| fw | 是否重定向，0返回网页，1重定向到图片url |\n| fn | 本地图片库文件名 |\n| mode | 图片类型，没有fn参数时有效 |\n| c | 返回的图片数量，没有fw参数时有效 |\n\n```bash\n# 添加一个接口到二次元类型接口\n图图插件接口管理 二次元 + https://api.lolicon.app/setu/v2\n# 支持批量添加接口\n图图插件接口管理 二次元 + \nhttps://api.lolicon.app/setu/v2  \nhttp://api.tangdouz.com/sjdmbz.php  \nhttps://api.dujin.org/pic/yuanshen/  \n# 添加一个本地图片库接口到三次元类型接口\n图图插件接口管理 三次元 + 本地图库self_cosplay\n# 爬取一篇微信文章的图片到本地图片库self_anime\nhttps://mp.weixin.qq.com/s/IHeYqZTu8xYLv7nDkRwxUQ self_anime\n# 该命令等效于上面的命令 默认2指self_anime，3指self_cosplay\nhttps://mp.weixin.qq.com/s/IHeYqZTu8xYLv7nDkRwxUQ 2\n```\n\n## 文章图片爬取 \n下载mitmproxy_script文件夹中的两个脚本 \n```bash\n# 安装mitmproxy\npip install mitmproxy\n# 运行papa.py，8080的监听端口，可以自己改\npython papa.py -p8080\n# 手机或电脑设置好代理后，用浏览器访问以下网站，如果看到证书选择那就是代理对了，然后看说明安装证书\nmitm.it\n# 然后根据下面的方法爬取，结果输出在result文件夹中\n```\n\n**爬取微信公众号文章url 方法一**  \nPS：建议iOS微信爬取，装证书简单  \n微信连上代理后，大部分微信公众号的对话框有个查看历史文章（有的没有），点进去后浏览，一直往下刷到底就行，如果没有历史文章接口看方法二  \n<img width="600" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/weixin1.jpg"/>\n\n**爬取微信公众号文章url 方法二**  \nPS：容易被限制，如果翻页不回显数据就是被限制了，被限制就等几个小时再来（具体时间自己摸索），否则限制时间会大幅度延长\n注册一个微信公众平台账号  \nhttps://mp.weixin.qq.com/  \n依次点草稿箱、新的创作、写新图文，会有个新页面，在最上面有个超链接，点选择公众号，搜索公众号，然后选择就可以看到历史文章了，一页页往下翻，一次翻二三十页就好，不然容易被限制  \n<img width="600" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/weixin2.jpg"/>\n\n**爬取B站专栏图片**  \n用网页打开某个UP的账号空间，点TA的专栏，就会打开 https://space.bilibili.com/XXXXXXX/article  \n<img width="600" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_setu_customization/readme_img/bili.jpg"/>  \n然后就会自动翻页爬取所有文章url了，可以在结果文件夹里看到进度，爬取完会有个DONE文件\n\n**提取文章url**  \n爬取到新数据会生成“new_data_XXX”文件在结果文件夹中，里面的格式是“标题 *** 文章url”，可以通过标题进行筛选，不要的文章整行剪切丢到“history_data_XXX”  \n“history_data_XXX”是历史数据，每次运行爬取脚本会读取历史数据，爬过的就不会再爬\n最后就是筛选好的“new_data_XXX”文件\n```bash\n# 运行split_url.py\npython 运行split_url.py\n```\nsplit_url.py会遍历result里面的文件，把里面命名含有“new_data_”的文件里的url提取出来输出到“wait_for_upload”文件夹  \n在nonebot根目录的“tutu_crawler”里新建一个文件夹，文件夹名字是爬取的图片加入的本地图片库，如“self_anime”，也可以直接新建一个名字“2”的文件夹，默认2指self_anime，3指self_cosplay  \n把wait_for_upload里面的文件根据类型上传到 tutu_crawler/<本地图片库>/里面  \n然后给机器人私聊发送“开爬”就会自动爬取\n\n## 更新日志\n### 2023/1/15 \\[v1.4.6]\n\n* 依赖错误修复\n\n### 2023/1/14 \\[v1.4.5]\n\n* 依赖错误修复，优化逻辑\n\n### 2023/1/9 \\[v1.4.3]\n\n* 页面细节优化\n\n### 2023/1/8 \\[v1.4.2]\n\n* 增加P站搜图功能（需要公网服务器网页访问结果），优化图片下载状态判断\n* P站搜图功能基础上增加网页预览 http://127.0.0.1:8080/soutu （具体域名和端口看你nb绑定的地址）\n\n### 2023/1/4 \\[v1.3.1]\n\n* 增加本地下图和远端下图配置，优化api请求逻辑\n\n### 2023/1/4 \\[v1.2.2]\n\n* 出图改为nb下载好再发送，优化大量细节，修bug\n\n### 2023/1/3 \\[v1.1.1]\n\n* 优化接口管理功能\n\n### 2023/1/3 \\[v1.1.0]\n\n* 增加批量导入api\n\n### 2023/1/3 \\[v1.0.0]\n\n* 发布插件',
    'author': 'nikissXI',
    'author_email': '1299577815@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikissXI/nonebot_plugins/tree/main/nonebot_plugin_setu_customization',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
