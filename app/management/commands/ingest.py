from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from app.feed_utils.ingester import Ingester

class Command(BaseCommand):
    help = "Saves products in a downloaded feed to the database"

    def add_arguments(self, parser):
        parser.add_argument("retailer", type=str, default='all')

    def handle(self, *args, **kwargs):
        ingester = Ingester()
        ingester.ingest(kwargs['retailer'])
