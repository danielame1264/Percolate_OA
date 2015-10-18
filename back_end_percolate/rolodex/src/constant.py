"""
Constants/Regexp for all the possible patterns in the data entry
"""

ZIP_CODE_PATTERN = "(?P<zipcode>\d{5})"
FIRST_NAME_PATTERN = "(?P<first_name>\w+)"
LAST_NAME_PATTERN = "(?P<last_name>\w+)"
PHONE_NUMBER_PATTERN = "(?P<phone_number>(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4})"
COLOR_PATTERN = "(?P<color>[\sa-z]+)"