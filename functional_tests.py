from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Let the user check the URL Page
        self.browser.get('http://localhost:8000')
        #Let the user notice the header
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
