from pages.radio_button_page import RadioButtonPage


def test_select_yes_radio_button(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    page.select_yes()

    assert page.get_result_text() == "Yes"


def test_select_impressive_radio_button(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    page.select_impressive()

    assert page.get_result_text() == "Impressive"