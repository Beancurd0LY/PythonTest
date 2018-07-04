#!/usrc/bin/python
# -*- coding: utf-8 -*-
'''
@author: admin
'''
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 测试平台
# desired_caps['fastReset'] = 'false'
desired_caps['platformVersion'] = '7.1.1' # 平台版本
desired_caps['deviceName'] = 'meizu_MX6'  # 设备名称，多设备时需区分
desired_caps['appPackage'] = 'com.tencent.mm'  # app package名
desired_caps['appActivity'] = '.ui.LauncherUI'  # app默认Activity
# desired_caps['fullReset'] = 'false'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['noReset'] = 'True'
desired_caps['recreateChromeDriverSessions'] = 'True'
desired_caps['chromeOptions'] = {
    'androidProcess': 'com.tencent.mm:tools '  # 会影响获取页面
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动Remote RPC
sleep(20)
driver.find_element_by_xpath("//*[@text='发现']").click()
# driver.swipe()
# driver.swipe(300,1000,300,500)
sleep(5)
driver.find_element_by_xpath("//*[@text='小程序']").click()
sleep(5)
# driver.find_element_by_xpath("//*[@text='小红书']").click()
sleep(5)
webview = driver.contexts
print webview
driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")
# driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')  # native切换webview
sleep(5)

all_handles = driver.window_handles
print len(all_handles)
for handle in all_handles:
    try:
        driver.switch_to_window(handle)
        print driver.page_source
        driver.find_element_by_css_selector("[data-wpyhandletapcategory-a='4']")  # 定位handle
        print '定位成功'
        print all_handles
        print handle
        break
    except Exception as e:
        print e
driver.find_element_by_css_selector("[data-wpyhandletapcategory-a='4']").click()
sleep(10)
# driver.find_element_by_css_selector("[data-com-index='0']").click()
sleep(5)

driver.switch_to.context('NATIVE_APP')  # webview切换native
driver.find_element_by_xpath("//*[@text='我的']").click()
driver.quit()
