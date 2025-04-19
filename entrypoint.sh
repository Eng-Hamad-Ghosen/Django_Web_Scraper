#!/bin/ash


echo "Apply database migration"
echo "------------------------"
python manage.py migrate
echo "------------------------"
exec "$@"