import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from etf_chart import app as dashboard1

# define FastAPI server
app = FastAPI()
# mount the Dash app as a sub-application in the FastAPI server
app.mount("/dashboard1", WSGIMiddleware(dashboard1.server))

# define the main API endpoint
@app.get("/")
async def root():
    return {'message': 'hello world'}

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0")