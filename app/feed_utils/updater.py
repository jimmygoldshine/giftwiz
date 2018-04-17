from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from app.feed_utils.ingester import Ingester
from app.feed_utils.downloader import FTPDownloader
from app.scraper.retailer_configs import configs


def update():
    ftpDownloader = FTPDownloader()
    ingester = Ingester()
    for retailer in configs:
        ftpDownloader.download(kwargs['retailer'])
        ingester.ingest(kwargs['retailer'])
