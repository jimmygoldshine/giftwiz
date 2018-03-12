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
        print 'Connecting to FTP Server...'
        ftp.login(username, password)
        print 'Connected'
        print 'Downloading file...'
        ftp.retrbinary('RETR %s' % server_filename, open(zipped_filename, 'wb').write)
        print 'File downloaded successfully'
        self.__unzip_and_save(zipped_filename, unzipped_filename)
        self.__delete_zipped_file(zipped_filename)
        print 'Ranger completed successfully'

    def __unzip_and_save(self, infile, outfile):
        print 'Reading file...'
        lines=[]
        with gzip.open(infile,'r') as f:
            for line in f:
                line_list = line.split('|')
                if '\n' in line_list:
                    line_list.remove('\n')
                lines.append(line_list)
        print 'Reading file completed'

        print 'Writing file...'
        with open(outfile, 'wb') as f:
            writer = csv.writer(f, delimiter = '|', quoting = csv.QUOTE_ALL)
            writer.writerows(lines)
        print 'Writing file completed'

    def __delete_zipped_file(self, path):
        os.remove(path)


class Command(BaseCommand):
    help = "Downloads product data from FTP"

    def handle(self, *args, **options):
        ftpDownloader = FTPDownloader()
        ftpDownloader.download('36027')
