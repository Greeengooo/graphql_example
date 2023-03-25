from uvicorn import run
from api import app

if __name__ == '__main__':
    run(app, host="localhost", port=8080)
