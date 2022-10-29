release: python manage.py migrate
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_infodokter_data.json'
web: gunicorn project_django.wsgi --log-file -