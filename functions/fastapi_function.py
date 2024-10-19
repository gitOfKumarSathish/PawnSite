import os
from mangum import Mangum  # AWS Lambda to ASGI adapter
from app.main import app   # Import FastAPI app

# Use Mangum to handle requests via AWS Lambda (Netlify Functions)
handler = Mangum(app)
