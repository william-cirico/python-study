from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = "chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-data-dir=Perfil")
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text("Sign in")
            btn_sign_in.click()
        except Exception as e:
            print(f"Erro ao clicar em Sign in {e}")

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id("login_field")
            input_pass = self.chrome.find_element_by_id("password")
            input_login.send_keys("contato.williamc@gmail.com")
            input_pass.send_keys("X*&ricr6*LS4")
            btn_sign_in = self.chrome.find_element_by_name("commit")
            btn_sign_in.click()
        except Exception as e:
            print(f"Erro ao fazer login {e}")

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == "__main__":
    chrome = ChromeAuto()

    chrome.acessa("https://github.com")
    sleep(3)
    chrome.clica_sign_in()
    sleep(3)
    chrome.faz_login()
    sleep(3)
    chrome.sair()