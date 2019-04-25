import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonTwitterWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\villa\Downloads\gecko\geckodriver.exe')
        self.driver.get('http://127.0.0.1:9000/')

    def test_simple_search(self):
        usernameElement = self.driver.find_element_by_name("username")
        usernameElement.clear()
        usernameElement.send_keys("@_lalusi")
        usernameElement.submit()
        lista = self.driver.find_element_by_id("id_list")
        correct_list = [['prueba', 5], ['práctica', 3], ['duni', 3], ['tweet', 3], ['王', 3], ['ahora', 2], ['quiero', 2], ['practica', 2], ['ensayo', 2], ['buena', 2], ['cama', 2], ['184', 2], ['iba', 2], ['venido', 2], ['parejas', 2], ['3', 2], ['ayer', 2], ['salir', 2], ['feliz', 2], ['muertos', 2]]
        self.assert_(correct_list,lista)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




