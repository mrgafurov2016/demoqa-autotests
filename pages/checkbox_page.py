from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    URL = "https://demoqa.com/checkbox"

    RESULT_ITEMS = (By.CSS_SELECTOR, "#result span.text-success")

    @staticmethod
    def _switcher_locator(node_text):
        # Находит значок "+/-" для разворачивания узла с указанным текстом
        return (
            By.XPATH,
            f"//span[@class='rc-tree-title' and text()='{node_text}']"
            f"/ancestor::div[contains(@class, 'rc-tree-treenode')]"
            f"//span[contains(@class, 'rc-tree-switcher')]"
        )

    @staticmethod
    def _checkbox_locator(node_text):
        # Находит сам чекбокс (квадратик) для узла с указанным текстом
        return (
            By.XPATH,
            f"//span[@class='rc-tree-title' and text()='{node_text}']"
            f"/ancestor::div[contains(@class, 'rc-tree-treenode')]"
            f"//span[contains(@class, 'rc-tree-checkbox')]"
        )

    def open_page(self):
        self.open(self.URL)

    def expand_node(self, node_text):
        self.click(self._switcher_locator(node_text))

    def check_node(self, node_text):
        self.click(self._checkbox_locator(node_text))

    def get_selected_items(self):
        elements = self.find_all(self.RESULT_ITEMS)
        return [el.text for el in elements]