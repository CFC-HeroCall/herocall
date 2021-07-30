import os, subprocess
from django.core.management.base import BaseCommand

# Tip from:
# https://github.com/dpgaspar/Flask-AppBuilder/issues/733#issuecomment-379009480
PORT = int(os.environ.get("PORT", 3000))

class Command(BaseCommand):
    print('here I am')
    print(os.listdir())
    help = 'runs server with gunicorn in a production setting'

    def add_arguments(self, parser):
        print('here I am')
        print(os.listdir())
        parser.add_argument('addrport', nargs='?', default='127.0.0.1:' + str(PORT), help='Optional ipaddr:port')

    def handle(self, *args, **options):
        print('here I am')
        print(os.listdir())
        cmd = ['gunicorn', '-b', options['addrport'], 'heroweb.wsgi']
        subprocess.call(cmd)
