import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

browser = webdriver.Chrome()

def test_blog_detail():
    browser.get('http://localhost:8000/blog/')
    browser.find_element_by_xpath("//a[contains(@href,'/blog/4/')]").click()
    
    browser.get('http://localhost:8000/blog/')
    browser.find_element_by_xpath("//a[contains(@href,'/blog/3/')]").click()


def test_blog_category_Django():
    browser.get('http://localhost:8000/blog/')
    browser.find_element_by_xpath("//a[contains(@href,'/blog/DJango')]").click()
    
    #assert 'localhost:8000/blog/DJango/' == browser.title
 

def test_blog_comment():
    browser.get('http://localhost:8000/blog/')
    browser.find_element_by_xpath("//a[contains(@href,'/blog/3/')]").click()
    
    au = browser.find_element_by_name('author')
    au.send_keys("tk")
    bdy = browser.find_element_by_name('body')
    bdy.send_keys("test comment")
    browser.find_element_by_xpath('//button[contains(text(), "Submit")]').click()
    
    #assert 'localhost:8000/blog/3/' == browser.title