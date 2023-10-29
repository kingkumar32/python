import os
import time 


import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
edge_driver_path=os.path.join(os.getcwd(),'msedgedriver.exe')
edge_service=Service(edge_driver_path)
edge_options =Options()
edge_options.add_argument(f'user-agent={user_agent}')

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)

browser = webdriver.Edge(options=options,service=edge_service)
browser.get('https://paytm.com/movies/chennai/sree-lakshmi-cinemas-a-c-2k-dolby-atmos-c/43338?fromdate=2023-10-19')
action_chains=ActionChains(browser) 
# browser.maximize_window()
# browser.refresh()
# search_date_class='DatesMobile_cinemaDatesActive__oHBpY'
# element = browser.find_element_by_class_name('search_date_class')
# element.sendkeys(Keys.ENTER)
#open the by date
xpathbutton='NoData_noData__Eqm7K NoData_imgSizeUnset__bloRJ'
element=browser.find_element(By.CLASS_NAME,xpathbutton)
print(element)
# if element:
#     print("present")
# else:
#     print("not present")

# time.sleep(2)
#opent by time
# xpathshowbutton='//*[@id="__next"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]'
# elementshow=browser.find_element_by_xpath(xpathshowbutton)
# action_chains.move_to_element(elementshow).click().perform()


# browser.quit()
