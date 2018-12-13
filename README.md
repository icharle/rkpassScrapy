# 基于Python3、Scrapy爬取软考在线历年题库

## 环境依赖

* Python3
* Scrapy库
* re库
* MySQL数据库

## 安装使用

```bash

# 下载源代码
$ git clone https://github.com/icharle/rkpassScrapy.git

# 配置settings.py中数据库信息(导入数据库文件wx_rkpass.sql)
  
  # MYSQL INFO
  MYSQL_HOST = '127.0.0.1'
  MYSQL_PORT = 3306
  MYSQL_DATABASE = 'wx_rkpass'
  MYSQL_USERNAME = 'root'
  MYSQL_PASSWORD = 'root' 
  
# 配置settings.py中图片保存路径
  
  # 图片存储
  IMAGES_STORE = './images'

# 执行爬虫(爬取科目见下面文件介绍)
$ 修改settings.py中pipelines (删除爬取科目前面的#号)
$ scrapy crawl rkpassSpider  # (可以更换其他科目)

```


## 文件介绍

```bash
# 软件设计师(上午题)
rkpassSpider.py

# 网络工程师(上午题)
wlMorningSpider.py

# 信息系统监理师(上午题)
xxMorningSpider.py

# 数据库系统工程师(上午题)
sjkMorningSpider.py

# 软件评测师(上午题)
rjpcsMorningSpider.py

# 嵌入式系统设计师(上午题)
qrsMorningSpider.py

# 电子商务设计师(上午题)
dzswMorningSpider.py

# 多媒体应用设计师(上午题)
mediaMorningSpider.py

# 信息系统管理工程师(上午题)
xxxtMorningSpider.py

# 信息安全工程师(上午题)
xxaqMorningSpider.py

# 系统集成项目管理工程师(上午题)
xtjcMorningSpider.py

# 系统规划与管理师(上午题)
xtghMorningSpider.py

# 网络规划设计师(上午题)
wlghMorningSpider.py

# 系统架构设计师(上午题)
xtjgMorningSpider.py

# 系统分析师(上午题)
xtfxMorningSpider.py

# 信息系统项目管理师(上午题)
xxxtxmMorningSpider.py

```