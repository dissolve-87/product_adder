# 2
from logic import login as lg


class SelectTopic(lg.Login):
    # choose Add procduct icon click
    def __init__(self):
        self.call = lg.Login()
        self.call.driver.find_element_by_css_selector('i.icon.icon-noun_add-product_3848212-1').click()
