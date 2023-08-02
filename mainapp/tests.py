from http import HTTPStatus

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, Client
from django.urls import reverse

from django_course import settings
from mainapp import models as mainapp_models
# from selenium.webdriver.firefox import WebDriver


class TestMainPage(TestCase):
    def test_page_open(self):
        path = reverse("mainapp:main_page")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)


# from selenium import webdriver
# import chromedriver_binary
# from time import sleep
#
# browser = webdriver.Chrome()
#
# sleep(5)


# class TestNewsPage(TestCase):
#     fixtures = (
#         'mainapp/fixtures/001_user.json',
#         'mainapp/fixtures/001_news.json',
#     )
#
#     def setUp(self):
#         super().setUp()
#         self.client_with_auth = Client()
#         path_auth = reverse("authapp:login")
#         self.client_with_auth.post(
#             path_auth, data={"username": "admin", "password": "admin"}
#         )
#
#     def test_page_open_list(self):
#         path = reverse("mainapp:news")
#         result = self.client.get(path)
#         self.assertEqual(result.status_code, HTTPStatus.OK)
#
#     def test_page_open_detail(self):
#         news_obj = mainapp_models.News.objects.first()
#         path = reverse("mainapp:news_detail", args=[news_obj.pk])
#         result = self.client.get(path)
#         self.assertEqual(result.status_code, HTTPStatus.OK)
#
#     def test_page_open_crete_deny_access(self):
#         path = reverse("mainapp:news_create")
#         result = self.client.get(path)
#         self.assertEqual(result.status_code, HTTPStatus.FOUND)
#
#     def test_page_open_crete_by_admin(self):
#         path = reverse("mainapp:news_create")
#         result = self.client_with_auth.get(path)
#         self.assertEqual(result.status_code, HTTPStatus.OK)
#
#     def test_create_in_web(self):
#         counter_before = mainapp_models.News.objects.count()
#         path = reverse("mainapp:news_create")
#         self.client_with_auth.post(
#             path,
#             data={
#                 "title": "NewTestNews001",
#                 "preamble": "NewTestNews001",
#                 "body": "NewTestNews001",
#             },
#         )
#         self.assertGreater(mainapp_models.News.objects.count(), counter_before)
#
#     def test_page_open_update_deny_access(self):
#         news_obj = mainapp_models.News.objects.first()
#         path = reverse("mainapp:news_update", args=[news_obj.pk])
#         result = self.client.get(path)
#         self.assertEqual(result.status_code, HTTPStatus.FOUND)
#
#     def test_page_open_update_by_admin(self):
#         news_obj = mainapp_models.News.objects.first()
#         path = reverse("mainapp:news_update", args=[news_obj.pk])
#         result = self.client_with_auth.get(path)
#         self.assertEqual(result.status_code, HTTPStatus.OK)
#
#     def test_update_in_web(self):
#         new_title = "NewTestTitle001"
#         news_obj = mainapp_models.News.objects.first()
#         self.assertNotEqual(news_obj.title, new_title)
#         path = reverse("mainapp:news_update", args=[news_obj.pk])
#         result = self.client_with_auth.post(
#             path,
#             data={
#                 "title": new_title,
#                 "preambule": news_obj.preambule,
#                 "body": news_obj.body,
#             },
#         )
#         self.assertEqual(result.status_code, HTTPStatus.FOUND)
#         news_obj.refresh_from_db()
#         self.assertEqual(news_obj.title, new_title)
#
#     def test_delete_deny_access(self):
#         news_obj = mainapp_models.News.objects.first()
#         path = reverse("mainapp:news_delete", args=[news_obj.pk])
#         result = self.client.post(path)
#         self.assertEqual(result.status_code, HTTPStatus.FOUND)
#
#     def test_delete_in_web(self):
#         news_obj = mainapp_models.News.objects.first()
#         path = reverse("mainapp:news_delete", args=[news_obj.pk])
#         self.client_with_auth.post(path)
#         news_obj.refresh_from_db()
#         self.assertTrue(news_obj.deleted)
#
#
# class TestNewsSelenium(StaticLiveServerTestCase):
#
#     fixtures = (
#         "authapp/fixtures/001_user_admin.json",
#         "mainapp/fixtures/001_news.json",
#     )
#
#     def setUp(self):
#         super().setUp()
#         self.selenium = WebDriver(
#             executable_path=settings.SELENIUM_DRIVER_PATH_FF
#         )
#         self.selenium.implicitly_wait(10)
#         # Login
#         self.selenium.get(f"{self.live_server_url}{reverse('authapp:login')}")
#         button_enter = WebDriverWait(self.selenium, 5).until(
#             EC.visibility_of_element_located(
#                 (By.CSS_SELECTOR, '[type="submit"]')
#             )
#         )
#         self.selenium.find_element_by_id("id_username").send_keys("admin")
#         self.selenium.find_element_by_id("id_password").send_keys("admin")
#         button_enter.click()
#         # Wait for footer
#         WebDriverWait(self.selenium, 5).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, "mt-auto"))
#         )
#
#     def test_create_button_clickable(self):
#         path_list = f"{self.live_server_url}{reverse('mainapp:news')}"
#         path_add = reverse("mainapp:news_create")
#         self.selenium.get(path_list)
#         button_create = WebDriverWait(self.selenium, 5).until(
#             EC.visibility_of_element_located(
#                 (By.CSS_SELECTOR, f'[href="{path_add}"]')
#             )
#         )
#         print("Trying to click button ...")
#         button_create.click()  # Test that button clickable
#         WebDriverWait(self.selenium, 5).until(
#             EC.visibility_of_element_located((By.ID, "id_title"))
#         )
#         print("Button clickable!")
#         # With no element - test will be failed
#         # WebDriverWait(self.selenium, 5).until(
#         #     EC.visibility_of_element_located((By.ID, "id_title111"))
#         # )
#
#     def test_pick_color(self):
#         path = f"{self.live_server_url}{reverse('mainapp:main_page')}"
#         self.selenium.get(path)
#         navbar_el = WebDriverWait(self.selenium, 5).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, "navbar"))
#         )
#         try:
#             self.assertEqual(
#                 navbar_el.value_of_css_property("background-color"),
#                 "rgb(255, 255, 155)",
#             )
#         except AssertionError:
#             with open(
#                 "var/screenshots/001_navbar_el_scrnsht.png", "wb"
#             ) as outf:
#                 outf.write(navbar_el.screenshot_as_png)
#             raise
#
#     def tearDown(self):
#         # Close browser
#         self.selenium.quit()
#         super().tearDown()
