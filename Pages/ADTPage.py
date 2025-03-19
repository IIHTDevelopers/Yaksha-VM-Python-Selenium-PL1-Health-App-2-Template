import time
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ADTPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "PatientName.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.test_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.ADT = {
            "ADT_link": (By.CSS_SELECTOR, 'a[href="#/ADTMain"]'),
            "search_bar": (By.CSS_SELECTOR, "#quickFilterInput"),
            "admitted_patients_tab": (By.CSS_SELECTOR, 'ul.page-breadcrumb a[href="#/ADTMain/AdmittedList"]'),
            "more_options_button": (By.XPATH, "//button[contains(text(),'...')]"),
            "change_doctor_option": (By.CSS_SELECTOR, 'a[danphe-grid-action="changedr"]'),
            "change_doctor_modal": (By.CSS_SELECTOR, 'div.modelbox-div'),
            "update_button": (By.XPATH, '//button[text()="Update"]'),
            "field_error_message": (By.XPATH, "//span[text()='Select doctor from the list.']"),
            "counter_item": (By.XPATH, "//div[@class='counter-item']"),
        }

    def verify_field_level_error_message(self):
        """
        /**
        * @Test14
        * @description This test verifies that the error message "Select doctor from the list." is displayed
        *              when the user attempts to update the doctor without selecting a value.
        * @expected The error message "Select doctor from the list." is shown near the field.
        */
        """
        pass
    assert False, "TODO:Implement verify_field_level_error_message"
