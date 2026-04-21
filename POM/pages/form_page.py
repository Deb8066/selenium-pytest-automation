
from selenium.webdriver.common.by import By
from base_page import BasePage

class FormPage(BasePage):

    # ---------- Locators ----------
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")

    MALE = (By.ID, "male")
    SUNDAY = (By.ID, "sunday")

    COUNTRY = (By.ID, "country")
    COLORS = (By.ID, "colors")

    DOB = (By.ID, "datepicker")
    START_DATE = (By.ID, "start-date")
    END_DATE = (By.ID, "end-date")

    SUBMIT_BTN = (By.CLASS_NAME, "submit-btn")
    RESULT_TEXT = (By.ID, "result")

    # ---------- Page Actions ----------
    def enter_personal_details(self, name, email, phone):
        self.enter_text(self.NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PHONE, phone)

    def select_gender_and_day(self):
        self.click(self.MALE)
        self.click(self.SUNDAY)

    def select_country_and_color(self, country, color):
        self.select_by_text(self.COUNTRY, country)
        self.select_by_text(self.COLORS, color)

    def enter_dates(self, dob, start_date, end_date):
        self.enter_text(self.DOB, dob)
        self.enter_text(self.START_DATE, start_date)
        self.enter_text(self.END_DATE, end_date)

    def submit_form(self):
        self.click(self.SUBMIT_BTN)

    def get_result_message(self):
        return self.get_text(self.RESULT_TEXT)
