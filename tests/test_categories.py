import unittest
from app.models import Categories

 
class CategoriesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Topnews class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_categories = Categories('engadget','Engadget','NY times under fire','www.foxnews.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_categories,Categories))