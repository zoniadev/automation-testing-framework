import common_variables
from pages.base_page_object import BasePage
from locators import *


class FaceScanPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def fill_face_scan_form(self, row):
        """
        Fills the Face Scan form using a Behave Row object (or dictionary).
        
        Args:
            row: A Behave Row object (from context.table) or a dictionary.
                 Expected headers/keys: height, weight, smoke, blood_pressure, diabetic, age, gender, first_name, email
        """
        # Map column names to (Locator, Action Type)
        # Action Type: 'fill' for inputs, 'select' for dropdowns
        field_map = {
            'height': (HEIGHT_FIELD, 'fill'),
            'weight': (WEIGHT_FIELD, 'fill'),
            'smoke': (SMOKE_SELECT, 'select'),
            'blood_pressure': (BLOOD_PRESSURE_SELECT, 'select'),
            'diabetic': (DIABETIC_SELECT, 'select'),
            'age': (AGE_FIELD, 'fill'),
            'gender': (GENDER_SELECT, 'select'),
            'first_name': (FIRST_NAME_FIELD_SCAN, 'fill'),
            'email': (EMAIL_FIELD_SCAN, 'fill')
        }

        for key, value in row.items():
            if key not in field_map or not value:
                raise Exception('Invalid Face Scan form.')
            locator, action = field_map[key]
            if action == 'fill':
                self.page.locator(locator).fill(str(value))
            elif action == 'select':
                self.page.locator(locator).select_option(value=value)
            self.page.locator(SUBMIT_FACE_SCAN_FORM_BUTTON).click()
            self.wait_for_navigation('https://bioimaging.ariascreening.com/measurement',
                                     timeout=20000)
            print(f'>>> Successfully filled HearthAge screening form and navigated to Face Scan page')
