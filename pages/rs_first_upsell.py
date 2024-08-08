import time
from pages.base_page_object import BasePage


class RsFirstUpsellPageLocators:
    YES_UPGRADE_BUTTON = "//*[contains(text(), 'YES, Upgrade My Order')]"
    NO_THANKS_BUTTON = "//*[contains(text(), 'No thanks')]"
    BUY_BEST_VALUE_BUTTON = "//*[@data-restore-sleep-sku='RS-6-final-discount']"
    BUY_MOST_POPULAR_BUTTON = "//*[@data-restore-sleep-sku='RS-3-discount']"
    LAST_CHANCE_POPUP_TITLE = "h3.last-chance-heading"


class RsFirstUpsellPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def chose_upsell(self, upgrade, last_chance):
        if upgrade == 'yes':
            self.find_element(RsFirstUpsellPageLocators.YES_UPGRADE_BUTTON).scroll_into_view_if_needed()
            time.sleep(20)
            self.find_element(RsFirstUpsellPageLocators.YES_UPGRADE_BUTTON).click()
        elif upgrade == 'no':
            self.find_element(RsFirstUpsellPageLocators.NO_THANKS_BUTTON).scroll_into_view_if_needed()
            self.find_element(RsFirstUpsellPageLocators.NO_THANKS_BUTTON).click()
            time.sleep(1)
            self.verify_element_visible(RsFirstUpsellPageLocators.LAST_CHANCE_POPUP_TITLE)
            if last_chance == 'no':
                self.find_element(RsFirstUpsellPageLocators.NO_THANKS_BUTTON).click()
            else:
                time.sleep(20)
                button_locator = f"BUY_{last_chance.upper()}_BUTTON"
                self.find_element(RsFirstUpsellPageLocators.__dict__[button_locator]).click()
                # self.scroll_to_element('buy_best_value_button')
                # self.click(f'buy_{last_chance}_button')
