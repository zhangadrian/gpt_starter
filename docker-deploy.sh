# use production environment settings
# echo "FLASK_ENV=production" >> .flaskenv
# initialize database
flask db init
# gunicorn server
gunicorn -c gunicorn.conf.py starter:app 
# gunicorn -w 3 -b 0.0.0.0:8080 starter:app
# flask run

