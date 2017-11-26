from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = "Saves products in a downloaded feed to the database"

    def handle(self, *args, **kwargs):
        print 'ingesting'

    def extract_row(self, csv_row):
        return csv_row.split('|')


    def data_to_object(self, product_data):
        indexes = {
            'id': 0,
            'product_name': 1,
            'sku': 2,
            'primary_categroy': 3,
            'secondary_category': 4,
            'product_url': 5,
            'product_image_url': 6,
            'buy_url': 7,
            'short_product_description': 8,
            'long_product_description': 9,
            'discount': 10,
            'discount_type': 11,
            'sale_price': 12,
            'retail_price': 13,
            'currency': 25
        }

        return {'name': product_data[indexes['product_name']],
            'image': product_data[indexes['product_image_url']],
            'price': product_data[indexes['retail_price']],
            'url': product_data[indexes['product_url']]}
