from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.settings = {
            "settings_link": (By.CSS_SELECTOR, 'a[href="#/Settings"]'),
            "more_dropdown": (By.XPATH, '//a[contains(text(),"More...")]'),
            "price_category_tab": (By.CSS_SELECTOR, 'ul.dropdown-menu a[href="#/Settings/PriceCategory"]'),
            "activate_success_message": (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Activated."]'),
            "deactivate_success_message": (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Deactivated."]'),
        }

    def disable_button(self, code: str):
        return (By.XPATH, f'//div[text()="{code}"]/../div/span/a[@danphe-grid-action="deactivatePriceCategorySetting"]')

    def enable_button(self, code: str):
        return (By.XPATH, f'//div[text()="{code}"]/../div/span/a[@danphe-grid-action="activatePriceCategorySetting"]')

    def toggle_price_category_status(self):
        """
        /**
        * @Test10
        * @description This method verifies disabling and enabling a price category code in the table.
        * @expected
        * A success message is displayed for both actions: "Deactivated." for disabling and "Activated." for enabling.
        */
        """
        pass
        assert False,"TODO:Implement toggle_price_category_status"
