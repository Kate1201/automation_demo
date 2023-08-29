import os


# alias for the getting env variables
def get(key, default=None):
    return os.environ.get(key=key, default=default)


# __________________EDITABLE CONFIGURATION__________________
BROWSER = get("BROWSER", "chrome")  # browser name
ENVIRONMENT = get("ENVIRONMENT", "NONPROD")  # PROD, NONPROD
IS_HIDDEN_PROD = get("HIDDEN_PROD", False)
LANGUAGE = get("LANGUAGE", "EN")  # EN, ES, CHI, DE, FR
REGION = get("REGION", "United States")  # China, Ukraine, United States
# If you need another region update REGIONS = { ... } and REGION_TRANSLATIONS = { ... }
# __________________________________________________________

LOCALE_CODE = {"EN": "en,en_US", "CHI": "zh-cn,zh_CN", "ES": "es,es_ES", "DE": "de,de_DE", "FR": "fr,fr_FR"}
URL = "https://makeup.com.ua/"