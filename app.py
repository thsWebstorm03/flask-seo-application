# app.py
from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configure logging
log_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
log_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
log_handler.setLevel(logging.INFO)

app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
   app.logger.info('Home route accessed.')
   user_is_logged_in  = True
   return render_template('index.html', user_is_logged_in=user_is_logged_in)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5001)
