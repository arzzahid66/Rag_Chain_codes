from fastapi import APIRouter , status , Depends, Request
from typing import Union
from fastapi import FastAPI , Response , status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.responses import Response
import uvicorn
from fastapi.params import Body
from typing import Optional
from random import randrange
from fastapi import FastAPI, HTTPException
from conversationa_qa import *
from fetch_data import  fetch_data_by_bot_id 
from delete_bot_id import *
app = FastAPI()
router = APIRouter()


# Fetch data from db 

@router.get("/Fetch_data/{bot_id}")
def get_history(bot_id : int):
    try :
        result = delete_bot_id(bot_id)
        return JSONResponse({"here is response :":result})
    except Exception as ex:
        ex




