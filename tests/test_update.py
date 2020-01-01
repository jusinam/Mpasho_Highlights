import unittest
from app.models import NewsUpdate

class NewsUpdateTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsUpdate class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_newsupdate = NewsUpdate('Google News','Justin','NY times under fire','Pretty good','https://image.tmdb.org/t/p/w500/khsjha27hbs','www.foxnews.com', '2018-08-31T17:38:41Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_newsupdate,NewsUpdate))