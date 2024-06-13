from django.test import TestCase

# Create your test here.

from catalog.models import Student, Teacher, Class, Time, Group

class StudentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Student.objects.create(first_name='Иван',
                               middle_name='Петрович',
                               last_name='Иванов')

    def test_first_name_label(self):
         student=Student.objects.get(id=1)
         field_label = student._meta.get_field('first_name').verbose_name
         self.assertEqual(field_label,'first name')

    def test_middle_name_label(self):
         student=Student.objects.get(id=1)
         field_label = student._meta.get_field('middle_name').verbose_name
         self.assertEqual(field_label,'middle name')

    def test_last_name_label(self):
         student=Student.objects.get(id=1)
         field_label = student._meta.get_field('last_name').verbose_name
         self.assertEqual(field_label,'last name')

    def test_first_name_max_length(self):
         student=Student.objects.get(id=1)
         max_length = student._meta.get_field('first_name').max_length
         self.assertEqual(max_length,100)

    def test_middle_name_max_length(self):
         student=Student.objects.get(id=1)
         max_length = student._meta.get_field('middle_name').max_length
         self.assertEqual(max_length,100)

    def test_last_name_max_length(self):
         student=Student.objects.get(id=1)
         max_length = student._meta.get_field('last_name').max_length
         self.assertEqual(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
         student=Student.objects.get(id=1)
         expected_object_name = '%s %s %s' % (student.last_name, student.first_name, student.middle_name)
         self.assertEqual(expected_object_name,str(student))

    def test_get_absolute_url(self):
         student=Student.objects.get(id=1)
         self.assertEqual(student.get_absolute_url(),'/catalog/student/1')


class TeacherModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Teacher.objects.create(first_name='Иван',
                               middle_name='Петрович',
                               last_name='Иванов')

    def test_first_name_label(self):
         teacher=Teacher.objects.get(id=1)
         field_label = teacher._meta.get_field('first_name').verbose_name
         self.assertEqual(field_label,'first name')

    def test_middle_name_label(self):
         teacher=Teacher.objects.get(id=1)
         field_label = teacher._meta.get_field('middle_name').verbose_name
         self.assertEqual(field_label,'middle name')

    def test_last_name_label(self):
         teacher=Teacher.objects.get(id=1)
         field_label = teacher._meta.get_field('last_name').verbose_name
         self.assertEqual(field_label,'last name')

    def test_first_name_max_length(self):
         teacher=Teacher.objects.get(id=1)
         max_length = teacher._meta.get_field('first_name').max_length
         self.assertEqual(max_length,100)

    def test_middle_name_max_length(self):
         teacher=Teacher.objects.get(id=1)
         max_length = teacher._meta.get_field('middle_name').max_length
         self.assertEqual(max_length,100)

    def test_last_name_max_length(self):
         teacher=Teacher.objects.get(id=1)
         max_length = teacher._meta.get_field('last_name').max_length
         self.assertEqual(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
         teacher = Teacher.objects.get(id=1)
         expected_object_name = '%s %s %s' % (teacher.last_name, teacher.first_name, teacher.middle_name)
         self.assertEqual(expected_object_name,str(teacher))

    def test_get_absolute_url(self):
         teacher = Teacher.objects.get(id=1)
         self.assertEqual(teacher.get_absolute_url(),'/catalog/teacher/1')

class ClassModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Class.objects.create(number_class='176a')

    def test_last_name_max_length(self):
         classtest=Class.objects.get(id=1)
         max_length = classtest._meta.get_field('number_class').max_length
         self.assertEqual(max_length,12)

    def test_object_name_is_number_class(self):
         classtest=Class.objects.get(id=1)
         expected_object_name = classtest.number_class
         self.assertEqual(expected_object_name,str(classtest))


class GroupModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(number='4443-100301D')

    def test_last_name_max_length(self):
        group = Group.objects.get(id=1)
        max_length = group._meta.get_field('number').max_length
        self.assertEqual(max_length, 12)

    def test_object_name_is_number_class(self):
        group = Group.objects.get(id=1)
        expected_object_name = group.number
        self.assertEqual(expected_object_name, str(group))

