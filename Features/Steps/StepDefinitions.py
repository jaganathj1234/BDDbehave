from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import configReader
from Pages import *
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By


@given(u'User is on Registration Page')
def step_impl(context):
    global driver1

    if configReader.readConfigData('Details', 'Browser') == 'Chrome':

        path = "./Driver/chromedriver.exe"
        driver1 = Chrome(executable_path=path)

    elif configReader.readConfigData('Details', 'Browser') == 'Firefox':
        path = "./Driver/geckodriver.exe"
        driver1 = Firefox(executable_path=path)

    driver1.get(configReader.readConfigData('Details', 'Url'))
    driver1.maximize_window()
    register = registrationPage.registrationPageClass(driver1)
    register.registerLink()


# return driver1


@when(u'User enters gender')
def step_impl(context):
    register = registrationPage.registrationPageClass(driver1)
    register.enterGender()


@when(u'User enters first name"{FirstName}"')
def step_impl(context, FirstName):
    register = registrationPage.registrationPageClass(driver1)
    register.enterFirstName(FirstName)


@when(u'User enters last name"{LastName}"')
def step_impl(context, LastName):
    register = registrationPage.registrationPageClass(driver1)
    register.enterlastName(LastName)


@when(u'User enters email"{Email}"')
def step_impl(context, Email):
    register = registrationPage.registrationPageClass(driver1)
    register.emailId(Email)


@when(u'User enters password"{Password}"')
def step_impl(context, Password):
    register = registrationPage.registrationPageClass(driver1)
    register.password(Password)


@when(u'User enters Confirm Password"{ConfirmPassword}"')
def step_impl(context, ConfirmPassword):
    register = registrationPage.registrationPageClass(driver1)
    register.confirmPass(ConfirmPassword)


@when(u'User clicks on Register button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks on Register button')


@then(u'User should be registered successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should be registered successfully')


@when(u'User enters duplicate email"{Email}"')
def step_impl(context, Email):
    register = registrationPage.registrationPageClass(driver1)
    register.emailId(Email)


@then(u'User should not be registered successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should not be registered successfully')


@given(u'user is on website')
def step_impl(context):
    global driver1

    if configReader.readConfigData('Details', 'Browser') == 'Chrome':

        path = "./Driver/chromedriver.exe"
        driver1 = Chrome(executable_path=path)

    elif configReader.readConfigData('Details', 'Browser') == 'Firefox':
        path = "./Driver/geckodriver.exe"
        driver1 = Firefox(executable_path=path)

    driver1.get(configReader.readConfigData('Details', 'Url'))
    driver1.maximize_window()


@when(u'User logs into website"{login_name}""{login_pass}"')
def step_impl(context, login_name, login_pass):
    user_login = loginPage.loginPageClass(driver1)
    user_login.loginLink()
    user_login.emailId(login_name)
    user_login.password(login_pass)
    user_login.loginBut()


@when(u'user adds items to cart')
def step_impl(context):
    cartobj = addtoshoppincartPage.addToCartClass(driver1)
    cartobj.bookLink()
    cartobj.additems()
    cartobj.moveToCart()


@when(u'user confirms checkout')
def step_impl(context):
    confirmchkout = checkOutPage.checkOutClass(driver1)
    confirmchkout.countrySet()
    confirmchkout.TAC()
    confirmchkout.checkOutBut()


@when(
    u'user enters Billing address"{ba_company}""{ba_city}""{ba_address1}""{ba_address2}""{ba_zip}""{ba_phone}""{ba_fax}"')
def step_impl(context, ba_company, ba_city, ba_address1, ba_address2, ba_zip, ba_phone, ba_fax):
    billadd = billingAddress.billingAddressClass(driver1)
    billadd.enterCompany(ba_company)
    billadd.enterCountry()
    billadd.enterCity(ba_city)
    billadd.address(ba_address1, ba_address2)
    billadd.zip(ba_zip)
    billadd.phoneFax(ba_phone, ba_fax)
    billadd.ContniueBut()


@when(u'user enters Shipping address')
def step_impl(context):
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('ShippingAddress', 'continue_but'))))
    sh_add = shippingAddress.shippindAddressClass(driver1)
    sh_add.continuebut()


@when(u'user enters Shipping method')
def step_impl(context):
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('ShippingMethod', 'continue_but'))))
    sh_meth = shippingMethod.shippingMethodClass(driver1)
    sh_meth.shipMethod()
    sh_meth.ContniueBut()


@when(u'user enters Payment method')
def step_impl(context):
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('Paymentmode', 'continue_but'))))
    pay_meth = paymentMethod.paymentMethodClass(driver1)
    pay_meth.paymentmeth()
    pay_meth.ContniueBut()


@when(u'user enters Payment information')
def step_impl(context):
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('PaymentInfo', 'continue_but'))))
    pay_info = paymentInfo.paymentInfoClass(driver1)
    pay_info.ContniueBut()


@when(u'user Confirms order')
def step_impl(context):
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('ConfirmOrder', 'continue_but'))))
    con_order = confirmOrder.confirmOrderClass(driver1)
    con_order.ContniueBut()
