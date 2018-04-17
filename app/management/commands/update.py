from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from app.feed_utils.ingester import Ingester
from app.feed_utils.downloader import FTPDownloader
from app.scraper.retailer_configs import configs

class Command(BaseCommand):
    help = "Saves products in a downloaded feed to the database"

    def add_arguments(self, parser):
        parser.add_argument("retailer", type=str, default='all')

    def handle(self, *args, **kwargs):
        ftpDownloader = FTPDownloader()
        ingester = Ingester()
        if kwargs['retailer'] == 'all':
            for retailer in configs:
                ftpDownloader.download(kwargs['retailer'])
                ingester.ingest(kwargs['retailer'])
        else:
            ftpDownloader.download(kwargs['retailer'])
            ingester.ingest(kwargs['retailer'])
