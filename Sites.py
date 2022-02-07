import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import random
import string

class easyrogo(unittest.TestCase):
    Sites = '/html/body/app-root/app-dashboard/div/header/nav/div/ul[1]/li[5]/div/a[4]'
    status = '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site/div[1]/div/div[2]/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[3]/datatable-body-row/div[2]/datatable-body-cell[6]/div/input'
    site = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    newsite = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    newprefix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))



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

    def test_1_status(self):
        self.driver.find_element_by_xpath(self.status).click()
        self.driver.find_element_by_xpath('//button[normalize-space()="Ok"]').click()
        self.driver.find_element_by_xpath(self.status).click()
        self.driver.find_element_by_xpath('//button[normalize-space()="Ok"]').click()
        self.driver.find_element_by_xpath(self.status).click()
        self.driver.find_element_by_xpath('//button[normalize-space()="Cancel"]').click()
        time.sleep(5)

    def test_2_page_no(self):
        self.driver.find_element_by_link_text("2").click()
        self.driver.find_element_by_link_text("1").click()
        self.driver.execute_script("window.scrollTo(0, 0)")

    def test_3_add_new(self):
        self.driver.find_element_by_xpath('//button[normalize-space()="ADD NEW"]').click()
        self.driver.find_element_by_xpath('//button[normalize-space()="NEXT"]').click()
        time.sleep(2)
        self.driver.find_element_by_id("sName").click()
        self.driver.find_element_by_id("sName").clear()
        self.driver.find_element_by_id("sName").send_keys("Trade Company")
        self.driver.find_element_by_id("sitePrefix").click()
        self.driver.find_element_by_id("sitePrefix").clear()
        self.driver.find_element_by_id("sitePrefix").send_keys("TRA")
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Currency*'])[1]/following::select[1]")).select_by_visible_text(
            "NPR")
        self.driver.find_element_by_id("siteLocation").click()
        self.driver.find_element_by_id("siteLocation").clear()
        self.driver.find_element_by_id("siteLocation").send_keys("Lagankhel")
        Select(self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Time Zone*'])[1]/following::select[1]")).select_by_visible_text(
                "Osaka, Sapporo, Tokyo")
        self.driver.find_element_by_xpath('//button[normalize-space()="RESET"]').click()
        self.driver.find_element_by_id("sName").click()
        self.driver.find_element_by_id("sName").clear()
        self.driver.find_element_by_id("sName").send_keys(self.site)
        self.driver.find_element_by_id("sitePrefix").click()
        self.driver.find_element_by_id("sitePrefix").clear()
        self.driver.find_element_by_id("sitePrefix").send_keys(self.prefix)
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Currency*'])[1]/following::select[1]")).select_by_visible_text(
            "NPR")
        self.driver.find_element_by_id("siteLocation").click()
        self.driver.find_element_by_id("siteLocation").clear()
        self.driver.find_element_by_id("siteLocation").send_keys("Bhaktapur")
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Time Zone*'])[1]/following::select[1]")).select_by_visible_text(
            "Osaka, Sapporo, Tokyo")
        self.driver.find_element_by_xpath('//button[normalize-space()="NEXT"]').click()
        self.driver.find_element_by_xpath('//button[normalize-space()="ADD DEPARTMENT"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/div/div/div[2]/button/span").click()
        self.driver.find_element_by_id("departmentNames").click()
        self.driver.find_element_by_id("departmentNames").clear()
        self.driver.find_element_by_id("departmentNames").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CLOSE'])[2]/following::button[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[normalize-space()="PREVIOUS"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[normalize-space()="NEXT"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='RESET'])[2]/following::button[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[normalize-space()="AND NEXT"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys("8")
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys("30")
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys("5")
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys("30")
        self.driver.find_element_by_xpath('//button[normalize-space()="AM"]').click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='CLOSE'])[3]/following::button[1]").click()
        time.sleep(2)
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Week Start'])[1]/following::select[1]")).select_by_visible_text(
            "Sunday")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys(
            "8")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys(
            "30")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys(
            "5")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys(
            "30")
        self.driver.find_element_by_xpath('//button[normalize-space()="AM"]').click()
        self.driver.find_element_by_xpath('//button[normalize-space()="AND NEXT"]').click()
        time.sleep(2)

    def test_4_save_close(self):
        self.driver.find_element_by_id("sName").click()
        self.driver.find_element_by_id("sName").clear()
        self.driver.find_element_by_id("sName").send_keys(self.newsite)
        self.driver.find_element_by_id("sitePrefix").click()
        self.driver.find_element_by_id("sitePrefix").clear()
        self.driver.find_element_by_id("sitePrefix").send_keys(self.newprefix)
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Currency*'])[1]/following::select[1]")).select_by_visible_text(
            "NPR")
        self.driver.find_element_by_id("siteLocation").click()
        self.driver.find_element_by_id("siteLocation").clear()
        self.driver.find_element_by_id("siteLocation").send_keys("Patan")
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Time Zone*'])[1]/following::select[1]")).select_by_visible_text(
            "Osaka, Sapporo, Tokyo")
        self.driver.find_element_by_xpath('//button[normalize-space()="NEXT"]').click()
        self.driver.find_element_by_id("departmentNames").click()
        self.driver.find_element_by_id("departmentNames").clear()
        self.driver.find_element_by_id("departmentNames").send_keys("Administration")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='RESET'])[2]/following::button[1]").click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys(
            "9")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys(
            "15")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys(
            "6")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys(
            "25")
        self.driver.find_element_by_xpath('//button[normalize-space()="AM"]').click()
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Default Break Type'])[1]/following::select[1]")).select_by_visible_text(
            "Lunch Break")
        self.driver.find_element_by_xpath("//input[@type='number']").click()
        self.driver.find_element_by_xpath("//input[@type='number']").clear()
        self.driver.find_element_by_xpath("//input[@type='number']").send_keys("60")
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Paid Breaks'])[1]/following::div[4]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='UnSelect All'])[1]/following::label[1]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='PREVIOUS'])[1]/following::div[1]").click()
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/div[2]/div/div/div/angular2-multiselect/div/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/div[2]/div/div/div/angular2-multiselect/div/div[2]/div[3]/div[4]/ul/li[1]').click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='PREVIOUS'])[1]/following::div[1]").click()
        self.driver.find_element_by_xpath('//button[normalize-space()="AND CLOSE"]').click()
        time.sleep(2)

    def test_4_save_close_error(self):
        self.driver.find_element_by_xpath('//button[normalize-space()="ADD NEW"]').click()
        self.driver.find_element_by_id("sName").click()
        self.driver.find_element_by_id("sName").clear()
        self.driver.find_element_by_id("sName").send_keys(self.site)
        self.driver.find_element_by_id("sitePrefix").click()
        self.driver.find_element_by_id("sitePrefix").clear()
        self.driver.find_element_by_id("sitePrefix").send_keys(self.prefix)
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Currency*'])[1]/following::select[1]")).select_by_visible_text(
            "NPR")
        self.driver.find_element_by_id("siteLocation").click()
        self.driver.find_element_by_id("siteLocation").clear()
        self.driver.find_element_by_id("siteLocation").send_keys("Patan")
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Time Zone*'])[1]/following::select[1]")).select_by_visible_text(
            "Osaka, Sapporo, Tokyo")
        self.driver.find_element_by_xpath('//button[normalize-space()="NEXT"]').click()
        self.driver.find_element_by_id("departmentNames").click()
        self.driver.find_element_by_id("departmentNames").clear()
        self.driver.find_element_by_id("departmentNames").send_keys("Administration")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='RESET'])[2]/following::button[1]").click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys(
            "9")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[2]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys(
            "15")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[1]/input').send_keys(
            "6")
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').clear()
        self.driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/form/div/div/div[3]/div/timepicker/table/tbody/tr[2]/td[3]/input').send_keys(
            "25")
        self.driver.find_element_by_xpath('//button[normalize-space()="AM"]').click()
        Select(self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Default Break Type'])[1]/following::select[1]")).select_by_visible_text(
            "Lunch Break")
        self.driver.find_element_by_xpath("//input[@type='number']").click()
        self.driver.find_element_by_xpath("//input[@type='number']").clear()
        self.driver.find_element_by_xpath("//input[@type='number']").send_keys("60")
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Paid Breaks'])[1]/following::div[4]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='UnSelect All'])[1]/following::label[1]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='PREVIOUS'])[1]/following::div[1]").click()
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/div[2]/div/div/div/angular2-multiselect/div/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/main/div/div/app-adminsettings/app-site-form/div/div/div/aw-wizard/div/aw-wizard-step[3]/div[2]/div/div/div/angular2-multiselect/div/div[2]/div[3]/div[4]/ul/li[1]').click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='PREVIOUS'])[1]/following::div[1]").click()
        self.driver.find_element_by_xpath('//button[normalize-space()="AND CLOSE"]').click()
        time.sleep(3)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print("test closed")

if __name__ == '__main__':
    unittest.main()

