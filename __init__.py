import os
from dotenv import load_dotenv
from supabase import create_client, Client
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")

# Initialize the Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
twilioClient = Client(TWILIO_SID, TWILIO_TOKEN)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    db.init_app(app)

    # Import and register the blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app