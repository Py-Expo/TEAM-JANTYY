from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from booking.booking_filtrations import BookingFiltration   
from booking.booking_report import BookingReport
from prettytable import PrettyTable
import booking.constants as const
import os


class Booking:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'
        ).click()

    def changeCurrency(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        ).click()
        items = self.driver.find_elements(By.CLASS_NAME, "ea1163d21f")
        for item in items:
            if item.text == "USD":
                item.click()
                break

    def select_place_to_go(self, place_to_go):
        input = self.driver.find_element(By.ID, ":re:")
        input.clear()
        input.send_keys(place_to_go)
        WebDriverWait(self.driver, 100).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "a3332d346a"), place_to_go)
        )
        place = self.driver.find_element(By.CLASS_NAME, "a80e7dc237")
        place.click()

    def select_dates(self,checkin,checkout):
        checkin_element = self.driver.find_element(By.CSS_SELECTOR,f'td span[data-date="{checkin}"]')
        checkin_element.click()
        checkout_element = self.driver.find_element(By.CSS_SELECTOR,f'td span[data-date="{checkout}"]')
        checkout_element.click()

    def select_occupancy(self,adults):
        selection = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
        selection.click()
        dec_button = self.driver.find_element(By.CSS_SELECTOR,'div[class*="a7a72174b8"] button[class*="e91c91fa93"]')
        inc_button = self.driver.find_element(By.CSS_SELECTOR,'div[class*="a7a72174b8"] button[class*="f4d78af12a"]')
        count = self.driver.find_element(By.CLASS_NAME,"d723d73d5f")
        while(int(count.text)>1):
            dec_button.click()
        for i in range(adults-1):
            inc_button.click()
    def click_search(self):
        self.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self.driver)
        filtration.sort_by_price()
        filtration.apply_starrating(3,4,5)

    def report_results(self):
        hotels = self.driver.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')
        report = BookingReport(hotels)
        table = PrettyTable(
            field_names=["Hotel Name","Hotel Price", "Hotel Rating"]
        )
        table.add_rows(report.pull_details())
        print(table)
        
        