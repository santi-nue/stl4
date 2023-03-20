import streamlit as st
import time

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from parsel import Selector
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC    
    
    

    @st.experimental_singleton
    def get_driver():
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = get_driver()
    driver.get("https://www.startpage.com")
    
    
    # Maximize the window and let code stall 
    # for 10s to properly maximise the window.
    # driver.maximize_window()
    # time.sleep(6)
    
    
    # wait for page to load
    element = WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role=contentinfo]'))
    )
    
    
    
    search_box = driver.find_element_by_css_selector('input[aria-label="search"]') 
    search_box.send_keys(
        'https://www.planespotters.net/production-list/index'
    )
    
    # either press the enter key
    search_box.send_keys(Keys.ENTER)
    # or click search button
    # search_button = driver.find_element_by_css_selector('button[icon="NavSearch"]')
    # search_button.click()   
    
    time.sleep(6)

    st.code(driver.page_source)
