from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = "Saves products in a downloaded feed to the database"

    def handle(self, *args, **kwargs):
        print 'ingesting'
