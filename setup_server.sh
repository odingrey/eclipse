./manage.py makemigrations eclipse
./manage.py migrate
./manage.py loaddata eclipse_data
crontab crontab_setup
./manage.py createsuperuser
