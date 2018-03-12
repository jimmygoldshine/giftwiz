from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from app.models import Product
from app.scraper.scraper import WebScraper
import os
import csv

class Command(BaseCommand):
    help = "Delete's all products from the database"

    def handle(self, *args, **kwargs):
        print 'Deleting all products...'
        products = Product.objects.all()
        [product.delete() for product in products]
        print 'All products deleted'
