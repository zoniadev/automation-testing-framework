#BasePageLocators:
PLACE_ORDER_BUTTON = "//button[@data-id='order-btn']"
CC_NUM_FRAME = '//iframe[@id="braintree-hosted-field-number"]'
CC_NUM_FIELD = 'Card Number'
CC_EXP_DATE_FRAME = '//iframe[@id="braintree-hosted-field-expirationDate"]'
CC_EXP_DATE_FIELD = 'Expiration Date(MM/YY)'
CC_CVV_FRAME = '//iframe[@id="braintree-hosted-field-cvv"]'
CC_CVV_FIELD = 'Security Code(CCV)'
CC_ZIP_FRAME = '//iframe[@id="braintree-hosted-field-postalCode"]'
CC_ZIP_FIELD = 'Billing Zip/Postal Code'
# LOADER = "//*[@test-id='loader']"
LOADER = "//*[@data-id='loader']"
JOIN_ZONIA_BUTTON = "//a[text()='JOIN ZONIA NOW']"
REGISTER_FOR_FREE_NOW_BUTTON = "//a[text()='Register for free now']"
FIRST_NAME_REGISTER_FIELD = "//input[@id='first-name']"
SCROLL_ARROW_BUTTON = "//a[@class='arrow']"

#SupplementSalesPageLocators:
BUY_1_BOTTLES_BUTTON = "//*[@data-id='add-order-1']"
BUY_3_BOTTLES_BUTTON = "//*[@data-id='add-order-3']"
BUY_6_BOTTLES_BUTTON = "//*[@data-id='add-order-6']"
FIRST_NAME_FIELD = "//input[@id='form-firstname']"
LAST_NAME_FIELD = "//input[@id='form-lastname']"
EMAIL_FIELD = "//input[@id='form-email']"
PHONE_FIELD = "//input[@id='form-phone']"
ADDRESS_FIELD = "//input[@id='form-address']"
CITY_FIELD = "//input[@id='form-city']"
COUNTRY_FIELD = "//input[@id='form-country']"
STATE_FIELD = "//input[@id='form-state']"
ZIP_FIELD = "//input[@id='form-zip']"

#SupplementUpsellPageLocators:
YES_UPGRADE_BUTTON = "//*[@data-id='upgrade-order']"
NO_THANKS_BUTTON = "//*[@data-id='no-thanks']"
DOWNSELL_NO_THANKS_BUTTON = "//*[@data-id='downsell-no-thanks']"
BUY_BEST_VALUE_BUTTON = "//*[@data-id='add-order-6']"
BUY_MOST_POPULAR_BUTTON = "//*[@data-id='add-order-3']"
MEMBERSHIP_YES_BUTTON = "//*[@id='register-top-btn']"
MEMBERSHIP_NO_BUTTON = "//*[@id='skip-registration-top']"
MEMBERSHIP_MONTHLY_BUTTON = "//*[@data-plan='monthly_new']"
MEMBERSHIP_QUARTERLY_BUTTON = "//*[@data-plan='quarterly']"
MEMBERSHIP_ANNUALLY_BUTTON = "//*[@data-plan='yearly_new']"
ACTIVATE_MEMBERSHIP_BUTTON = "//*[@id='register-middle']"

#DocuseriesUpsellPageLocators:
SILVER_PACKAGE_BUTTON = "//button[@data-id='silver-package-upsell']"
PLATINUM_PACKAGE_BUTTON = "//button[@data-id='platinum-package-upsell']"
BUY_MASTERCLASS_BUTTON = "//*[@data-id='buy-masterclass']"
SKIP_MASTERCLASS_BUTTON = "//*[@data-id='skip-masterclass']"

#UserPageLocators:
SKIP_QUESTIONS_BUTTON = "//*[@class='skipAndRegister']"
USER_MENU_BUTTON = "//*[@id='subname']"

#WelcomePageLocators:
PASSWORD_POPUP_FIELD = "//*[@placeholder='Enter password']"
SAVE_PASSWORD_BUTTON = "//*[@class[contains(., 'save-password')] and @type='submit']"
SKIP_LINKING_BUTTON = "//button[@class='skip-login']"

#OptInPageLocators:
OPTIN_NAME_FIELD = "//input[@id='first-name']"
OPTIN_EMAIL_FIELD = "//input[@id='email']"
PHONE_CHECKBOX = "//input[@name='hasPhone']"
OPTIN_PHONE_FIELD = "//input[@id='phone']"
# REGISTER_BUTTON = "//button[text()='Register for free now']"
REGISTER_BUTTON = "//button[@data-id='register-btn']"
REGISTER_SCROLL_BUTTON = "//*[@data-id='register-btn-scroll']"

#JoinZoniaPageLocators:
JOIN_ZONIA_ID_BUTTON = "//*[@data-id='register-btn']"

#SignUpPageLocators:
MONTHLY_RADIO_BUTTON = "//input[@data-cycle='monthly_new']"
QUARTERLY_RADIO_BUTTON = "//input[@data-cycle='quarterly']"
ANNUALLY_RADIO_BUTTON = "//input[@data-cycle='yearly_new']"
SIGNUP_NAME_FIELD = "//input[@id='form-name']"
SIGNUP_EMAIL_FIELD = "//input[@id='form-email']"
SIGNUP_PASSWORD_FIELD = "//input[@id='form-password']"
# SIGNUP_ACTIVATE_MEMBERSHIP_BUTTON = "//button[text()='activate my membership']"
SIGNUP_ACTIVATE_MEMBERSHIP_BUTTON = "//button[@data-id='activate-membership']"

#SpippingAddressPopupLocators:
SHIPPING_FULL_NAME_FIELD = "//input[@id='shippingName']"
SHIPPING_PHONE_FIELD = "//input[@id='shippingPhone']"
SHIPPING_ADDRESS_FIELD = "//input[@id='shippingAddress']"
SHIPPING_CITY_FIELD = "//input[@id='city']"
SHIPPING_STATE_FIELD = "//input[@id='state']"
SHIPPING_ZIP_FIELD = "//input[@id='postcode']"
SHIPPING_COUNTRY_FIELD = "//input[@id='country']"
SHIPPING_SUBMIT_BUTTON = "//button[@id='save-shipping-address']"

