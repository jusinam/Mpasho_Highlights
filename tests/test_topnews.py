import unittest
from app.models import TopNews
 
class TopnewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Topnews class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_topnews = TopNews('Google News','Justin','NY times under fire','Pretty good','https://image.tmdb.org/t/p/w500/khsjha27hbs','www.foxnews.com')
    