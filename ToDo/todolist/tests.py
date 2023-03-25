from django.test import TestCase
from .models import Task, Category, Status
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class TaskTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='test category')
        self.status = Status.objects.create(name='test status')
        self.user = User.objects.create(first_name='testuser', last_name="test")
        self.task = Task.objects.create(
            user=self.user,
            title='test title',
            description='test description',
            category=self.category,
            status=self.status,
            due_date=datetime.now() + timedelta(days=1)
        )

    def test_task_fields(self):
        """Test that Task fields are correctly set"""
        self.assertEqual(self.task.user.first_name, 'testuser')
        self.assertEqual(self.task.title, 'test title')
        self.assertEqual(self.task.description, 'test description')
        self.assertEqual(self.task.category, self.category)
        self.assertEqual(self.task.status, self.status)
        self.assertIsNotNone(self.task.due_date)

    def test_task_created_at(self):
        """Test that Task created_at is auto set"""
        self.assertIsNotNone(self.task.created_at)

    def test_task_completed_at(self):
        """Test that Task completed_at is initially None"""
        self.assertIsNone(self.task.completed_at)

    def test_task_str(self):
        """Test that Task __str__ method returns the expected string"""
        # given
        # expected_str = f'{self.task.ID}: {self.task.title}'
        # f"Title: {self.title}  Category:  {self.category}  Status: {self.status}."
        expected_str = "Title: test title  Category:  test category  Status: test status."
        # when
        # then
        self.assertEqual(str(self.task), expected_str)


from django.test import TestCase

# Create your tests here.
