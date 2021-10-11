from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.suning.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")

driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

driver.find_element_by_xpath("//*[@id='product-list']/ul/li[1]/div[1]/div[1]/div[1]/div[1]/a").click()

handles = driver.window_handles
driver.switch_to.window(handles[1])

driver.find_element_by_xpath("//*[@id='addCart']").click()

driver.implicitly_wait(1)

driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()

driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()



