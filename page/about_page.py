from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class AboutPage(BaseAction):
    
    # 版本更新
    update_button = By.XPATH, "//*[@text='版本更新']"

    # 点击 版本更新
    @allure.step(title="关于 - 点击 版本更新")
    def click_update(self):
        self.click(self.update_button)
