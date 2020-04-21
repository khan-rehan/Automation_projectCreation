import sys
import os 
from selenium import webdriver


path = "/Users/your-Homedirectory/Downloads/Projects/"
browser = webdriver.Chrome(r"/Users/your-Homedirectory/chromedriver")
browser.get('https://github.com/login')

username = '' # Your github username
password = '' # Your github password

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username) 
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0] 
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new') 
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0] 
    python_button.send_keys(folderName)
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()
    browser.quit()

if __name__ == "__main__":
    create()