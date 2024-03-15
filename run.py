from booking.booking import Booking

bot = Booking()
bot.land_first_page()
bot.changeCurrency()
bot.select_place_to_go("Los Angeles")
bot.select_dates(checkin="2023-09-05",checkout="2023-09-09")
bot.select_occupancy(5)
bot.click_search()
bot.apply_filtration()
bot.driver.refresh()
bot.report_results()