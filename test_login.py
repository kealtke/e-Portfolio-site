import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

browser = webdriver.Chrome()

def test_login_no_input():
    browser.get('http://localhost:8000/admin/login/?next=/admin/')
    u = browser.find_element_by_name('username')
    u.send_keys("")
    pw = browser.find_element_by_name('password')
    pw.send_keys("")
    pw.send_keys(Keys.RETURN)
    assert 'Log in | Django site admin' == browser.title
    
def test_login_no_username():
    browser.get('http://localhost:8000/admin/login/?next=/admin/')
    u = browser.find_element_by_name('username')
    u.send_keys("")
    pw = browser.find_element_by_name('password')
    pw.send_keys("01A58g99")
    pw.send_keys(Keys.RETURN)
    assert 'Log in | Django site admin' == browser.title

def test_login_no_password():
    browser.get('http://localhost:8000/admin/login/?next=/admin/')
    u = browser.find_element_by_name('username')
    u.send_keys("teekiat")
    pw = browser.find_element_by_name('password')
    pw.send_keys("")
    pw.send_keys(Keys.RETURN)
    assert 'Log in | Django site admin' == browser.title

def test_login_wrong_username():
    browser.get('http://localhost:8000/admin/login/?next=/admin/')
    u = browser.find_element_by_name('username')
    u.send_keys("aidjoaiwjodjw")
    pw = browser.find_element_by_name('password')
    pw.send_keys("01A58g99")
    pw.send_keys(Keys.RETURN)
    assert 'Log in | Django site admin' == browser.title

def test_login_wrong_password():
    browser.get('http://localhost:8000/admin/login/?next=/admin/')
    u = browser.find_element_by_name('username')
    u.send_keys("teekiat")
    pw = browser.find_element_by_name('password')
    pw.send_keys("WOjdjw90u2109")
    pw.send_keys(Keys.RETURN)
    assert 'Log in | Django site admin' == browser.title

def test_login_success():
    browser.get('http://localhost:8000/admin/login/?next=/admin/')
    u = browser.find_element_by_name('username')
    u.send_keys("teekiat")
    pw = browser.find_element_by_name('password')
    pw.send_keys("01A58g99")
    pw.send_keys(Keys.RETURN)
    assert 'Site administration | Django site admin' == browser.title


