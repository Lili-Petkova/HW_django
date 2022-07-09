from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help_for_you = 'Add new random user. You can add from 1 to 10 users, just enter a number'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        fake = Faker()
        obj = []
        for i in range(options['count']):
            obj.append(User(username=fake.user_name(), email=fake.email(),
                            password=make_password(str(fake.password)), first_name=fake.first_name(),
                            last_name=fake.last_name()))
        User.objects.bulk_create(obj)
