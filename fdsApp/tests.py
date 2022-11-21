# from unittest import TestCase
#
# from django.urls import reverse
#
# from fdsApp.models import fdsApp, computers
# from django.test import Client
# from django.contrib.auth import authenticate, get_user_model
# from django.db import IntegrityError
#
#
# class LoginTesting(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='testing_user', password='testing',
#                                                          email='test@example.com')
#         self.user.save()
#
#     def tearDown(self):
#         self.user.delete()
#
#     def test_correct_credentials(self):
#         user = authenticate(username='testing_user', password='testing')
#         self.assertTrue((user is not None) and user.is_authenticated)
#
#     def test_wrong_username(self):
#         user = authenticate(username='testing', password='testing')
#         self.assertFalse(user is not None and user.is_authenticated)
#
#     def test_wrong_password(self):
#         user = authenticate(username='testing_user', password='test')
#         self.assertFalse(user is not None and user.is_authenticated)
#
#     def test_no_username_provided(self):
#         self.assertRaises(ValueError, get_user_model().objects.create_user, username='', email='testing@gmail.com',
#                           password='password')
#
#     def test_duplicate_username(self):
#         self.assertRaises(IntegrityError, get_user_model().objects.create_user,
#                           username='testing_user', email='testing@gmail.com', password='password')
#
#
# class BookRegistration(TestCase):
#
#     def setUp(self):
#         self.book_reg = fdsApp.objects.create(name='testing book', quantity_in_stock=2)
#         self.book_reg.save()
#
#     def tearDown(self):
#         self.book_reg.delete()
#
#     def test_book_reg(self):
#         self.assertEqual(self.book_reg.name, 'testing book')
#         self.assertEqual(self.book_reg.quantity_in_stock, 2)
#
#     def test_update_book_stoke(self):
#         self.book_reg.quantity_in_stock = 5
#         self.book_reg.save()
#         self.assertEqual(self.book_reg.quantity_in_stock, 5)
#
#     def test_inventory_list(self):
#         client = Client()
#         response = client.get(reverse('inventory_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'fds_app/inventory_list.html')
#
#     def test_book_reserve(self):
#         book_stock = self.book_reg.quantity_in_stock
#         self.book_reg.quantity_in_stock -= 1
#         self.book_reg.save()
#         book_stock -= 1
#         self.assertEqual(book_stock, self.book_reg.quantity_in_stock)
#
#     def test_book_return(self):
#         book_stock = self.book_reg.quantity_in_stock
#         self.book_reg.quantity_in_stock += 1
#         self.book_reg.save()
#         book_stock += 1
#         self.assertEqual(book_stock, self.book_reg.quantity_in_stock)
#
#     def assertTemplateUsed(self, response, param):
#         pass
#
#
# class ComputersRegistration(TestCase):
#     def setUp(self):
#         self.comp_reg = computers.objects.create(c_name='first_pc', c_quantity_in_stock=2)
#         self.comp_reg.save()
#
#     def tearDown(self):
#         self.comp_reg.delete()
#
#     def test_comp_reg(self):
#         self.assertEqual(self.comp_reg.c_name, 'first_pc')
#         self.assertEqual(self.comp_reg.c_quantity_in_stock, 2)
#
#     def test_update_comp_stoke(self):
#         self.comp_reg.c_quantity_in_stock = 5
#         self.comp_reg.save()
#         self.assertEqual(self.comp_reg.c_quantity_in_stock, 5)
#
#     def test_comp_reserve(self):
#         comp_stock = self.comp_reg.c_quantity_in_stock
#         self.comp_reg.c_quantity_in_stock -= 1
#         self.comp_reg.save()
#         comp_stock -= 1
#         self.assertEqual(comp_stock, self.comp_reg.c_quantity_in_stock)
#
#     def test_comp_free(self):
#         comp_stock = self.comp_reg.c_quantity_in_stock
#         self.comp_reg.c_quantity_in_stock += 1
#         self.comp_reg.save()
#         comp_stock += 1
#         self.assertEqual(comp_stock, self.comp_reg.c_quantity_in_stock)
#
#     def assertTemplateUsed(self, response, param):
#         pass


# comment this code to run above code
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        time.sleep(3)

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(3)

        submit = driver.find_element_by_id('submit')

        user_name.send_keys('admin')
        user_password.send_keys('admin')

        submit.send_keys(Keys.RETURN)
        print(driver.page_source)

        assert 'secretaria@cesar.school' in driver.page_source


class SignUpFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/register')

        time.sleep(3)

        user_name = driver.find_element_by_name('username')
        user_email = driver.find_element_by_name('email')
        user_password = driver.find_element_by_name('password1')
        user_password2 = driver.find_element_by_name('password2')

        time.sleep(3)

        submit = driver.find_element_by_id('submit')

        user_name.send_keys('gamer')
        user_email.send_keys('gamer@gmail.com')
        user_password.send_keys('tester1234')
        user_password2.send_keys('tester1234')

        submit.send_keys(Keys.RETURN)

        assert 'secretaria@cesar.school' in driver.page_source