from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://www.aktualne.cz/autori/')

    autori_name = page.query_selector_all('.imprint__author__name')
    autori_post = page.query_selector_all('.imprint__author__position')
    
    autor_full = []
   
    for name_elm, post_elm in zip(autori_name, autori_post):
        name = name_elm.inner_text().strip()
        post = post_elm.inner_text().strip()
        autor_full.append((name, post))
   
    for name, post in autor_full:
        print("Name:", name)
        print("Post:", post)
        print()
   
    browser.close()
