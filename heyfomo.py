from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://heyfomo.cz/autori')

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()

redakce_full = []

autori = driver.find_elements(By.CLASS_NAME, 'AuthorBadge_wrapper__vKygs')

for autor in autori:
    name_post = autor.get_attribute('href')
    name_post_replace = name_post.replace('https://heyfomo.cz/autor/', '').replace('-', ' ').strip()
    name_upper = name_post_replace.title()
    print(f"Name: {name_upper} - Post: Autor")

driver.quit()




