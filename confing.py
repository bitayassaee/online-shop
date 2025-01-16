SQLALCHEMY_DATABASE_URI = "sqlite:///databasse.db"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

SECRET_KEY = "DBJCFBJAJJDCKLPQ.Z25856635QKMXALKXMJ4S5"

PAYMENT_MERCHANT = "sandbox"
PAYMENT_CALLBACK = "http://localhost:5000/verify"
PAYMENT_FIRST_REQUEST_URL = 'https://sandbox.shepa.com/api/v1/token'
PAYMENT_VERIFY_REQUEST_URL = 'https://sandbox.shepa.com/api/v1/verify'