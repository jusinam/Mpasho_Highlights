from app import app
import urllib.request,json
from .models import newsarticle


News = newsarticle.News

# Getting the api key
api_key = app.config['NEWS_API_KEY']