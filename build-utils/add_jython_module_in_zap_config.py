import os

ZAP_CONFIG_XML_PATH = os.getenv("ZAP_CONFIG_XML_PATH")
EXTRA_MODULES_DIR = os.getenv("EXTRA_MODULES_DIR")

jython_config = f"""
    <jython version="1">
        <modulepath>{EXTRA_MODULES_DIR}</modulepath>
    </jython>
"""

with open(ZAP_CONFIG_XML_PATH, "r+") as file:
    config = file.readlines()

    config_close_tag = config.pop()
    config.append(jython_config)
    config.append(config_close_tag)

    file.seek(0)
    file.writelines(config)

print("Jython Module Section added in ZAP config")
