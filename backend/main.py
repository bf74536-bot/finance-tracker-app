from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI(title="Finance Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExpressionRequest(BaseModel):
    expression: str

@app.get("/")
def read_root():
    return {"message": "Python Finance Tracker API is online!"}

@app.post("/api/calculate")
def calculate_expression(request: ExpressionRequest):
    # Only allow safe mathematical characters
    clean_expr = re.sub(r'[^0-9+\-*/.]', '', request.expression)
    
    if not clean_expr:
        raise HTTPException(status_code=400, detail="Invalid input.")
        
    try:
        # Calculate the mathematical result safely
        result = eval(clean_expr, {"__builtins__": None}, {})
        return {"result": float(result)}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    except Exception:
        raise HTTPException(status_code=400, detail="Calculation error.")
