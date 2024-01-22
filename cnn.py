from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://cnn.iprima.cz/redakce-zpravodajstvi-cnn-prima-news-56323')

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()

redakce_elms = driver.find_elements(By.TAG_NAME, 'tr')
reditel_elm = driver.find_elements(By.CLASS_NAME, 'atom-image-description')

redakce_full = []
reditel_full = []


for redaktor in redakce_elms:
    td_name = redaktor.find_elements(By.TAG_NAME, 'td')
    if td_name:
        name = td_name[0].text.strip()
        post = td_name[1].text.strip()
        redakce_full.append((name, post))

for reditel in reditel_elm:
    name_post = reditel.find_elements(By.TAG_NAME, 'span')
    if name_post:
        name_elm = name_post[0].text.strip().split(',')
        if len(name_elm) >= 2:
            name = name_elm[0].strip()
            post = name_elm[1].strip()
            reditel_full.append((name, post))


unique_reditel_full = []
unique_redakce_full = []

for unique_reditel in reditel_full:
    if unique_reditel not in unique_reditel_full:
        unique_reditel_full.append(unique_reditel)
        print(unique_reditel)

for unique_redakce in redakce_full:
    if unique_redakce not in unique_redakce_full:
        unique_redakce_full.append(unique_redakce)
        print(unique_redakce)

driver.quit()
