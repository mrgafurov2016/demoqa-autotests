import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # включишь позже для CI

    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()