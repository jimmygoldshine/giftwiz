from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from app.models import Product
from app.scraper.scraper import WebScraper
import os
import csv
from tqdm import tqdm

class Command(BaseCommand):
    help = "Saves products in a downloaded feed to the database"

    indexes = {
        'id': 0,
        'product_name': 1,
        'sku': 2,
        'primary_category': 3,
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

    NOTHS = {
        "name": "NOTHS",
        "urls": {
            1: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/1st-anniversary-paper?filter%5Bdelivery_zone%5D=1",
            2: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/2nd-anniversary-cotton",
            3: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/3rd-anniversary-leather",
            4: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/4th-anniversary-linen",
            5: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/5th-anniversary-wood",
            10: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/10th-anniversary-tin",
            25: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/25th-anniversary-silver",
            30: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/30th-anniversary-pearl",
            40: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/40th-anniversary-ruby",
            50: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/50th-anniversary-gold",
            60: "https://www.notonthehighstreet.com/gifts/shop-by-occasion/anniversary/by-year/60th-anniversary-diamond"
        },
        "target": "div.product_details > a[title]",
        "last_page_link": ".pagination_index > a:not(:last-of-type)",
        "next_page": "a.next_page"
    }

    product_anniversary_dict = {}

    def add_arguments(self, parser):
        parser.add_argument("retailer", type=str, default='all')

    def handle(self, *args, **kwargs):
        scraper = WebScraper()
        retailer = kwargs['retailer']
        print 'Scraping {0}...'.format(retailer)
        for anniversary in self.NOTHS['urls']:
            tmp_dict = scraper.scrape(anniversary, self.NOTHS['urls'][anniversary], self.NOTHS)
            self.product_anniversary_dict = self.merge_dicts(self.product_anniversary_dict, tmp_dict)
        print 'Writing products to database...'
        with open ('downloaded_feeds/36027.csv') as f:
            csv_reader = csv.reader(f, delimiter='|')
            next(csv_reader, None)
            for row in csv_reader:
                product = self.data_to_object(row)
                if self.is_new_product(product):
                    self.save_product(product)
                else:
                    print 'product found'
        print 'Writing to database completed successfully'


    def extract_row(self, csv_row):
        return csv_row.split('|')

    def save_product(self, product):
        try:
            if product['anniversary'] > 0:
                Product.objects.create(
                    id=product['id'], name=product['name'],
                    anniversary=product['anniversary'], price=product['price'],
                    image=product['image'], url=product['url'],
                    description=product['description']
                )
                print product['name'], 'created'
        except:

            pass


    def data_to_object(self, product_data):
        try:
            return {
                'id': product_data[self.indexes['id']],
                'name': product_data[self.indexes['product_name']],
                'image': product_data[self.indexes['product_image_url']],
                'price': product_data[self.indexes['retail_price']],
                'url': product_data[self.indexes['product_url']],
                'anniversary': self.find_anniversary(product_data, self.product_anniversary_dict),
                'description': product_data[self.indexes['short_product_description']]
            }
        except:
            return {}

    def find_anniversary(self, product, dictionary):
        if product[self.indexes['product_name']] in dictionary:
            return dictionary[product[self.indexes['product_name']]]
        return False

    def merge_dicts(self, x, y):
        z = x.copy()
        z.update(y)
        return z

    def is_new_product(self, product):
        try:
            Product.objects.get(url__exact=product['url'])
            return False
        except:
            return True
