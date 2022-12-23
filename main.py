from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

website = 'https://www.google.com/maps/place/Evercare+Hospital+Dhaka/@23.8096141,90.4309607,16.85z/data=!4m7!3m6!1s0x3755c64aaa9e9039:0x226faca86a7e028d!8m2!3d23.8102668!4d90.4313219!9m1!1b1?hl=en-BD'
driver = webdriver.Chrome()
driver.get(website)

matches = driver.find_elements_by_class_name('wiI7pd')
name = driver.find_elements_by_xpath('//span[@jstcache="1371"]')

while 5==5:
    op = input()
    # name = driver.find_elements_by_xpath("//span[@jstcache='1371']")
    # matches = driver.find_elements_by_class_name('wiI7pd')
    matches = driver.find_elements_by_class_name('d4r55')
    # matches = driver.find_elements_by_class_name('jJc9Ad')
    for match in matches:
        print(match.text)




    # print(match.get_attribute('innerHTML').splitlines()[0])
    # # print(match.find_elements_by_class_name('badge-over45')[0].text)
    # jaiccha = match.find_elements_by_css_selector('*')
    # for jekono in jaiccha:
    #     print(jekono.text)
    # # print(match.find_elements_by_class_name('mb-1')[0].)

#driver.quit()

