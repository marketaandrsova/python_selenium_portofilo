from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.respekt.cz/redakce')

    autori = page.query_selector_all('.Author_content__BkXIr')
    autor_full = []

    for autor in autori:
        h2_element = autor.query_selector('.Author_name__lhuP0')
        p_element = autor.query_selector('.Author_position__Kme_I')
        h2_text = h2_element.text_content()
        p_text = p_element.text_content()

        autor_full.append((h2_text, p_text))

    for h2_text, p_text in autor_full:
        print("Name:", h2_text)
        print("Position:", p_text)
        print()

    browser.close()