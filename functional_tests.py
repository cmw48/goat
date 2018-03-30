from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #user navigates to homepage
        self.browser.get('http://localhost:8000')

        #page title mentions to-do list
        self.assertIn('To-Do', self.browser.title) 
        #, "browser.title was " + browser.title

        self.fail('Finish the test!')

        #enter a todo item
        # type a list item into a text box
        # when enter is pressed, page updates 
        # list item appears in a todo list
        # enter another list item in text box
        # page updates, and both list items are displayed
        # page explains that a unique url has been created for this list
        # user navigates to url
        # todo list is displayed
        # end

if __name__ == '__main__':
    unittest.main(warnings='ignore')

