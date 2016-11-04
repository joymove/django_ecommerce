"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import index
from django.shortcuts import render_to_response
#from payment.model import User
from django.test import RequestFactory


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class MainPageTest(TestCase):
    
    def test_root_resolves_to_main_view(self):
        main_page = resolve('/')
	self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html(self):
	index = self.client.get('/')
	self.assertEquals(index.status_code, 200)

    def test_uses_index_html_template(self):
	index = self.client.get('/')
	self.assertTemplateUsed(index,  "index.html")

    def test_returns_exact_html(self):
	index = self.client.get("/")
	self.assertEquals(index.content, render_to_response("index.html").content)

    def test_index_handles_logged_in_user(self):
	# test logic will go here

	self.assertTemplateUsed(resp, 'user.html')

    def test_index_handles_logged_in_user(self):
	# create the user needed for user lookup from index page
	from payments.models import User
	user = User(
		name = 'jj',
		email='j@j.com',
)
	user.save()
	
	#create a Mock request object, so we can manipulate the session
	request_factory  = RequestFactory()
	request = request_factory.get('/')
	request.session= {'user': '1'}
	rep = index(request)
	# verify the response returns the page for the logged in user
	self.assertEquals(rep.content,render_to_response('user.html', {'user': user}).content)
	


