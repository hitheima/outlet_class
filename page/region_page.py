import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class RegionPage(BaseAction):
    # area_title
    area_title_feature = By.ID, "com.yunmall.lc:id/area_title"

    @allure.step(title="区域页面 - 选择对应的省市区")
    def choose_region(self):
        region_text = ""
        while True:
            # 如果当前的页面，已经不是省市区选择的页面了，直接结束循环
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return region_text
            # 获取所有的城市的元素
            area_titles = self.find_elements(self.area_title_feature)
            # 获取所有的城市的个数
            area_titles_count = len(area_titles)
            # 根据所有城市的数量，随机生成一个下标
            area_titles_index = random.randint(0, area_titles_count - 1)
            # 保存 选择城市的文字内容
            region_text += area_titles[area_titles_index].text
            # 根据随机下标，取随机城市元素，并点击
            area_titles[area_titles_index].click()
            # 暂定一秒，防止页面没有跳转
            time.sleep(1)



