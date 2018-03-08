# python-selenium
这里介绍使用selenium来获取动态的文本和实现鼠标的下拉动作
# selenium的定义
    selenium就是真实的模拟人的行为，实现通过浏览器打开页面等
# 官方文档在百度搜索
    selenium python api
# 准备条件
    首先是安装selenium
 ```python
pip install selenium
```
    然后是安装浏览器的驱动,在官方文档的Drivers下载，该例子使用的是chrome
## 例子一、获取动态文本
    这里举例获取某商品的价格，因为很多网站的某些文本都是用js来生成的，所以最好用selenium来模拟人打开网页等所有元素加载完再获取
```python
from selenium import webdriver    #引入所需包
from scrapy.selector import Selector  #引入所需包

browser =webdriver.Chrome(executable_path="E:/python36/chromedriver.exe") #选择刚刚下载的driver路径

browser.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.71.6631331eBB4wFy&id=545602688279&skuId=3458030501021&user_id=2101899623&cat_id=50025174&is_b=1&rn=e2ade042699c64e3297bc85a0695b475#")  #获取想要爬去的页面的链接

t_selector=Selector(text=browser.page_source) #使用selector工具

print(t_selector.css(".tm-promo-price .tm-price::text").extract()) #获取具体的价格

browser.quit() #获取完价格后退出浏览器
```
## 例子二、模拟鼠标向下拉加载动态内容
    这里使用开源中国博客作为例子，因为很多博客、论坛都是给出一部分内容然后需要鼠标拖到底部才会继续加载内容，所以可以使用selenium来模拟人往下拉鼠标
```python
from selenium import webdriver  #引入所需包
import time #引入时间类
browser =webdriver.Chrome(executable_path="E:/python36/chromedriver.exe") #选择刚刚下载的driver路径

browser.get("http://www.oschina.net/blog")  #模拟人打开开源中国博客

for i in range(5):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenofPage=document.body.scrollHeight;return lenofPage;") #实现模拟人下拉动作的js
    time.sleep(4) #睡眠4秒，防止被检测到

