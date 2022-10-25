import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 målet
# Öppna en webläsare som vi har kontroll över och gå till www.chalmers.se


browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
browser.set_window_size(1920, 1080)
browser.get("https://www.chalmers.se")
browser.find_element(By.LINK_TEXT, "Utbildning").click()
browser.find_element(By.LINK_TEXT, "Program på grundnivå").click()
browser.find_element(By.LINK_TEXT, "Elektro, Data, IT och Medicinteknik").click()
browser.find_element(By.CSS_SELECTOR, ".orange li:nth-child(5) .title").click()

time.sleep(10)