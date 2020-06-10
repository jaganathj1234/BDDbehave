from Library import configReader

class shippindAddressClass:
    def __init__(self, obj):
        global driver1
        driver1 = obj

    def continuebut(self):
        driver1.find_element_by_xpath(configReader.readElementData('ShippingAddress', 'continue_but')).click()