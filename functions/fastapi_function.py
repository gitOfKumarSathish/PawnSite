import os
from magnum import Mangum  # AWS Lambda to ASGI adapter
from run import app   # Import FastAPI app

# Use Mangum to handle requests via AWS Lambda (Netlify Functions)
handler = Mangum(app)
