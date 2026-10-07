import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:YOUR_PASSWORD@localhost/student-management"
        
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False