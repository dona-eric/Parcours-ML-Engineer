from fastapi import FastAPI
import uvicorn, os, logging

logging.basicConfig(level=logging.INFO)
logging.getLogger("uvicorn.error").setLevel(logging.INFO)

app = FastAPI()







if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.1", port=8000, log_level="info")