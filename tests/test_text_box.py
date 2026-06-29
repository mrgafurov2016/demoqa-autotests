from pages.text_box_page import TextBoxPage


def test_text_box_form_submission(driver):
    page = TextBoxPage(driver)
    page.open_page()

    full_name = "Ivan Petrov"
    email = "ivan.petrov@example.com"
    current_address = "Moscow, Lenina st. 10"
    permanent_address = "Saint Petersburg, Nevsky pr. 5"

    page.fill_form(full_name, email, current_address, permanent_address)
    page.submit()

    assert page.get_output_name() == f"Name:{full_name}"
    assert page.get_output_email() == f"Email:{email}"
    assert page.get_output_current_address() == f"Current Address :{current_address}"
    assert page.get_output_permanent_address() == f"Permananet Address :{permanent_address}"