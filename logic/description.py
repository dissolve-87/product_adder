# 3
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

from logic import account as ac

class ProdectDiscrib(ac.SelectTopic):
    def __init__(self):
        self.data = []
        with open('yel_data.csv', newline='') as f:
            reader = csv.reader(f)
            # Skip title
            for val,row in enumerate(reader):
                if val == 0:
                    continue
                self.data.append(row)
        # print(self.data)
        
    def addProduct(self):
        # print('----------------------',self.data)
        self.gdrive = ac.SelectTopic()
        def loopPro(lst):
            
            
            # ---------- Gendral tab button -----------------
            # Product Name
            gdrive.call.driver.find_element_by_id("input-name1").send_keys(lst[0])
            # product description
            gdrive.call.driver.find_element_by_class_name('note-editable').send_keys(lst[1])
            # meta tag title as product name
            gdrive.call.driver.find_element_by_id("input-meta-description1").send_keys(lst[2])
            
            
            # ------------Click Data button --------------
            gdrive.call.driver.find_element_by_link_text("Data").click()

            # select Model ID
            gdrive.call.driver.find_element_by_id("input-model").send_keys("model 0001")
            

            # Making Charge Type
            Mk_charge_tp = Select(gdrive.call.driver.find_element_by_id("input-makingtype"))
            Mk_charge_tp.select_by_visible_text("Fixed Rate")

            # Making Charge
            Mk_charge = gdrive.call.driver.find_element_by_id("input-makingcharge").send_keys(1)
    
            # Gold purity
            goldpurity = Select(gdrive.call.driver.find_element_by_id("input-goldpurity"))
            # goldpurity.select_by_index(2)
            goldpurity.select_by_visible_text("24k")

            # Silver purity
            silverpurity = Select(gdrive.call.driver.find_element_by_id("input-silverpurity"))
            silverpurity.select_by_visible_text("900")
            
            # Platinum Purity
            Platinumpurity = Select(gdrive.call.driver.find_element_by_id("input-platinumpurity"))
            Platinumpurity.select_by_visible_text("950")

            # Metal Wastage(%)
            gdrive.call.driver.find_element_by_id("input-metalwastage").send_keys(10)

            # Price
            gdrive.call.driver.find_element_by_id("input-price").send_keys(1000)

            # Quantity
            gdrive.call.driver.find_element_by_id("input-quantity").send_keys(1)

            # Weight
            gdrive.call.driver.find_element_by_id("input-weight").send_keys(400)



            # --------------- Save ------------------------
            gdrive.call.driver.find_element_by_id("submit").click()

            # --------------- previous tab --------------------
            gdrive.call.driver.back()


            #------------- Image Upload -------------------

            # main_page = gdrive.call.driver.current_window_handle
            # # select image option
            # gdrive.call.driver.find_element_by_id("image-thumb-image").click()
        
        list(map(loopPro, self.gdrive, self.data))