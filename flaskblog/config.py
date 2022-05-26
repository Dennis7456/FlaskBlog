class Config:
    SECRET_KEY  = 'd7b96227203499913a89ce531ae866ba'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
