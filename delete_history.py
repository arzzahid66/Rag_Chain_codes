
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
from delete_bot_id import delete_bot_id

app = FastAPI()
router = APIRouter()

# Fetch data from db 

@router.get("/delete_data/{bot_id}")
def get_history(bot_id : int):
    try :
        deleted = delete_bot_id(bot_id)
        return {f"Here is Deleted bot id {deleted}"}
    except Exception as ex:
        ex






