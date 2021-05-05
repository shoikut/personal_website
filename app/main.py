from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi.encoders import jsonable_encoder
from starlette.responses import RedirectResponse

from get_from_db import db_read
import json

app = FastAPI()


@app.get("/")
async def home():
    data = {
        "text": "hi"
    }
    return {"data": data}


@app.get("/page/{page_name}")
async def page(page_name: str):
    data = {
        "page": page_name
    }
    return {"data": data}

@app.get("/download-sensor-data/")
def download_sensor_data(device : str, last : Optional[str] = '3d', start_date : Optional[str] = None, end_date : Optional[str] = None):
    data = {
        "device"        : device,
        "last"          : last,
        "start_date"    : start_date,
        "end_date"      : end_date
    }

    sensor_readings = jsonable_encoder(db_read(device, last=last, start_date=start_date, end_date=end_date))

    return sensor_readings

@app.get("/modify-sensor-frequency/")
def modify_sensor_frequency(device : str, frequency : int):
    data = {
        "device"            : device,
        "new frequency (s)" : frequency
    }

    return "sensor frequency has been updated"

@app.get("/add-sensor/")
def add_sensor(device : str, last : Optional[str] = '3d', start_date : Optional[str] = None, end_date : Optional[str] = None):
    data = {
        "device"        : device,
        "last"          : last,
        "start_date"    : start_date,
        "end_date"      : end_date
    }

    return "sensor has been added"

@app.get("/remove-sensor/")
def add_sensor(device : str, last : Optional[str] = '3d', start_date : Optional[str] = None, end_date : Optional[str] = None):
    data = {
        "device"        : device,
        "last"          : last,
        "start_date"    : start_date,
        "end_date"      : end_date
    }

    return "sensor has been added"

@app.get("/dashboards")
async def dashboards():
    response = RedirectResponse(url='http://52.20.129.243:3000/')
    return response
