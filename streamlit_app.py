import streamlit as st
import time

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By

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
    driver.maximize_window()
    time.sleep(6)
    
    stext = driver.find_element(By.ID, "search")
    
    
    # stext.clear()
    stext.send_keys("https://www.planespotters.net/production-list/index")
    
    time.sleep(6)
    

    st.code(driver.page_source)
