import configparser as cfg
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

coursename = 'cs253a'
starting_lec = 2
dir = f'/home/yashbg/Desktop/6th Sem/{coursename.upper()}/Lectures/'

parser = cfg.ConfigParser()
parser.read('config.cfg')
username = parser.get('creds', 'username')
pwd = parser.get('creds', 'pwd')

url = 'https://hello.iitk.ac.in/user/login'
driver = Chrome()
driver.get(url)

username_ele = driver.find_element(By.ID, 'edit-name')
pwd_ele = driver.find_element(By.ID, 'edit-pass')
username_ele.send_keys(username)
pwd_ele.send_keys(pwd)

driver.find_element(By.ID, 'edit-submit').click()

url = f"https://hello.iitk.ac.in/{coursename + '22'}/#/home"
driver.get(url)

links = driver.find_elements(By.TAG_NAME, 'a')

i = 1
for link in links:
    url = link.get_attribute('href')
    if url and '.pdf' in url:
        if i < starting_lec:
            i += 1
            continue
        print('Downloading Lecture', i)
        r = requests.get(url.split('?')[0])
        with open(dir + f'Lecture {i}.pdf', 'wb') as f:
            f.write(r.content)
        i += 1

driver.close()
print('All files downloaded')
