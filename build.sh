#!/bin/bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "from apps.accounts.models import User; User.objects.filter(role='admin').exists() or User.objects.create_superuser('admin@university.edu.ng', 'admin123', role='admin', phone='08000000000', surname='Admin', first_name='System')" | python manage.py shell
