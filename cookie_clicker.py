from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "biscoito": {
                    "xpath": '//*[@id="bigCookie"]'
                },
                "upgrade": {
                    "xpath": '/html/body/div[1]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]' 
                }
            }
        }

        chrome_service = Service(executable_path="C:\\WebDrivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)   
        time.sleep(20)

    def clicar_no_cookie(self):
        cookie = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SITE_MAP["buttons"]["biscoito"]["xpath"]))
        )
        cookie.click()

    def pega_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2

        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(elemento_atual))
            try:
                classes_objeto = self.driver.find_element(By.XPATH, objeto).get_attribute("class")
                if not "enabled" in classes_objeto:
                    encontrei = True
                else:
                    elemento_atual += 1
            except:
                encontrei = True
        return elemento_atual - 1

    def comprar_upgrade(self):
        melhor_upgrade = self.pega_melhor_upgrade()
        if melhor_upgrade > 0:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pega_melhor_upgrade()))
            try:
                self.driver.find_element(By.XPATH, objeto).click()
            except:
                pass

biscoito = CookieClicker()
biscoito.abrir_site()

i = 0

while True:
    if i % 100  == 0 and i != 0:
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    i += 1
