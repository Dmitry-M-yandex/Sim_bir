from selenium.webdriver.common.by import By


class RegistrationFormLocator:
    field_first_name = (By.ID, 'firstName')
    field_last_name = (By.ID, 'lastName')
    field_email = (By.ID, 'userEmail')
    radio_button_gender_dynamic = (By.XPATH, '//label[@for="gender-radio-{}"]')
    field_mobile = (By.ID, 'userNumber')
    pop_up_calendar_date_of_birth = (By.ID, 'dateOfBirthInput')
    calendar_value = (By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker__day")]')
    field_subjects = (By.ID, 'subjectsInput')
    file_picture = (By.CSS_SELECTOR, '.form-control-file')
    field_current_address = (By.ID, 'currentAddress')
    drop_down_list_select_state = (By.ID, 'state')
    drop_down_list_select_city = (By.ID, 'city')
    drop_down_value = (By.XPATH, '//div[contains(@id, "react-select-")]')
    button_submit = (By.ID, 'submit')
    pop_up_window_title = (By.ID, 'example-modal-sizes-title-lg')
    table_value = (By.XPATH, '//tr/td[text()="{}"]/following-sibling::td[text()="{}"]')
