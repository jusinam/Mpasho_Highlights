from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'MPasho HighLights'
    return render_template('index.html',title = title)

@app.route('/newsarticle/<int:newsarticle_id>')
def newsarticle(newsarticle_id):    
    """
    view news function that returns the movie details page and its data
    """
    return render_template('newsarticle.html',id = newsarticle_id)