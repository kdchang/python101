import unittest
from selenium import webdriver

class TestOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1280, 800)

    def test_url(self):
        self.driver.get('https://www.google.com.tw/')
        #self.driver.find_element_by_id('lst-ib').send_keys("realpython")
        print(self.driver.find_element_by_id('lst-ib').get_attribute('innerHTML'))
        # self.driver.find_element_by_name("btnI").click()
        #print(self.driver.find_element_by_tag_name('body').get_attribute('innerHTML'))

    def tearDown(self):
        print('finished')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()