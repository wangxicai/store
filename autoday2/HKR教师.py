from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()

time.sleep(2)

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()

time.sleep(1)

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")

time.sleep(1)

driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")

time.sleep(1)

driver.find_element_by_xpath("//*[@id='submit']").click()  # 登录

time.sleep(2)
'''
driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()  # 教师管理

time.sleep(2)

driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click() # 重置密码

time.sleep(2)

driver.switch_to.alert.accept()  #点击弹窗确定

time.sleep(2)

driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("贾生")  #查询教师

time.sleep(2)

driver.find_element_by_xpath("//*[@id='search_user']/span/span[1]").click()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()  # 学生管理

time.sleep(2)

driver.find_element_by_xpath("//*[@id='datagrid-row-r2-2-0']/td[11]/div/a").click() # 设置学生状态

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[9]/div[3]/a").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("张伟")  # 输入学生姓名

time.sleep(1)

driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click() # 点击查询

time.sleep(2)

driver.find_element_by_xpath("//*[@id='_easyui_tree_13']/span[4]/a").click() #课程管理

time.sleep(2)

driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span").click() # 点击添加课程

time.sleep(2)

driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("英语")

time.sleep(2)

driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("English")

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[1]/span").click()  # 点击确定

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[12]/div[3]/a").click() # 确定添加成功

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[2]/span").click() #点击取消

time.sleep(2)
'''
driver.find_element_by_xpath("//*[@id='_easyui_tree_15']/span[4]/a").click()  # 今日评价

time.sleep(2)

driver.find_element_by_xpath("//*[@id='eva']/div/div/div[1]/table/tbody/tr/td[4]").click() # 导出当前评价

time.sleep(2)

driver.find_element_by_xpath("//*[@id='_easyui_tree_16']").click() # 评价报表

time.sleep(2)

# driver.find_element_by_xpath("//*[@id='highcharts-0']/svg/g[1]/g[1]/path[4]").click()  # 点击满意

# time.sleep(2)

driver.find_element_by_xpath("//*[@id='_easyui_tree_18']").click()  #历史操作日志

time.sleep(2)

driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click()  # 导出当前日志

time.sleep(2)

driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[10]/a/span").click()  # 下一页

time.sleep(2)

driver.find_element_by_xpath("//*[@id='J-history']").click() # 输入时间

time.sleep(2)

driver.find_element_by_xpath("//*[@id='laydate_ok']").click()  # 确定时间

time.sleep(5)

driver.refresh()  # 刷新页面


