from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get('https://www.vlmedia.cz/kontakty/regiony/nymbursky_denik.html')

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()

sef_full = []
editor_full = []

reditel = driver.find_elements(By.CLASS_NAME, 'reditel')
editor_elm = driver.find_elements(By.CLASS_NAME, 'item')

for sefredaktor in reditel:
    reditel_post = sefredaktor.find_element(By.TAG_NAME, 'h3').text.strip()
    reditel_name = sefredaktor.find_element(By.TAG_NAME, 'div').text.strip()
    sef_full.append((reditel_name, reditel_post))

for editor in editor_elm:
    editor_post = editor.find_element(By.TAG_NAME,'h4').text.strip()
    if "Šéfeditor" == editor_post:
        editor_name = editor.find_element(By.CLASS_NAME, 'name').text.strip()        
        editor_full.append((editor_name,editor_post))     
        break

for reditel_name, reditel_post in sef_full:
    print("Name:", reditel_name)
    print("Post:", reditel_post)
    print()

for editor_name, editor_post in editor_full:
    print("Name:", editor_name)
    print("Post:", editor_post)
    print()

driver.quit()

