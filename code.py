import configparser as cfg
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

parser = cfg.ConfigParser()
parser.read('config.cfg')
username = parser.get('creds', 'username')
pwd = parser.get('creds', 'pwd')

url = "https://hello.iitk.ac.in/user/login"
driver = Chrome()
driver.get(url)

username_ele = driver.find_element(By.ID, 'edit-name')
pwd_ele = driver.find_element(By.ID, 'edit-pass')
username_ele.send_keys(username)
pwd_ele.send_keys(pwd)

driver.find_element(By.ID, 'edit-submit').click()

url = "https://hello.iitk.ac.in/eco342a22/#/home"
driver.get(url)

links = driver.find_elements(By.TAG_NAME, 'a')

dir = '/home/yashbg/Desktop/6th Sem/ECO342A/Lectures/'
starting_lec = 2
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
