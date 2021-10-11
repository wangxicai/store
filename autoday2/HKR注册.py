#  注册账号

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("wzj")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("王昭君")

driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123456")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123456")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()

driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("18")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]/option[2]").click()

driver.find_element_by_xpath("//*[@id='classname']/option[3]").click()

# driver.switch_to.frame("//*[@id='msform']/fieldset[2]")  # 跳转页面
time.sleep(2)
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()

driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("1903654469@qq.com")

driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("18812163137")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("北京职业科技学院")

driver.find_element_by_xpath("//*[@id='btn_reg']").click()  # 点击注册

time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[3]/a/span/span").click()

driver.quit()
