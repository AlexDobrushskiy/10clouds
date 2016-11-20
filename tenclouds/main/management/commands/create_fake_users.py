import requests
import json
import sys
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

RANDOM_USER_URL_TEMPLATE = 'https://randomuser.me/api/?results={}'


class Command(BaseCommand):
    help = '''
    Creates a given number of users.
    Example:
    ./manage.py create_fake_users 100
    Will create 100 users.
    '''

    def add_arguments(self, parser):
        parser.add_argument('number_of_users',  type=int)

    def handle(self, *args, **options):
        response = requests.get(RANDOM_USER_URL_TEMPLATE.format(options['number_of_users']))
        users_json = json.loads(response.content).get('results')
        for user in users_json:
            kwargs = {
                'username': user['login']['username'],
                'first_name': user['name']['first'],
                'last_name': user['name']['last'],
                'email': user['email'],
                'is_staff': False,
                'is_active': True
            }
            sys.stderr.write('Creating {}...\n'.format(user['login']['username']))
            User.objects.create(**kwargs)
        sys.stderr.write('{} Users created.\n'.format(options['number_of_users']))
