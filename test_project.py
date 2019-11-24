import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

browser = webdriver.Chrome()

def test_projects():
    browser.get('http://localhost:8000/projects/')
    browser.find_element_by_xpath("//a[contains(@href,'/projects/1/')]").click()

    browser.get('http://localhost:8000/projects/')
    browser.find_element_by_xpath("//a[contains(@href,'/projects/2/')]").click()
    
    browser.get('http://localhost:8000/projects/')
    browser.find_element_by_xpath("//a[contains(@href,'/projects/3/')]").click()
