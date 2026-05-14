from selenium import webdriver
from selenium.webdriver.common.by import By

# người điều khiển
driver = webdriver.Chrome()

# 1. Vào trang
driver.get("https://phatnguoi.com")

# 2. Click danh sách phương tiên
element_options =  driver.find_element(By.ID, 'loaixe')
element_options.click()

# 3. Chọn option xe máy
element_options =  driver.find_element(By.XPATH, '//*[@id="loaixe"]/option[2]')
element_options.click()

# 4. Nhập biển số
element_input =  driver.find_element(By.ID, 'bsxinput')
element_input.click()
element_input.send_keys("43A333333")

# 5. Click button tra ngay
element_btn =  driver.find_element(By.ID, 'submit-btn')
element_btn.click()
print()
