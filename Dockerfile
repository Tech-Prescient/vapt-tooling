FROM ghcr.io/zaproxy/zaproxy:stable

COPY /src/ /src/
COPY /build-utils/ /tmp/build-utils/
COPY /report-templates/ /root/.ZAP/reports

ENV PYTHONPATH=/src:

ARG TMP_CONFIG_DIR="/tmp/ZAPConfigs"

ENV ALERT_FILTERS="$TMP_CONFIG_DIR/AlertFilters.csv"
ENV AUTHENTICATION_SCRIPT="$TMP_CONFIG_DIR/authentication.py"
ENV CONTEXT_FILE="$TMP_CONFIG_DIR/Default Context.context"
ENV SCAN_POLICY="$TMP_CONFIG_DIR/Default Policy.policy"
ENV SCRIPT_PARAMS_FILE="$TMP_CONFIG_DIR/script_params.json"
ENV SWAGGER_SCHEMA_FILE="$TMP_CONFIG_DIR/swagger_schema.json"
ENV URLS_FILE="$TMP_CONFIG_DIR/urls.txt"

ENV EXTRA_MODULES_DIR="$TMP_CONFIG_DIR/extra_modules/"
ENV ZAP_CONFIG_XML_PATH="/zap/xml/config.xml"
RUN python /tmp/build-utils/add_jython_module_in_zap_config.py

ENV REPORT_DIR="/reports/"

ENV TARGET_URL=""
ENV ZAP_PORT=8080

CMD "zap-full-scan.py" \
    "-t" ${TARGET_URL} \
    "-d" \
    "-P" ${ZAP_PORT} \
    "--hook" "/src/hooks.py" \
    "-z -silent -addoninstallall -addonupdate"
