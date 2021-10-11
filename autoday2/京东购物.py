from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 事件链
import time
import cv2.cv as cv

driver = webdriver.Chrome()

driver.get("http://www.jd.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()

driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]").click()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18812163137")

driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("18812163137Wxc")

driver.find_element_by_xpath("//*[@id='loginsubmit']").click()

ac = ActionChains(driver)
#获取元素
ele = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")


def FindPic(target, template):

    target_rgb = cv2.imread(target)
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread(template, 0)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)


ac.click_and_hold(ele).move_by_offset(198,0).perform()

ac.release().perform()