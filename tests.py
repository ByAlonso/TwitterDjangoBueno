import unittest
from selenium import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonTwitterWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\villa\Downloads\gecko\geckodriver.exe')
        self.driver.get('http://127.0.0.1:9000/')
        self.username_element = self.driver.find_element_by_name("username")
        self.button_element_reset = self.driver.find_element_by_xpath('/html/body/form[2]/input[2]')

    def test_simple_search(self):
        self.username_element.clear()
        self.username_element.send_keys("@realDonaldTrump")
        self. username_element.submit()
        lista = self.driver.find_element_by_id("id_list")
        self.assertIsNotNone(lista)
        self.driver.quit()

    def test_reset(self):
        self.username_element.clear()
        self.username_element.send_keys("@realDonaldTrump")
        self.username_element.submit()
        self.button_element_reset.click()
        with self.assertRaises(common.exceptions.NoSuchElementException):
            self.driver.find_element_by_id("id_list")
        self.driver.quit()

    def test_invalid_username(self):
        self.username_element.clear()
        self.username_element.send_keys("@realDonaldTrump")
        self.username_element.submit()
        with self.assertRaises(common.exceptions.NoSuchElementException):
            self.driver.find_element_by_id("id_list")
        self.driver.quit()

    def test_empty_submit(self):
        self.button_element_reset.click()
        button_element_execute = self.driver.find_element_by_xpath('/html/body/form[1]/div/div[2]/input')
        button_element_execute.click()
        with self.assertRaises(common.exceptions.NoSuchElementException):
            self.driver.find_element_by_id("id_list")
        self.driver.quit()

    def test_empty_reset(self):
        self.button_element_reset.click()
        self.button_element_reset.click()
        with self.assertRaises(common.exceptions.NoSuchElementException):
            self.driver.find_element_by_id("id_list")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




