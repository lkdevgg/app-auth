import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()

origins = ["http://localhost:9000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to PNO Services"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=9000, log_level="info", reload=True)
    print("PSP is stopping...")
