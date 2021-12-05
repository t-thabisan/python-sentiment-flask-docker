from flask import Flask, redirect, url_for
from routes.sentiment_bp import sentiment_bp

app = Flask(__name__)
app.register_blueprint(sentiment_bp, url_prefix='/sentiment')

@app.route('/')
def index():
    return redirect(url_for('sentiment_bp.sentiment_form'))
    
if __name__ == '__main__':
    app.run()