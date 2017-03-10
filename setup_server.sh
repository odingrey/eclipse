./manage.py makemigrations eclipse
./manage.py migrate
./manage.py loaddata eclipse_data
ECLIPSE_ENV=$(pwd)
crontab crontab_setup
./manage.py createsuperuser
