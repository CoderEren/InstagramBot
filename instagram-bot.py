from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://instagram.com")

driver.implicitly_wait(3)

accept_cookies = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
accept_cookies.click()

username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys("YOUR_USERNAME")

password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("YOUR_PASSWORD")

login_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
login_button.click()

driver.implicitly_wait(9)

save_info = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
save_info.click()

driver.implicitly_wait(9)

turn_notif = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
turn_notif.click()

driver.implicitly_wait(9)

search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search.send_keys("neilpatel")
driver.implicitly_wait(5)
target_account = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]")
target_account.click()

driver.implicitly_wait(6)

followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()

driver.implicitly_wait(2)

a_list = []
a_range = range(1,26)

for n in a_range:
    a_list.append(str(n))

a = 0

for number in a_list:
    follower = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]".format(number))
    follow_button = follower.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[3]/button".format(number))
    follow_button.click()
    driver.implicitly_wait(1)
    print("{} accounts followed".format(a))
    a = a + 1
    if a >= 25:
        break

