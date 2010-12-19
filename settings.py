# ----------------------------------------------------------------------------------------------------------------------
# SERVER
# ----------------------------------------------------------------------------------------------------------------------

hosts =  [("0.0.0.0", 8080)]

# ----------------------------------------------------------------------------------------------------------------------
# HTTP
# ----------------------------------------------------------------------------------------------------------------------

from elements.http.session import MemcacheSession

http_credentials_url    = "/"
http_gmt_offset         = "-5"
http_login_url          = "/login"
http_max_headers_length = 10000
http_max_request_length = 5000
http_max_upload_size    = None
http_memcache_hosts     = ["127.0.0.1:11211"]
http_session_autostart  = False
http_session_class      = MemcacheSession
http_session_cookie     = "session_id"
http_session_expiration = 30
http_upload_buffer_size = 50000
http_upload_dir         = "/tmp"

# ----------------------------------------------------------------------------------------------------------------------
# RESPONSE FORMATS
# ----------------------------------------------------------------------------------------------------------------------

from bunk.response_formatters.json import JsonFormatter

response_formatters = {
    "json": JsonFormatter
}

# ----------------------------------------------------------------------------------------------------------------------
# DATABASE
# ----------------------------------------------------------------------------------------------------------------------

import MySQLdb

databases = {
    "default": {
        "host":   "localhost",
        "user":   "bunk",
        "passwd": "RESTing",
        "db":     "bunk_db",
        "pool":   2,
        "api":    MySQLdb
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# LOGGING
# ----------------------------------------------------------------------------------------------------------------------

import logging

logging_file  = "./error_log"
logging_level = logging.DEBUG
logging_on    = True

# ----------------------------------------------------------------------------------------------------------------------
# MODEL
# ----------------------------------------------------------------------------------------------------------------------

dbmodel_fk_constraint_err = "Foreign key does not exist"

model_required_err       = "This is required"
model_boolean_type_err   = "Invalid boolean value"
model_date_type_err      = "Invalid date"
model_datetime_type_err  = "Invalid date/time"
model_domain_type_err    = "Invalid domain"
model_email_type_err     = "Invalid email address"
model_float_max_err      = "Maximum size is %3"
model_float_min_err      = "Minimum size is %3"
model_float_type_err     = "Invalid decimal value"
model_int_max_err        = "Maximum size is %3"
model_int_min_err        = "Minimum size is %3"
model_int_type_err       = "Invalid numerical value"
model_ipaddress_type_err = "Invalid IP Address"
model_money_max_err      = "Maximum size is %3"
model_money_min_err      = "Minimum size is %3"
model_money_type_err     = "Invalid money value"
model_text_max_err       = "Maximum length is %3 characters"
model_text_min_err       = "Minimum length is %3 characters"
model_text_regex_err     = "Invalid format"
model_text_type_err      = "Invalid value"
model_time_type_err      = "Invalid time"
model_url_type_err       = "Invalid URL"

