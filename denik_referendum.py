from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://denikreferendum.cz/stranka/redakce')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'drbutton.svelte-1w4oywx.invert.whiteBorder'))).click()

li_elements = driver.find_elements(By.XPATH, '//ul/li[em]')

for li_element in li_elements:
    em_text = li_element.find_element(By.TAG_NAME, 'em').text.strip()
    li_text = li_element.text.replace(em_text, '').strip()
    print(f"{em_text} {li_text}")

driver.quit()

