import pandas as pd
import numpy as np 
from typing import Literal
from fastapi import FastAPI,Path,Query,HTTPException,JSONResponse
from pydantic import BaseModel,Field,computed_field
import pickle



with open('model.pkl','rb') as f:
    model=pickle.load(f)

app=FastAPI(    )