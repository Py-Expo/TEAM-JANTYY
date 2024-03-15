from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def apply_starrating(self,*star_values):
        for star_value in star_values:
            star_rating = self.driver.find_element(By.CSS_SELECTOR,f'div[data-filters-item="class:class={star_value}"]')
            star_rating.click()

    def sort_by_price(self):
        sort = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sort.click()
        price = self.driver.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        price.click()
