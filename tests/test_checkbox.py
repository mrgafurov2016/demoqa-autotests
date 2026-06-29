from pages.checkbox_page import CheckboxPage


def test_select_single_checkbox_notes(driver):
    page = CheckboxPage(driver)
    page.open_page()

    page.expand_node("Home")
    page.expand_node("Desktop")
    page.check_node("Notes")

    selected_items = page.get_selected_items()

    assert selected_items == ["notes"]