# 登录并修改头像并评价

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("wzj")  #输入登录账号

driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")  # 输入密码

driver.find_element_by_xpath("//*[@id='submit']").click() # 点击登录

driver.implicitly_wait(1)

# driver.find_element_by_xpath("//*[@id='img']").click()  # 点击修改头像
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='ul_pic']/li[6]/img").click()  # 点击新头像
# time.sleep(3)

# driver.refresh() # 刷新页面

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select/option[1]").click()

driver.find_element_by_xpath("//*[@id='tea_td']/select/option[4]").click()


# 评价
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()

time.sleep(1)

# target = driver.find_element_by_id("subtn")
target = driver.find_element_by_xpath("//*[@id='textarea']")
driver.execute_script("arguments[0].scrollIntoView();", target)  #拖动到可见的元素去

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()

# driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]").send_keys(Keys.TAB)

driver.find_element_by_id("textarea").send_keys("嗯！斯高一！")
# driver.find_element_by_xpath("//*[@id='textarea]'").send_keys("嗯！还算斯高一！")
driver.find_element_by_xpath("//*[@id='subtn']").click()


# driver.quit()  # 关闭浏览器