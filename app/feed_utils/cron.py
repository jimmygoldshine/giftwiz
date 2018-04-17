from django_cron import CronJobBase, Schedule
from app.feed_utils.ingester import Ingester
from app.feed_utils.downloader import FTPDownloader
from app.scraper.retailer_configs import configs

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.feed_utils.cron'    # a unique code

    def do(self):
        print 'cron'
        # ftpDownloader = FTPDownloader()
        # ingester = Ingester()
        # for retailer in configs:
        #     ftpDownloader.download(kwargs['retailer'])
        #     ingester.ingest(kwargs['retailer'])
