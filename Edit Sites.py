import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class easyrogo(unittest.TestCase):
    Sites = '/html/body/app-root/app-dashboard/div/header/nav/div/ul[1]/li[5]/div/a[4]'
    Edit = '//datatable-row-wrapper[3]/datatable-body-row/div[2]/datatable-body-cell[7]/div/button/i'



    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get("http://easyrogo.nestrait.com/")
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("jqu80496@zwoho.com")
        self.driver.find_element_by_name("password").click()
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("Template999#")
        self.driver.find_element_by_xpath('//button[normalize-space()="SIGN IN"]').click()
        self.driver.find_element_by_link_text("Admin Settings").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.Sites).click()
        time.sleep(2)

    def test_1_edit_site(self):
        self.driver.find_element_by_xpath(self.Edit).click()
        self.driver.find_element_by_id("sName").click()
        self.driver.find_element_by_id("sName").clear()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[normalize-space()="RESET"]').click()
        time.sleep(2)
        self.driver.find_element_by_id("siteLocation").clear()
        self.driver.find_element_by_id("siteLocation").send_keys("Basantapur")
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[normalize-space()="NEXT"]').click()
        self.driver.find_element_by_id("departmentNames").click()
        self.driver.find_element_by_id("departmentNames").clear()
        self.driver.find_element_by_id("departmentNames").send_keys("Management")
        time.sleep(2)
        self.driver.find_element_by_xpath("(//button[normalize-space()='RESET'])[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("(//button[normalize-space()='NEXT'])[2]").click()
        Select(self.driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Week Start'])[1]/following::select[1]")).select_by_visible_text("Sunday")
        time.sleep(2)
        self.driver.find_element_by_xpath("(//button[normalize-space()='RESET'])[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[normalize-space()="AND CLOSE"]').click()
        time.sleep(5)

    def test_2_close(self):
        self.driver.find_element_by_xpath(self.Edit).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[normalize-space()="CLOSE"]').click()

    def test_3_sorting(self):
        self.driver.find_element_by_xpath("//datatable-header-cell/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[2]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[2]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[3]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[3]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[4]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[4]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[5]/div/span[2]").click()
        self.driver.find_element_by_xpath("//datatable-header-cell[5]/div/span[2]").click()

    def test_4_search(self):
        self.driver.find_element_by_xpath("//input[@type='text']").click()
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("Sharon")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@type='text']").click()
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        time.sleep(1)



    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print("test closed")


if __name__ == '__main__':
    unittest.main()

































