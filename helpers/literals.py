import random
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
TEST_IMAGES_DIR = str(ROOT_DIR / 'files' / 'cat.jpg')
TEST_URL = 'https://demoqa.com/automation-practice-form'

FIRST_NAME = 'John'
LAST_NAME = 'Jovani'
GENDER_DICT = {1: 'Male', 2: 'Female', 3: 'Other'}
DICT_REGISTRATION_TABLE = {
    'Student Name': FIRST_NAME + ' ' + LAST_NAME,
    'Student Email': 'megaemail@gmail.com',
    'Gender': '',
    'Mobile': '1234567890',
    'Date of Birth': f'{random.randint(11, 20)} Aug {random.randint(1980, 1999)}',
    'Subjects': 'Somthing subjects',
    'Hobbies': '',
    'Picture': 'cat.jpg',
    'Address': 'Russia, Bashkortostan',
    'State and City': '',
}
