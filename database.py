import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Fetch data from the "CustomerInfo" table
def fetch_table_data():
    response = supabase.table("CustomerInfo").select("*").execute()
    return response.data



#fetch_table_data()