from django.test import TestCase
from list.models import Content
from list import views
# Create your tests here.
class ContentTest(TestCase):
    def test_creat(self):
        url = reversed('creatTodoList')
        data = {
            'content':'tt'
        }
        self.response = self.client.post(url,data)
        #self.assertTrue(Content.objects.exists())

