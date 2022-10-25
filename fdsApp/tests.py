from unittest import TestCase

from django.urls import reverse

from fdsApp.models import fdsApp
from django.test import Client
from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError


class LoginTesting(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testing_user', password='testing',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_credentials(self):
        user = authenticate(username='testing_user', password='testing')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='testing', password='testing')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='testing_user', password='test')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_no_username_provided(self):
        self.assertRaises(ValueError, get_user_model().objects.create_user, username='', email='testing@gmail.com',
                          password='password')

    def test_duplicate_username(self):
        self.assertRaises(IntegrityError, get_user_model().objects.create_user,
                          username='testing_user', email='testing@gmail.com', password='password')


class BookRegistration(TestCase):

    def setUp(self):
        self.book_reg = fdsApp.objects.create(name='testing book', quantity_in_stock=2)
        self.book_reg.save()

    def tearDown(self):
        self.book_reg.delete()

    def test_book_reg(self):
        self.assertEqual(self.book_reg.name, 'testing book')
        self.assertEqual(self.book_reg.quantity_in_stock, 2)

    def test_update_book_stoke(self):
        self.book_reg.quantity_in_stock = 5
        self.book_reg.save()
        self.assertEqual(self.book_reg.quantity_in_stock, 5)

    def test_inventory_list(self):
        client = Client()
        response = client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fds_app/inventory_list.html')

    def assertTemplateUsed(self, response, param):
        pass
