from django.test import TestCase
from .models import Editor, Article, Tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.alvin = Editor(first_name = 'Alvin', last_name = 'Wanjala', email = 'alvinwanjala@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.alvin,Editor))

    # Testing save method
    def test_save_method(self):
        self.alvin.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)