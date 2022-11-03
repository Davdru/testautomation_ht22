from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.common.by import By


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


class ChalmersMainPage(ChalmersPage):
    pass


class ChalmersUtbildning(ChalmersPage):
    def click_program_grundniva(self) -> ChalmersProgramGrundniva:
        self.driver.find_element(By.LINK_TEXT, "Program på grundnivå").click()
        return ChalmersProgramGrundniva(self.driver)

    @property
    def title(self) -> str:
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div[2]/h3').text

    @property
    def body(self) -> str:
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div[2]').text


class ChalmersProgramGrundniva(ChalmersPage):
    @property
    def title(self):
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]/div/h1').text
