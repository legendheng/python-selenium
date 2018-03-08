#自动往下加载信息

from selenium import webdriver
import time
browser =webdriver.Chrome(executable_path="E:/python36/chromedriver.exe")

browser.get("http://www.oschina.net/blog")

for i in range(5):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenofPage=document.body.scrollHeight;return lenofPage;")
    time.sleep(4)
