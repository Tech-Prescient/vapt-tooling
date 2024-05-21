# ZAP Desktop App Guide

Download ZAP Desktop App from [here](https://www.zaproxy.org/download/)  
ZAP 2.14.0 is the latest version on Feb 2024.  

### Start ZAP and Create a Session
__Once the installation is complete open the ZAP App.
You will see an interface like this__  
![](screenshots/zap-home.png)

__Click on start and name the session.__  


### Install all the addons available in the marketplace
__Click on the `Manage Add-ons` icon, and install all the addons from marketplace section__  
![](screenshots/manage-add-ons.png)  


### Import OpenAPI Definition
__Go to Import > Import an OpenAPI Definition__  
![](screenshots/openapi-import-1.png)  

__Enter the definition url, target url and choose `Blank` as context__  
![](screenshots/openapi-import-2.png)  

__This may take some time to complete depending on the number of APIs in the definition. 
You can check the progress in the `Progress` section.__  
![](screenshots/openapi-import-progress.png)  

__Once the import is successful, you will see all the endpoints to be listed in the sites tree.__  
![](screenshots/sites-tree.png)  


### Add login script
__Click on the `+` icon to open the `Scripts` section__  
![](screenshots/script-1.png)  

__Expand `Authentication` and right-click on it to create a new script__  
![](screenshots/script-2.png)  

__Enter the details as shown in the image__  
![](screenshots/script-3.png)  

__Once the script is created, replace the contents of the script with the contents of `login.py` file from `Configs` dir__  
![](screenshots/script-4.png)  


### Import Context
__Delete the existing `Default Context`. Right-click on it > Delete__  
![](screenshots/context-delete.png)  

__Import `Default Context.context` file from `Configs` dir__  
![](screenshots/context-import.png)  

### Add Target URL to the context
__Right-click on the URL in the sites tree and follow the options as shown in the image__  
![](screenshots/context-add-target.png)  


### Set Authentication Mechanism
__Double-click on the context to open it__  
__Go to the `Authentication` section__  
__Select `Script-based authentication`__  
__Then in the Script dropdown select `login` and click on `Load`__  
__This may take few seconds to load the script. Once loaded you will see the input boxes.__  
__Fill the details as shown in the image__  
__Don't forget to add the `Logged Out Regex Pattern`__  
![](screenshots/context-authentication.png)  


### Add User details
__Go to the `Users` section in context details__  
![](screenshots/context-user.png)  


### Export Context
![](screenshots/context-export.png)  


### Import and Export Scan Policy
__Click on the `Scan Policy Manager` icon__  
__And then click on Import / Export accordingly on the Scan Policy Manager window__  
![](screenshots/scan-policy-manager.png)  


### Modify Scan Policy
__Once the scan policy is imported then double-click on it to open the detailed view of it. 
Then modify the threshold and strength accordingly.__


### Add Alert filters
__Click on the `Options` icon__  
![](screenshots/options.png)  

__Open the `Global Alert Filters` section__  
__Add all the alert filters present in the `AlertFilters.csv` file in `Configs` dir__  
__Make sure all of them are in `Enabled` state__
![](screenshots/alert-filters.png)  


### Enable Forced User Mode
__Click on the `Forced User Mode` icon to enable it__  
![](screenshots/forced-user-mode.png)  


### Start Active Scan
__Right-click on the Default Context > Active Scan__  
![](screenshots/active-scan-1.png)  

__Select the fields as shown in the image__  
![](screenshots/active-scan-2.png)  


### Start Spider
__Once the Active Scan is complete, run the spider again__  
__Right-click on the Default Context > Spider__  
![](screenshots/spider-1.png)  

__Select the fields as shown in the image__  
![](screenshots/spider-2.png)  


### Generate Report
__Once all the scans are done, alerts can be seen in the `Alerts` section__  
![](screenshots/alerts.png)  

__Go to Report > Generate Report ...__  
![](screenshots/generate-report.png)

__Fill the details, change the template if needed.__  
__Make sure the `Informational` Risk and `False Positive` Confidence is unchecked in the `Filter` section__  
![](screenshots/generate-report-filter.png)  
