import psycopg2
import psycopg2.extras
from crm_api.config.config import settings

def get_connection():
    conn = psycopg2.connect(settings.DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    return conn