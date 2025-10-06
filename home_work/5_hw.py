from selenium.webdriver.common.by import By
from selenium  import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_elem = driver.find_element(By.ID, "user-name")
is_un = False
if username_elem is not None:
    is_un = True

password_elem = driver.find_element(By.ID, "password")
is_pass = False
if password_elem is not None:
    is_pass = True

login_button = driver.find_element(By.ID, "login-button")
is_login = False
if login_button is not None:
    is_login = True

if is_un & is_pass & is_login:
    print("Элементы найдены")
else:
    print("Error")
