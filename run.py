from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn,os
from app import customer, models, dashboard, auth
from app.database import engine
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url=None, redoc_url=None)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(auth.router, prefix="/api")

app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/", response_class=FileResponse)
async def serve_vite():
    index_path = os.path.join("static", "index.html")
    return FileResponse(index_path)

@app.get("/{full_path:path}", response_class=FileResponse)
async def serve_spa(full_path: str):
    index_path = os.path.join("static", "index.html")
    return FileResponse(index_path)

# log_config = uvicorn.config.LOGGING_CONFIG
# log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)
