from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone(Edith) have seen the cool To-Do-List-App was launched.
        # Check the website.
        self.browser.get('http://localhost:8000')

        # The side show 'To-do' in the title and header.
        self.assertIn('To-Do', self.browser.title)
        # MARK: legacy -- self.fail('Finish the test!')
        HeaderText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', HeaderText)

        # She finally decide to add work to do in the app.
        InputBox = self.browser.find_element_by_id('id-new-item')
        self.assertEqual(
            InputBox.get_attribute('placeholder'),
            'Input work to do'
        )

        # In textbox, she input "Buying peacock feather"
        # (Edith's hobby is making a web to catch a flying fish)
        InputBox.send_keys('Buying peacock feather')

        # When hit the Enter, the page reloaded and...
        # "1: Buying peacock feather" item added in the work list.
        InputBox.send_keys(Keys.ENTER)

        # time.sleep(10)

        table = self.browser.find_element_by_id('id-list-table') # NOT `ELEMENT`, `ELEMENTS`
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buying peacock feather' for row in rows),
            'Does not show the new To-do in table'
        )

        # There are another text-boxes which to additional items in the page.
        # Input : "Making the web by using the peacock feather" (Edith is a very organized person)
        self.fail('Finish the test!')


        # The page will reload again, Two items will be in the work list.
        # Edith wonder if the site has input list.
        # The site will provide a specific URL to her.
        # at that time, the site provide also README.

        # Enter the URL, She could see the work list is still in there.

        # and then she go to bed peacefully.

if __name__ == "__main__":
    unittest.main(warnings='ignore')






