from selenium import webdriver
from selenium.webdriver.common.by import By

# người điều khiển
driver = webdriver.Chrome()

driver.get("https://sinhvien.dau.edu.vn")

# username
element_user_name = driver.find_element(By.ID, 'UserName')
element_user_name.click()
element_user_name.send_keys("ABC001")

# password
element_pwd = driver.find_element(By.ID, 'Password')
element_pwd.click()
element_pwd.send_keys("0123456789")

# click button đăng nhập
element_btn = driver.find_element(By.CSS_SELECTOR, 'input[value="Đăng nhập"]')
element_btn.click()
print()


