from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os
from ftplib import FTP
import gzip
import csv

class FTPDownloader:

    def download(self, directory):
        server = settings.SERVER
        username = settings.USERNAME
        password = settings.PASSWORD
        server_filename = ('%s_3112344_mp.txt.gz' % directory)
        zipped_filename = os.path.join(settings.BASE_DIR, 'downloaded_feeds', '%s.txt.gz' % directory)
        unzipped_filename = os.path.join(settings.BASE_DIR, 'downloaded_feeds', '%s.csv' % directory)
        ftp = FTP(server)
        ftp.login(username, password)
        ftp.retrbinary('RETR %s' % server_filename, open(zipped_filename, 'wb').write)
        self.__unzip_and_save(zipped_filename, unzipped_filename)
        self.__delete_zipped_file(zipped_filename)

    def __unzip_and_save(self, infile, outfile):
        lines=[]
        with gzip.open(infile,'r') as f:
            for line in f:
                line_list = line.split('|')
                lines.append(line_list)

        with open(outfile, 'wb') as f:
            writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_ALL)
            writer.writerows(lines)

    def __delete_zipped_file(self, path):
        os.remove(path)


class Command(BaseCommand):
    help = "Downloads product data from FTP"

    def handle(self, *args, **options):
        ftpDownloader = FTPDownloader()
        ftpDownloader.download('36027')
