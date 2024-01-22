from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.seznamzpravy.cz/clanek/redakce-seznam-33526')
time.sleep(3)
driver.execute_script("document.querySelector('.szn-cmp-dialog-container').remove()")
            
redakce = driver.find_element(By.CSS_SELECTOR, '[data-dot="ogm-article-content"]').text.strip()
print("Redakce:", redakce)

autori_name_elements = driver.find_elements(By.CSS_SELECTOR, '.mol-rich-content--for-article .e_n')
autori_post_elements = driver.find_elements(By.CSS_SELECTOR, '.mol-rich-content--for-article .e_bd')

autor_full = []

for name_elm, post_elm in zip(autori_name_elements, autori_post_elements):
    name = name_elm.text.strip()
    post = post_elm.text.strip()
    autor_full.append((name, post))

for name, post in autor_full:
    print("Name:", name)
    print("Post:", post)
    print()

driver.quit()

