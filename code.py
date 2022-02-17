import configparser as cfg
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

driver.close()

# r = requests.get(url)

# print(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')

# links = soup.find_all('a')

# # for link in links:
# #     print(link)
