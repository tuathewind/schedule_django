from django.test import TestCase

# Create your test here.

from catalog.models import Student, Teacher, Class, Time, Group, Schedule
from django.urls import reverse
from django.contrib.auth.models import User

class StudentListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

        #Create 13 authors for pagination test
        number_of_students = 13
        for student_num in range(number_of_students):
            Student.objects.create(first_name='Name %s' % student_num,
                                   middle_name = 'Patronymic %s' % student_num,
                                   last_name = 'Surname %s' % student_num)

    # def test_view_url_exists_at_desired_location(self):
    #     resp = self.client.get('/catalog/students/')
    #     self.assertEqual(resp.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     resp = self.client.get(reverse('students'))
    #     self.assertEqual(resp.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('students'))
        self.assertRedirects(resp, '/accounts/login/?next=/catalog/students/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('students'))

        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)

        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'catalog/student_list.html')

    # def test_view_uses_correct_template(self):
    #     resp = self.client.get(reverse('students'))
    #     self.assertEqual(resp.status_code, 200)
    #
    #     self.assertTemplateUsed(resp, 'catalog/student_list.html')

    def test_pagination_is_ten(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('students'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['student_list']) == 10)

    def test_lists_all_students(self):
        login = self.client.login(username='testuser1', password='12345')
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('students')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['student_list']) == 3)
