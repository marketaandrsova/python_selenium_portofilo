from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://www.advojka.cz/o-nas/autori')

full_names = []

autori_name = driver.find_elements(By.CLASS_NAME, 'author-name')
autori_post = driver.find_elements(By.CLASS_NAME, 'author-role')

for name_elm, post_elm in zip(autori_name, autori_post):
    name = name_elm.text.strip()
    post = post_elm.text.strip()
    full_names.append((name, post))

for name, post in full_names:
    print("Name:", name)
    print("Post:", post)
    print()
    
driver.quit()

