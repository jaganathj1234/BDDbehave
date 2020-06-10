from Library import configReader
from selenium.webdriver.support.ui import Select



class billingAddressClass:
    def __init__(self, obj):
        global driver1
        driver1 = obj

    def enterCompany(self, company):
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'company')).send_keys(company)


    def enterCountry(self):
        select = Select(driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'country')))
        select.select_by_index(2)

    def enterCity(self, city):
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'city')).send_keys(city)

    def address(self, address1, address2):
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'address1')).send_keys(address1)
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'address2')).send_keys(address2)

    def zip(self, zip):
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'zip')).send_keys(zip)

    def phoneFax(self, phone, fax):
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'phone')).send_keys(phone)
        driver1.find_element_by_id(configReader.readElementData('BillingAddress', 'fax')).send_keys(fax)

    def ContniueBut(self):
        driver1.find_element_by_xpath(configReader.readElementData('BillingAddress', 'continue_but')).click()
