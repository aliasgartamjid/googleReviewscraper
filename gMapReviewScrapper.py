from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
website='https://www.google.com/maps/place/Evercare+Hospital+Dhaka/@23.8106745,90.4301011,18.85z/data=!4m7!3m6!1s0x3755c64aaa9e9039:0x226faca86a7e028d!8m2!3d23.8102668!4d90.4313219!9m1!1b1?hl=en-BD'
driver = webdriver.Chrome()
driver.get(website)

matches = driver.find_elements_by_class_name('wiI7pd')
name = driver.find_elements_by_xpath('//span[@jstcache="1371"]')

while 5==5:
    op = input()

    matches = driver.find_elements_by_class_name('wiI7pd')

    for match in matches:
        print(match.text)






