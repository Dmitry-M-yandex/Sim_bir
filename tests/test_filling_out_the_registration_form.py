import random

import allure

from helpers.literals import TEST_IMAGES_DIR, DICT_REGISTRATION_TABLE, FIRST_NAME, LAST_NAME, GENDER_DICT
from pages.registration_form_page import RegistrationFormPage


@allure.title('Заполнение формы регистрации')
def test_registration_form(driver):

    rf_page = RegistrationFormPage(driver)
    rf_page.fill_first_name(FIRST_NAME)
    rf_page.fill_last_name(LAST_NAME)

    rf_page.fill_email(DICT_REGISTRATION_TABLE['Student Email'])

    gender_number = random.randint(1, 3)
    gender = GENDER_DICT[gender_number]
    DICT_REGISTRATION_TABLE['Gender'] = gender
    rf_page.select_gender(gender_number)

    rf_page.fill_mobile(DICT_REGISTRATION_TABLE['Mobile'])

    DICT_REGISTRATION_TABLE['Date of Birth'] = rf_page.select_birthday().replace('Aug ', 'August,')

    rf_page.fill_subjects(DICT_REGISTRATION_TABLE['Subjects'])

    rf_page.add_picture(TEST_IMAGES_DIR)

    rf_page.fill_current_address(DICT_REGISTRATION_TABLE['Address'])

    state = rf_page.select_state()
    city = rf_page.select_city()
    DICT_REGISTRATION_TABLE['State and City'] = f'{state} {city}'

    rf_page.click_submit()
    rf_page.assert_view_thank_for_submit(DICT_REGISTRATION_TABLE)
