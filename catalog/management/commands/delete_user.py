from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help_for_you = 'List the id of the users you want to remove, separated by a space. ' \
                   'You can delete all users except the superuser.'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, nargs='+')

    def handle(self, *args, **options):
        user = User.objects.filter(id__in=options['id']).exclude(is_superuser=True).count()
        if user == len(options['id']):
            User.objects.filter(id__in=options['id']).delete()
        else:
            return "You can not delete the superuser."
