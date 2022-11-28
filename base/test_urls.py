from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import CustomLoginView, RegisterPage, TaskList, DetailTask, TaskCreate, TaskUpdate, DeleteView


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterPage)

    def test_tasks_url_is_resolved(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func.view_class, TaskList)

    def test_task_create_url_is_resolved(self):
        url = reverse('task-create')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)
