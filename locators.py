#BasePageLocators:
PLACE_ORDER_BUTTON = "//button[@unique-id='order-btn-1']"
CC_NUM_FRAME = '//iframe[@id="braintree-hosted-field-number"]'
CC_NUM_FIELD = 'Card Number'
CC_EXP_DATE_FRAME = '//iframe[@id="braintree-hosted-field-expirationDate"]'
CC_EXP_DATE_FIELD = 'Expiration Date(MM/YY)'
CC_CVV_FRAME = '//iframe[@id="braintree-hosted-field-cvv"]'
CC_CVV_FIELD = 'Security Code(CCV)'
CC_ZIP_FRAME = '//iframe[@id="braintree-hosted-field-postalCode"]'
CC_ZIP_FIELD = 'Billing Zip/Postal Code'
LOADER = "//*[@unique-id='loader-1']"
JOIN_ZONIA_BUTTON = "//a[text()='JOIN ZONIA NOW']"
REGISTER_FOR_FREE_NOW_BUTTON = "//a[text()='Register for free now']"
FIRST_NAME_REGISTER_FIELD = "//input[@id='first-name']"
SCROLL_ARROW_BUTTON = "//a[@class='arrow']"

#SupplementSalesPageLocators:
BUY_1_BOTTLES_BUTTON = "//*[@unique-id='add-order-1-1']"
BUY_2_BOTTLES_BUTTON = "//*[@unique-id='add-order-2-1']"
BUY_3_BOTTLES_BUTTON = "//*[@unique-id='add-order-3-1']"
BUY_5_BOTTLES_BUTTON = "//*[@unique-id='add-order-5-1']"
BUY_6_BOTTLES_BUTTON = "//*[@unique-id='add-order-6-1']"
FIRST_NAME_FIELD = "//input[@id='form-firstname']"
LAST_NAME_FIELD = "//input[@id='form-lastname']"
EMAIL_FIELD = "//input[@id='form-email']"
PHONE_FIELD = "//input[@id='form-phone']"
ADDRESS_FIELD = "//input[@id='form-address']"
CITY_FIELD = "//input[@id='form-city']"
COUNTRY_FIELD = "//*[@id='form-country']"
STATE_FIELD = "//input[@id='form-state']"
ZIP_FIELD = "//input[@id='form-zip']"

#SupplementUpsellPageLocators:
YES_UPGRADE_BUTTON = "//*[@unique-id='upgrade-order-1']"
NO_THANKS_BUTTON = "//*[@unique-id='no-thanks-1']"
DOWNSELL_NO_THANKS_BUTTON = "//*[@data-id='downsell-no-thanks']"
BUY_BEST_VALUE_BUTTON = "//*[@data-id='add-order-6']"
BUY_MOST_POPULAR_BUTTON = "//*[@data-id='add-order-3']"
BUY_SPECIAL_B4G7_OFFER_BUTTON = "//*[@data-id='add-order-7']"
MEMBERSHIP_YES_BUTTON = "//*[@id='register-top-btn']"
MEMBERSHIP_NO_BUTTON = "//*[@id='skip-registration-top']"
MEMBERSHIP_MONTHLY_BUTTON = "//*[@unique-id='monthly_new-1']"
MEMBERSHIP_QUARTERLY_BUTTON = "//*[@unique-id='quarterly-1']"
MEMBERSHIP_ANNUALLY_BUTTON = "//*[@unique-id='yearly_new-1']"
ACTIVATE_MEMBERSHIP_BUTTON = "//*[@id='register-middle']"

#DocuseriesUpsellPageLocators:
SILVER_PACKAGE_BUTTON = "//button[@unique-id='silver-package-upsell-1']"
PLATINUM_PACKAGE_BUTTON = "//button[@unique-id='platinum-package-upsell-1']"
BUY_MASTERCLASS_BUTTON = "//*[@unique-id='buy-masterclass-1']"
SKIP_MASTERCLASS_BUTTON = "//*[@unique-id='skip-masterclass-1']"

#UserPageLocators:
SKIP_QUESTIONS_BUTTON = "//*[@class='skipAndRegister']"
USER_MENU_BUTTON = "//li[@id='top_header_menu_account']//a[@id='subname']"

#WelcomePageLocators:
PASSWORD_POPUP_FIELD = "//*[@placeholder='Enter password']"
SAVE_PASSWORD_BUTTON = "//*[@class[contains(., 'save-password')] and @type='submit']"
SKIP_LINKING_BUTTON = "//*[@class='home-button']"

#OptInPageLocators:
OPTIN_NAME_FIELD = "//input[@id='first-name']"
OPTIN_NAME_FIELD_AD_LIVE = "//input[@data-id='first-name']"
OPTIN_EMAIL_FIELD = "//input[@id='email']"
PHONE_CHECKBOX = "//input[@name='hasPhone']"
OPTIN_PHONE_FIELD = "//input[@id='phone']"
REGISTER_BUTTON = "//*[@unique-id='register-btn-1']"
REGISTER_SCROLL_BUTTON = "//*[@unique-id='register-btn-scroll-1']"

#JoinZoniaPageLocators:
JOIN_ZONIA_ID_BUTTON = "//*[@unique-id='register-btn-1']"
JOIN_ZONIA_ID_BUTTON_TWL = "//*[@unique-id='register-btn-3']"

#SignUpPageLocators:
MONTHLY_RADIO_BUTTON = "//input[@unique-id='monthly_new-1']"
QUARTERLY_RADIO_BUTTON = "//input[@unique-id='quarterly-1']"
ANNUALLY_RADIO_BUTTON = "//input[@unique-id='yearly_new-1']"
LIFETIME_RADIO_BUTTON = "//input[@unique-id='lifetime-1']"
SIGNUP_NAME_FIELD = "//input[@id='form-name']"
SIGNUP_EMAIL_FIELD = "//input[@id='form-email']"
SIGNUP_PASSWORD_FIELD = "//input[@id='form-password']"
SIGNUP_ACTIVATE_MEMBERSHIP_BUTTON = "//button[@unique-id='activate-membership-1']"

#SpippingAddressPopupLocators:
SHIPPING_POPUP_TITLE = "#shippingModal h5.modal-title"
SHIPPING_FULL_NAME_FIELD = "//input[@id='shippingName']"
SHIPPING_PHONE_FIELD = "//input[@id='shippingPhone']"
SHIPPING_PHONE_FIELD_ALT = "//input[@unique-identifier='shippingPhone-1']"
SHIPPING_PHONE_FIELD_ALT2 = "//input[@unique-identifier='shippingPhone-2']"
SHIPPING_ADDRESS_FIELD = "//input[@id='shippingAddress']"
SHIPPING_ADDRESS_FIELD_ALT = "//input[@unique-identifier='shippingAddress-1']"
SHIPPING_ADDRESS_FIELD_ALT2 = "//input[@unique-identifier='shippingAddress-2']"
SHIPPING_CITY_FIELD = "//input[@id='city']"
SHIPPING_CITY_FIELD_ALT = "//input[@unique-identifier='city-1']"
SHIPPING_CITY_FIELD_ALT2 = "//input[@unique-identifier='city-2']"
SHIPPING_STATE_FIELD = "//input[@id='state']"
SHIPPING_STATE_FIELD_ALT = "//input[@unique-identifier='state-1']"
SHIPPING_STATE_FIELD_ALT2 = "//input[@unique-identifier='state-2']"
SHIPPING_ZIP_FIELD = "//input[@id='postcode']"
SHIPPING_ZIP_FIELD_ALT = "//input[@unique-identifier='postcode-1']"
SHIPPING_ZIP_FIELD_ALT2 = "//input[@unique-identifier='postcode-2']"
SHIPPING_COUNTRY_FIELD = "//input[@id='country']"
SHIPPING_COUNTRY_FIELD_ALT = "//input[@unique-identifier='country-1']"
SHIPPING_COUNTRY_FIELD_ALT2 = "//input[@unique-identifier='country-2']"
SHIPPING_SUBMIT_BUTTON = "//button[@id='save-shipping-address']"

#CookieBannerPopupLocators:
ACCEPT_COOKIES_BUTTON = "//div[@id='cookiebanner']//button[text()='Accept']"

#ChatLocators:
CHAT_FRAME = '//iframe[@title="Chat"]'
CHAT_CLOSE_BUTTON = '//*[@aria-label="Close widget"]'

