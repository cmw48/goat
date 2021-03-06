from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #user navigates to homepage
        self.browser.get('http://localhost:8080')

        #page title mentions to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #enter a todo item
        # type a list item into a text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('here is the first list item.')
        # when enter is pressed, page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_for_row_in_list_table('1: here is the first list item.')

        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertIn('1: here is the first list item.', [row.text for row in rows])
        #self.assertTrue(
        #    any(row.text == '1. here is the first list item.' for row in rows),
        #    f"New to-do item did not appear in table.  Contents were:\n{table.text}")
        ## TODO research generator expressions

        # list item appears in a todo list
        # enter another list item in text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('here is a second list item.')
        # when enter is pressed, page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        ##table = self.browser.find_element_by_id('id_list_table')
        ##rows = table.find_elements_by_tag_name('tr')
        ##self.assertIn('2: here is a second list item.', [row.text for row in rows])
        self.check_for_row_in_list_table('1: here is the first list item.')
        self.check_for_row_in_list_table('2: here is a second list item.')

        # page updates, and both list items are displayed
        self.fail('Finish the test!')
        # page explains that a unique url has been created for this list
        # user navigates to url
        # todo list is displayed
        # end

if __name__ == '__main__':
    unittest.main(warnings='ignore')
