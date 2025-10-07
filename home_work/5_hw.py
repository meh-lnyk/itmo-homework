from selenium.webdriver.common.by import By
from selenium  import webdriver

def check_login(s: str) -> bool:
    driver = webdriver.Chrome()
    driver.get(s)

    is_all_elems_found = False

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
        is_all_elems_found = True

    return is_all_elems_found


site = "https://www.saucedemo.com/"

if check_login(site):
    print("Элементы найдены")
else:
    print("Error")
