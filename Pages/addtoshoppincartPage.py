from Library import configReader
import time



class addToCartClass:

    def __init__(self, obj):
        global driver1
        driver1 = obj

    def bookLink(self):
        driver1.find_element_by_xpath(configReader.readElementData('DemoWebMainPage', 'books_link')).click()

    def additems(self):
        driver1.find_element_by_xpath(configReader.readElementData('BooksSelectionPage', 'book_addToCart')).click()
        time.sleep(1)
        driver1.find_element_by_xpath(configReader.readElementData('BooksSelectionPage', 'book_addToCart2')).click()

    def moveToCart(self):
         driver1.find_element_by_xpath(configReader.readElementData('DemoWebMainPage', 'cart_link')).click()


