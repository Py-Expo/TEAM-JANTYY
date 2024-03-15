from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self,hotels:WebElement):
        self.hotels = hotels

    def pull_details(self):
        details = []
        for hotel in self.hotels:
            hotel_title=hotel.find_element(By.CSS_SELECTOR,'div[data-testid="title"]')
            hotel_price = hotel.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]')
            hotel_rating="NA"
            try:
                hotel_rating = hotel.find_element(By.CSS_SELECTOR,'div[class="a3b8729ab1 d86cee9b25"]')
                hotel_rating = hotel_rating.text
            
            except:
                hotel_rating = "NA"
            
            details.append([hotel_title.text,hotel_price.text,hotel_rating])
        return details