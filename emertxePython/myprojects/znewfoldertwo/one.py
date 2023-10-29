from selenium import webdriver
from selenium.webdriver import Chrome
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)

driver = webdriver.Chrome("D:\code\python\emertxePython\myprojects\znewfoldertwo\chromedriver.exe")
driver.get('https://www.amazon.in/')
driver.maximize_window()
