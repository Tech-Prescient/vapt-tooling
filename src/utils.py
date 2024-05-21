import csv
import logging
import time

from zapv2 import ZAPv2

from env import LOG_PREFIX

YELLOW = "\x1b[33;20m"
RESET = "\x1b[0m"


def custom_log(msg: str):
    logging.debug(YELLOW + LOG_PREFIX + msg + RESET)


def add_urls_to_zap(zap: ZAPv2, target_url: str, urls_file: str):
    with open(urls_file, "r") as file:
        for url in file:
            complete_url = target_url.rstrip("/") + "/" + url.strip().lstrip("/")
            zap.urlopen(complete_url)


def add_alert_filters(zap: ZAPv2, alert_filters_path: str):
    FALSE_POSITIVE = -1
    CSV_URL_HEADER = "URL"
    CSV_ALERT_ID_HEADER = "AlertID"

    with open(alert_filters_path, mode="r") as file:
        for row in csv.DictReader(file):
            url = row.get(CSV_URL_HEADER, "")
            if url:
                url = ".*/" + url.lstrip("/") + ".*"  # converting the URL into regex

            zap.alertFilter.add_global_alert_filter(
                ruleid=row.get(CSV_ALERT_ID_HEADER),
                newlevel=FALSE_POSITIVE,
                url=url,
                urlisregex=True if url else None,
                enabled=True,
            )


def wait_till_all_the_available_addons_are_installed(zap: ZAPv2):
    addon_status_poll_interval_in_sec = 2
    stabilization_time_in_sec = 5

    all_installed = False
    while not all_installed:
        available_addons: list[dict] = zap.autoupdate.marketplace_addons
        installed_addons: list[dict] = zap.autoupdate.installed_addons

        custom_log(
            "Available addons = "
            + str(len(available_addons))
            + " ||| Installed addons = "
            + str(len(installed_addons))
        )

        all_installed = len(available_addons) == len(installed_addons)
        if not all_installed:
            time.sleep(addon_status_poll_interval_in_sec)

    # time to let the zap stabilize
    time.sleep(stabilization_time_in_sec)


def spider_scan(zap: ZAPv2, target_url: str, context_name: str):
    spider_scan_id = zap.spider.scan(url=target_url, contextname=context_name)

    time.sleep(5)
    while int(zap.spider.status(spider_scan_id)) < 100:
        custom_log("Spider progress %: " + zap.spider.status(spider_scan_id))
        time.sleep(5)
    custom_log("Spider complete")


def generate_report(
    zap: ZAPv2, title: str, template: str, report_filename: str, report_dir: str
):
    report_path = zap.reports.generate(
        title=title,
        template=template,
        reportfilename=report_filename,
        reportdir=report_dir,
        includedconfidences="Confirmed|High|Medium|Low",
        includedrisks="High|Medium|Low",
    )
    custom_log(template + " report generated at " + report_path)
