from selenium import webdriver
import time

driver = webdriver.Chrome()

# 打开京东网址
driver.get("http://www.jd.com")

# 窗口最大化
driver.maximize_window()

# 寻找输入框
driver.find_element_by_id("key").send_keys("电脑")

# 点击搜索按钮
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()

# 等待加载
driver.implicitly_wait(3)

# 点击一项
driver.find_element_by_xpath("//*[@src='//img14.360buyimg.com/n7/jfs/t1/162243/8/22159/215958/61501dc6E28e47aeb/0ae0018bc55a3c14.jpg']").click()
# driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[3]/a").click()
time.sleep(2)

driver.quit()