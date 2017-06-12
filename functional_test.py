from selenium import webdriver
import unittest


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
        self.fail('Finish the test!')

        # She finally decide to add work to do in the app.
        # In textbox, she input "Buying peacock feather"
        # (Edith's hobby is making a web to catch a flying fish)

        # When hit the Enter, the page reloaded and...
        # "1: Buying peacock feather" item added in the work list.

        # There are another text-boxes which to additional items in the page.
        # Input : "Making the web by using the peacock feather" (Edith is organized person)

        # The page will reload again, Two items will be in the work list.
        # Edith wonder if the site has input list.
        # The site will provide a specific URL to her.
        # at that time, the site provide also README.

        # Enter the URL, She could see the work list is still in there.

        # and then she go to bed peacefully.

if __name__ == "__main__":
    unittest.main(warnings='ignore')






