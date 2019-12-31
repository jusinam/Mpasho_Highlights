import unittest
from .models import newsarticle

News = newsarticle.News

class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """
    def setUp(self):
        """
        set up method that will run before every test
        """
        self.new_newsarticle = News(1234,'Python Must Be Crazy','A thrilling breaking news','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993,'Top trending news in the globe by Sir CarlosStone')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newsarticle, News))


if __name__ == '__main__':
    unittest.main()