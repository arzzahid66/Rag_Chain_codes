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
# from simple_qa import*
from fastapi import FastAPI, HTTPException
from conversationa_qa import *
from fetch_data import  fetch_data_by_bot_id 

app = FastAPI()
router = APIRouter()


class QueryRequest(BaseModel):
    input_query: str
    bot_id: str


@router.post("/posts/conversational_Retrieval_chain")
async def process_query(query_request: QueryRequest):
    input_query = query_request.input_query
    bot_id = query_request.bot_id
    input_query, ai_response = qa_retrieval_with_conv(input_query,bot_id)
    conn = connect()
    insert_data(conn, input_query, ai_response, bot_id)
    return {"input_query": input_query, "ai_response": ai_response}













# Q A  End point 

# @app.post("/posts/QA/{input_query}")
# def get_QA(input_query):
#     try :
#         result = rag(input_query)
        
#         return JSONResponse({"here is response :":result})
    
#     except Exception as ex:
#         ex

#  Q A Retrieval End point 

# @app.post("/posts/QA Retrieval/{input_query}")
# def get_QA(input_query):
#     try :
#         result = qa_retrieval(input_query)
        
#         return JSONResponse({"here is response :":result})
    
#     except Exception as ex:
#         ex

# conversational chain 

# @app.post("/posts/conversational_chain/{input_query}")
# def get_QA(input_query):
#     try :
#         result = simple_conversational_chain(input_query)
        
#         return JSONResponse({"here is response :":result})
    
#     except Exception as ex:
#         ex

# conversational_Retrieval_chain :
# conn = connect()
# class QueryRequest(BaseModel):
#     input_query: str
#     bot_id: str

# @app.post("/posts/conversational_Retrieval_chain")
# async def process_query(query_request: QueryRequest):
#     input_query = query_request.input_query
#     bot_id = query_request.bot_id
#     input_query, ai_response = qa_retrieval_with_conv(input_query,bot_id)
#     conn = connect()
#     insert_data(conn, input_query, ai_response, bot_id)
#     return {"input_query": input_query, "ai_response": ai_response}

# # Fetch data from db 

# @app.get("/Fetch_data/{bot_id}")
# def get_history(bot_id):
#     try :
#         result = fetch_data_by_bot_id(bot_id)
#         return JSONResponse({"here is response :":result})
#     except Exception as ex:
#         ex

