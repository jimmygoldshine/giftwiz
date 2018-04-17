from app.models import Product
from app.scraper.scraper import WebScraper
from app.scraper.retailer_configs import configs
import os
import csv

class Ingester:

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

    product_anniversary_dict = {}

    def ingest(self, retailer):
        scraper = WebScraper()
        print 'Scraping {0}...'.format(retailer)
        for anniversary in configs[retailer]['urls']:
            tmp_dict = scraper.scrape(anniversary, configs[retailer]['urls'][anniversary], configs[retailer])
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
