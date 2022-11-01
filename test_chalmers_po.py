from __future__ import annotations
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

RESOLUTIONS = ((1920, 1080), (2560, 1440))


@pytest.fixture(params=RESOLUTIONS, scope="module")
def browser(request):
    x, y = request.param
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(x, y)
    yield driver
    driver.quit()


class ChalmersPage:
    driver: webdriver.Edge # Vi behöver en driver för att interagera med webbsidan, vi börjar skriva koden för en typ av driver,
    # i mitt fall Edge, vi skall senare ändra så att objektet kan hantera alla olika drivers

    def __init__(self, driver: webdriver.Edge):
        self.driver = driver

    def click_utbildning(self) -> ChalmersUtbildning:
        self.utbildning_link.click()
        return ChalmersUtbildning(self.driver)

    def click_forskning(self):
        self.driver.find_element(By.LINK_TEXT, "Forskning").click()

    def click_samverkan(self):
        self.driver.find_element(By.LINK_TEXT, "Samverkan").click()

    @property
    def utbildning_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Utbildning")


# Den här klassen skall representera huvudsidan chalmers.se med sina olika länkar och innehåll
class ChalmersMainPage(ChalmersPage):
    pass


class ChalmersUtbildning(ChalmersPage):
    def click_program_grundniva(self):
        self.driver.find_element(By.LINK_TEXT, "Program på grundnivå").click()

    @property
    def title(self) -> str:
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div[2]/h3').text

    @property
    def body(self) -> str:
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div[2]').text


def test_nav_till_program_grundniva(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    utbildning = main_page.click_utbildning()
    utbildning.click_program_grundniva()
    # assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"


def test_nav_till_utbildning(browser):
    # browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    main_page.click_utbildning()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"


def test_nav_till_forskning(browser):
    # browser = webdriver.Edge()  # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    main_page = ChalmersMainPage(browser)
    main_page.click_forskning()
    assert browser.current_url == "https://www.chalmers.se/sv/forskning/Sidor/default.aspx"


# 1 målet
# Öppna en webläsare som vi har kontroll över och gå till www.chalmers.se



# Några problem med testfunktioner skrivna så här.
# 1. Hårdkodad data i testfunktionen. Exempelvis hur vi hittar olika element. Om systemet vi testar förändras måste vi manuellt rätta varje test
# 2. Setup av webläsare och upplösning inne i testfunktionen. Vill vi testa på flera webläsare och upplösnignar får vi skapa fler testfunktioner med dubblering av kod som följd
def test_nav_it(browser):
    # browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se") # Navigera till chalmers.se
    browser.find_element(By.LINK_TEXT, "Utbildning").click() # hitta länk baserat på länktext och klicka på
    browser.find_element(By.LINK_TEXT, "Program på grundnivå").click()
    browser.find_element(By.LINK_TEXT, "Elektro, Data, IT och Medicinteknik").click()
    browser.find_element(By.CSS_SELECTOR, ".orange li:nth-child(5) .title").click()


def test_nav_data_civ(browser):
    # browser = webdriver.Edge() # Starta en webläsare och ge mig en referens till den så att jag kan styra den
    # browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se") # Navigera till chalmers.se
    browser.find_element(By.LINK_TEXT, "Utbildning").click() # hitta länk baserat på länktext och klicka på
    browser.find_element(By.LINK_TEXT, "Program på grundnivå").click()
    browser.find_element(By.LINK_TEXT, "Elektro, Data, IT och Medicinteknik").click()
    browser.find_element(By.CSS_SELECTOR, ".orange li:nth-child(1) .title").click()