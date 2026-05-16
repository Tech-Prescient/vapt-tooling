path to your folder % `docker run     -p 8080:8080     -u 0    -v VAPT-ZAPConfigs-dir-full-path:/tmp/ZAPConfigs/ \     -v Zap-report-output-dir-full-path:/report/ \     -i     -e TARGET_URL="https://your-site.com/"     vapt-tool:latest`

2024-08-06 09:30:57,908 Trigger hook: cli_opts, args: 1

2024-08-06 09:30:57,908 Using port: 8080

2024-08-06 09:30:57,908 Trigger hook: start_zap, args: 2

2024-08-06 09:30:57,909 Starting ZAP

2024-08-06 09:30:57,911 Params: ['/zap/zap-x.sh', '-daemon', '-port', '8080', '-host', '0.0.0.0', '-config', 'database.recoverylog=false', '-config', 'api.disablekey=true', '-config', 'api.addrs.addr.name=.*', '-config', 'api.addrs.addr.regex=true', '-config', 'spider.maxDuration=0', '-silent', '-addoninstallall', '-addonupdate']

2024-08-06 09:30:59,948 Starting new HTTP connection (1): localhost:8080

`....`

2024-08-06 09:32:41,442 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:42,593 http://localhost:8080 "GET http://zap/JSON/core/view/version/ HTTP/1.1" 200 20

2024-08-06 09:32:42,595 ZAP Version 2.15.0

2024-08-06 09:32:42,595 Took 104 seconds

2024-08-06 09:32:42,596 Trigger hook: zap_started, args: 2

2024-08-06 09:32:42,597 [#########################] - Executing zap_started hook ...

2024-08-06 09:32:42,597 [#########################] - Waiting till all the available addons are installed ...

2024-08-06 09:32:42,600 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:42,640 http://localhost:8080 "GET http://zap/JSON/autoupdate/view/marketplaceAddons/ HTTP/1.1" 200 81615

2024-08-06 09:32:42,644 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:42,675 http://localhost:8080 "GET http://zap/JSON/autoupdate/view/installedAddons/ HTTP/1.1" 200 70867

2024-08-06 09:32:42,677 [#########################] - `Available addons = 108 ||| Installed addons = 108`

2024-08-06 09:32:47,687 [#########################] - `Addon installation complete.`

2024-08-06 09:32:47,695 [#########################] - Adding URLs into zap from txt file ...

2024-08-06 09:32:53,995 https://your-site-url:443 "GET /settings HTTP/1.1" 404 207

2024-08-06 09:32:53,998 [#########################] - `URLs added successfully.`

2024-08-06 09:32:54,002 [#########################] - `Importing Swagger from file...`

2024-08-06 09:32:54,004 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,204 http://localhost:8080 "GET http://zap/JSON/openapi/action/importFile/?file=%2Ftmp%2FZAPConfigs%2Fswagger_schema.json&target=http%3A%2F%2Fdev-api.7thgear.ai%2F HTTP/1.1" 200 17

2024-08-06 09:32:55,206 [#########################] - `Swagger import successful.`

2024-08-06 09:32:55,207 [#########################] - `Loading Authentication Script ...`

2024-08-06 09:32:55,211 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,231 http://localhost:8080 "GET http://zap/JSON/script/action/load/?scriptName=authentication&scriptType=httpsender&scriptEngine=jython&fileName=%2Ftmp%2FZAPConfigs%2Fauthentication.py HTTP/1.1" 200 15

2024-08-06 09:32:55,232 [#########################] - `Authentication Script loading status OK`

2024-08-06 09:32:55,235 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,240 http://localhost:8080 "GET http://zap/JSON/script/action/enable/?scriptName=authentication HTTP/1.1" 200 15

2024-08-06 09:32:55,241 [#########################] - `Authentication script enabled OK`

2024-08-06 09:32:55,242 [#########################] - `Importing Context ...`

2024-08-06 09:32:55,248 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,331 http://localhost:8080 "GET http://zap/JSON/context/action/importContext/?contextFile=%2Ftmp%2FZAPConfigs%2FDefault+Context.context HTTP/1.1" 200 17

2024-08-06 09:32:55,333 [#########################] - `Context import status 1`

2024-08-06 09:32:55,336 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,356 http://localhost:8080 "GET http://zap/JSON/context/action/includeInContext/?contextName=Default+Context&regex=http%3A%2F%2Fdev-api.7thgear.ai.%2A HTTP/1.1" 200 15

2024-08-06 09:32:55,359 [#########################] - `Target url regex included in context, status = OK`

2024-08-06 09:32:55,360 [#########################] - `Importing Scan Policy ...`

2024-08-06 09:32:55,364 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,406 http://localhost:8080 "GET http://zap/JSON/ascan/action/removeScanPolicy/?scanPolicyName=Default+Policy HTTP/1.1" 200 15

2024-08-06 09:32:55,409 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,440 http://localhost:8080 "GET http://zap/JSON/ascan/action/importScanPolicy/?path=%2Ftmp%2FZAPConfigs%2FDefault+Policy.policy HTTP/1.1" 200 15

2024-08-06 09:32:55,441 [#########################] - `Scan policy import status OK`

2024-08-06 09:32:55,443 [#########################] - `Adding alert filters in zap ...`

2024-08-06 09:32:55,448 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,465 http://localhost:8080 "GET http://zap/JSON/alertFilter/action/addGlobalAlertFilter/?ruleId=43&newLevel=-1&enabled=True HTTP/1.1" 200 15

2024-08-06 09:32:55,468 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,478 http://localhost:8080 "GET http://zap/JSON/alertFilter/action/addGlobalAlertFilter/?ruleId=30003&newLevel=-1&enabled=True HTTP/1.1" 200 15

2024-08-06 09:32:55,571 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:32:55,587 http://localhost:8080 "GET http://zap/JSON/alertFilter/action/addGlobalAlertFilter/?ruleId=40025&newLevel=-1&enabled=True HTTP/1.1" 200 15

2024-08-06 09:32:55,589 [#########################] - `Alert filters added successfully.`

2024-08-06 09:32:55,589 [#########################] - `zap_started hook execution complete.`

2024-08-06 09:32:55,589 Tune

2024-08-06 09:32:55,589 Disable all tags

2024-08-06 09:32:55,595 Starting new HTTP connection (1): localhost:8080

`...`

2024-08-06 09:33:06,055 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:33:06,063 http://localhost:8080 "GET http://zap/JSON/spider/view/status/?scanId=0 HTTP/1.1" 200 16

2024-08-06 09:33:06,065 `Spider complete`

2024-08-06 09:33:06,065 Trigger hook: zap_spider_wrap, args: 1

2024-08-06 09:33:06,065 Trigger hook: zap_active_scan, args: 3

2024-08-06 09:33:06,065 `Active Scan https://your-site.com/ with policy Default Policy`

2024-08-06 09:33:06,069 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:33:06,122 http://localhost:8080 "GET http://zap/JSON/ascan/action/scan/?url=http%3A%2F%2Fdev-api.7thgear.ai%2F&recurse=True&scanPolicyName=Default+Policy HTTP/1.1" 200 12

2024-08-06 09:33:11,133 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:33:11,141 http://localhost:8080 "GET http://zap/JSON/ascan/view/status/?scanId=0 HTTP/1.1" 200 14

2024-08-06 09:33:11,148 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:33:11,160 http://localhost:8080 "GET http://zap/JSON/ascan/view/status/?scanId=0 HTTP/1.1" 200 14

2024-08-06 09:33:16,200 `Active Scan progress %:` 1

2024-08-06 09:33:21,208 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:33:21,220 http://localhost:8080 "GET http://zap/JSON/ascan/view/status/?scanId=0 HTTP/1.1" 200 14

2024-08-06 09:39:38,469 `Active Scan progress %:` 68

2024-08-06 09:39:43,483 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:39:43,489 http://localhost:8080 "GET http://zap/JSON/ascan/view/status/?scanId=0 HTTP/1.1" 200 15

2024-08-06 09:40:48,938 `Active Scan progress %:` 98

2024-08-06 09:40:53,953 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:40:53,959 http://localhost:8080 "GET http://zap/JSON/ascan/view/status/?scanId=0 HTTP/1.1" 200 16

2024-08-06 09:40:53,961 `Active Scan complete`

2024-08-06 09:40:53,964 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:40:53,980 http://localhost:8080 "GET http://zap/JSON/ascan/view/scanProgress/?scanId=0 HTTP/1.1" 200 6950

2024-08-06 09:40:53,983 ['https://your-site.com', {'HostProcess': [{'Plugin': ...}]}]

2024-08-06 09:40:53,985 Trigger hook: zap_active_scan_wrap, args: 1

2024-08-06 09:40:53,989 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:40:53,992 http://localhost:8080 "GET http://zap/JSON/pscan/view/recordsToScan/ HTTP/1.1" 200 21

2024-08-06 09:40:53,993 `Records to scan...`

2024-08-06 09:40:53,999 Starting new HTTP connection (1): localhost:8080

2024-08-06 09:40:54,006 http://localhost:8080 "GET http://zap/JSON/pscan/view/recordsToScan/ HTTP/1.1" 200 21

2024-08-06 09:40:54,007 `Passive scanning complete`

2024-08-06 09:40:54,011 Starting new HTTP connection (1): localhost:8080

...

2024-08-06 09:41:02,345 [#########################] - `custom-html report generated at /Zap-report-output/06_08_2024_09_32_47.html`

2024-08-06 09:41:02,346 [#########################] - `Reports saved at /Zap-report-output/`

2024-08-06 09:41:02,346 [#########################] - `zap_pre_shutdown hook execution complete.`

2024-08-06 09:41:02,355 Trigger hook: pre_exit, args: 3

Total of 23 URLs

`PASS`: Directory Browsing [0]

`PASS`: Reflected HTTP GET Parameter(s) [100014]

...

`PASS`: Server Side Template Injection [90035]

`PASS`: Server Side Template Injection (Blind) [90036]

`PASS`: NoSQL Injection - MongoDB (Time Based) [90039]

WARN-NEW: Server Leaks Version Information via "Server" HTTP Response Header Field [10036] x 6

    https://your-site.com/users?type= (301 Moved Permanently)

    https://your-site.com/settings (301 Moved Permanently)

    https://your-site.com/v1/meetings?meeting_ids=meeting_ids (301 Moved Permanently)

    https://your-site.com/ (301 Moved Permanently)

    https://your-site.com/sitemap.xml (301 Moved Permanently)

`FAIL-NEW: 0     FAIL-INPROG: 0  WARN-NEW: 4     WARN-INPROG: 0  INFO: 0 IGNORE: 0      PASS: 14`
