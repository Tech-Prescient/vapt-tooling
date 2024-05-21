import json
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

from zapv2 import ZAPv2

from constants import (
    AUTH_METHOD_NAME,
    AUTH_SCRIPT_TYPE,
    DEFAULT_CONTEXT_NAME,
    DEFAULT_SCAN_POLICY_NAME,
    HTML_REPORT_TEMPLATE,
    HTTP_SENDER_SCRIPT_TYPE,
    PDF_REPORT_TEMPLATE,
    SCRIPT_ENGINE,
    SCRIPT_NAME,
)
from env import (
    ALERT_FILTERS,
    AUTHENTICATION_SCRIPT,
    CONTEXT_FILE,
    LOGGED_OUT_INDICATOR_REGEX,
    PASSWORD,
    REPORT_DIR,
    SCAN_POLICY,
    SCRIPT_PARAMS_FILE,
    SWAGGER_JSON_URL,
    SWAGGER_SCHEMA_FILE,
    TARGET_URL,
    URLS_FILE,
    USERNAME,
)
from utils import (
    add_alert_filters,
    add_urls_to_zap,
    custom_log,
    generate_report,
    spider_scan,
    wait_till_all_the_available_addons_are_installed,
)


def zap_started(zap: ZAPv2, target: str):
    custom_log("Executing zap_started hook ...")

    custom_log("Waiting till all the available addons are installed ...")
    wait_till_all_the_available_addons_are_installed(zap=zap)
    custom_log("Addon installation complete.")

    os.environ["SCAN_START_TS"] = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    if Path(URLS_FILE).is_file():
        custom_log("Adding URLs into zap from txt file ...")
        add_urls_to_zap(zap=zap, target_url=target, urls_file=URLS_FILE)
        custom_log("URLs added successfully.")

    if Path(SWAGGER_SCHEMA_FILE).is_file():
        custom_log(f"Importing Swagger from file...")
        zap.openapi.import_file(file=SWAGGER_SCHEMA_FILE, target=target)
        custom_log("Swagger import successful.")

    elif SWAGGER_JSON_URL:
        custom_log(f"Importing Swagger from {SWAGGER_JSON_URL} ...")
        zap.openapi.import_url(url=SWAGGER_JSON_URL, hostoverride=target)
        custom_log("Swagger import successful.")

    custom_log("Loading Authentication Script ...")
    script_type = AUTH_SCRIPT_TYPE if USERNAME else HTTP_SENDER_SCRIPT_TYPE
    script_loading_status = zap.script.load(
        scriptname=SCRIPT_NAME,
        scripttype=script_type,
        scriptengine=SCRIPT_ENGINE,
        filename=AUTHENTICATION_SCRIPT,
    )
    custom_log("Authentication Script loading status " + script_loading_status)

    if not USERNAME:
        http_sender_script_status = zap.script.enable(
            scriptname=SCRIPT_NAME,
        )
        custom_log("Authentication script enabled " + http_sender_script_status)

    custom_log("Importing Context ...")
    context_id = zap.context.import_context(contextfile=CONTEXT_FILE)
    custom_log("Context import status " + context_id)

    target_regex = target.rstrip("/") + ".*"
    regex_include_status = zap.context.include_in_context(
        contextname=DEFAULT_CONTEXT_NAME, regex=target_regex
    )
    custom_log("Target url regex included in context, status = " + regex_include_status)

    if USERNAME:
        with open(SCRIPT_PARAMS_FILE) as file:
            script_params = json.load(file)

        auth_method_configs = {"scriptName": SCRIPT_NAME, **script_params}

        custom_log("Adding Authentication method ...")
        auth_method_status = zap.authentication.set_authentication_method(
            contextid=context_id,
            authmethodname=AUTH_METHOD_NAME,
            authmethodconfigparams=urlencode(auth_method_configs),
        )
        custom_log("Authentication method added, status = " + auth_method_status)

        logged_out_indicator_status = zap.authentication.set_logged_out_indicator(
            contextid=context_id,
            loggedoutindicatorregex=LOGGED_OUT_INDICATOR_REGEX,
        )
        custom_log(
            "logged_out_indicator set to `"
            + LOGGED_OUT_INDICATOR_REGEX
            + "`, status = "
            + logged_out_indicator_status
        )

        user_id = zap.users.new_user(contextid=context_id, name=USERNAME)
        custom_log(
            "New user created with username = " + USERNAME + ", user_id = " + user_id
        )

        auth_creds = {"username": USERNAME, "password": PASSWORD}
        auth_creds_status = zap.users.set_authentication_credentials(
            contextid=context_id,
            userid=user_id,
            authcredentialsconfigparams=urlencode(auth_creds),
        )
        custom_log("Auth creds set, status = " + auth_creds_status)

        user_enabled_status = zap.users.set_user_enabled(
            contextid=context_id, userid=user_id, enabled=True
        )
        custom_log("User enabled, status " + user_enabled_status)

        forced_user_set = zap.forcedUser.set_forced_user(
            contextid=context_id, userid=user_id
        )
        custom_log("User " + user_id + " set as forced user, status " + forced_user_set)

        force_user_enabled = zap.forcedUser.set_forced_user_mode_enabled(boolean=True)
        custom_log("Forced User Mode enabled, status " + force_user_enabled)

    custom_log("Importing Scan Policy ...")
    zap.ascan.remove_scan_policy(scanpolicyname=DEFAULT_SCAN_POLICY_NAME)
    scan_policy = zap.ascan.import_scan_policy(path=SCAN_POLICY)
    custom_log("Scan policy import status " + scan_policy)

    if Path(ALERT_FILTERS).is_file():
        custom_log("Adding alert filters in zap ...")
        add_alert_filters(zap=zap, alert_filters_path=ALERT_FILTERS)
        custom_log("Alert filters added successfully.")

    custom_log("zap_started hook execution complete.")


def zap_pre_shutdown(zap: ZAPv2):
    custom_log("Executing zap_pre_shutdown hook ...")

    # Spider again before generating report
    spider_scan(zap=zap, target_url=TARGET_URL, context_name=DEFAULT_CONTEXT_NAME)

    custom_log("Generating reports ...")
    generate_report(
        zap=zap,
        title=os.getenv("SCAN_START_TS"),
        template=PDF_REPORT_TEMPLATE,
        report_filename=os.getenv("SCAN_START_TS"),
        report_dir=REPORT_DIR,
    )

    generate_report(
        zap=zap,
        title=os.getenv("SCAN_START_TS"),
        template=HTML_REPORT_TEMPLATE,
        report_filename=os.getenv("SCAN_START_TS"),
        report_dir=REPORT_DIR,
    )
    custom_log("Reports saved at " + REPORT_DIR)

    custom_log("zap_pre_shutdown hook execution complete.")
