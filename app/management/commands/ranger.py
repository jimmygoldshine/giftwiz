from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from app.feed_utils.downloader import FTPDownloader


class Command(BaseCommand):
    help = "Downloads product data from FTP"

    def add_arguments(self, parser):
        parser.add_argument("retailer", type=str, default='all')

    def handle(self, *args, **kwargs):
        ftpDownloader = FTPDownloader()
        ftpDownloader.download(kwargs['retailer'])
