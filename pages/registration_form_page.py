import random

import allure

from locators.registration_form_locator import RegistrationFormLocator
from pages.base_wrapper import BaseWrapper


class RegistrationFormPage(BaseWrapper, RegistrationFormLocator):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поле First Name значением {value}')
    def fill_first_name(self, value: str) -> None:
        self.clear_and_send_keys(self.field_first_name, value)

    @allure.step('Заполняем поле Last Name значением {value}')
    def fill_last_name(self, value: str) -> None:
        self.clear_and_send_keys(self.field_last_name, value)

    @allure.step('Заполняем поле Email значением {value}')
    def fill_email(self, value: str) -> None:
        self.clear_and_send_keys(self.field_email, value)

    @allure.step('Выбираем значение Gender')
    def select_gender(self, gender_number: int) -> None:
        self.find_dynamic_element(self.radio_button_gender_dynamic, gender_number).click()

    @allure.step('Заполняем поле Mobile значением {value}')
    def fill_mobile(self, value: str) -> None:
        self.clear_and_send_keys(self.field_mobile, value)

    @allure.step('Заполняем поле Date of birth')
    def select_birthday(self) -> str:
        self.find_element(self.pop_up_calendar_date_of_birth).click()
        values = self.find_elements(self.calendar_value)[8:25]
        random.choice(values).click()
        return self.find_element(self.pop_up_calendar_date_of_birth).get_attribute('value')

    @allure.step('Заполняем поле Subjects значением {value}')
    def fill_subjects(self, value: str) -> None:
        self.clear_and_send_keys(self.field_subjects, value)

    @allure.step('Добавляем изображение {value}')
    def add_picture(self, value: str) -> None:
        self.find_element(self.file_picture).send_keys(value)

    @allure.step('Заполняем поле Current Address значением {value}')
    def fill_current_address(self, value: str) -> None:
        self.clear_and_send_keys(self.field_current_address, value)

    @allure.step('Выбираем значение в Select State')
    def select_state(self) -> str:
        self.find_element(self.drop_down_list_select_state).click()
        values = self.find_elements(self.drop_down_value)
        state = random.choice(values).text
        random.choice(values).click()
        return state

    @allure.step('Выбираем значение в Select City')
    def select_city(self) -> str:
        self.find_element(self.drop_down_list_select_city).click()
        values = self.find_elements(self.drop_down_value)
        city = random.choice(values).text
        random.choice(values).click()
        return city

    @allure.step('Нажать кнопку Submit')
    def click_submit(self) -> None:
        self.find_element(self.button_submit).click()

    @allure.step('Проверяем появление заполненной таблицы с информацией для регистрации')
    def assert_view_thank_for_submit(self, dict_registration_table: dict) -> None:
        text_title = self.find_element(self.pop_up_window_title).text
        assert text_title == 'Thanks for submitting the form'

        for label, value in dict_registration_table.items():
            locator = self.format_dynamic_locator(self.table_value, label, value)
            assert self.is_element_visible(locator), f'В таблице неправильное значение у параметра {label}'
