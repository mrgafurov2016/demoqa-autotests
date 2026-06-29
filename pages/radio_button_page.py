from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RadioButtonPage(BasePage):
    URL = "https://demoqa.com/radio-button"

    YES_LABEL = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_LABEL = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RESULT_TEXT = (By.CLASS_NAME, "text-success")

    def open_page(self):
        self.open(self.URL)

    def select_yes(self):
        self.click(self.YES_LABEL)

    def select_impressive(self):
        self.click(self.IMPRESSIVE_LABEL)

    def get_result_text(self):
        return self.get_text(self.RESULT_TEXT)