from selenium.webdriver.support.ui import Select
from Library import configReader

class checkOutClass:

    def __init__(self, obj):
        global driver1
        driver1 = obj

    def countrySet(self):
        select = Select(driver1.find_element_by_xpath(configReader.readElementData('CheckOutPage', 'country_sel')))
        select.select_by_index(2)

    def TAC(self):
        driver1.find_element_by_id(configReader.readElementData('CheckOutPage', 'TAC')).click()

    def checkOutBut(self):
        driver1.find_element_by_id(configReader.readElementData('CheckOutPage', 'checkout_but')).click()


