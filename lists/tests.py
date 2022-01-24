from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve is the function Django uses internally to resolve URLs and find what view function they should map to. we are cheking that resolve, when called with "/", the root of the site, finds a function called home_page.
        self.assertEqual(found.func, home_page) # It's the view function we're going to write next, which will actually return HTML we want. You can see from the import that we're planning to store it in lists/views.py


    def test_home_page_returns_correct_html(self):

        request = HttpRequest()#what django will see when a user's browser asks for a page.
        response = home_page(request) #pass home_page view, which gives us a responce. This object is a instance of a class called Httpresponse
        html = response.content.decode('utf8') #Then we extract the .content of the response. These are the raw bytes, the ones and zeros that would be sent the wire to the user's browser. We call .decode() to convert them into the string of HTML that's being sent to the browser.

        self.assertTrue(html.startswith('<html>')) #we want it ti start with an <html> tag which gets closed at the end
        self.assertIn('<title>To-Do lists</title>',html) # we want to a <title> tag somewhere in the middle, with the words "To-Do lists" in it because that's what we specified in our functional test.
        self.assertTrue(html.endswith('</html>'))
