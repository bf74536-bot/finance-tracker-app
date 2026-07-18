from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI(title="Industrial Finance API Engine")

# Allow connections from mobile frontend apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize production SQL database layout
DB_FILE = "finance_vault.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            item TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Data models for input verification
class TransactionInput(BaseModel):
    type: str       # "Income" or "Expense"
    item: str
    amount: float
    category: str

class TransactionResponse(BaseModel):
    id: int
    type: str
    item: str
    amount: float
    category: str

@app.get("/")
def check_status():
    return {"status": "Online", "database": "Connected to SQLite"}

# 🚀 API Endpoint 1: Save transaction to real SQL database
@app.post("/api/transactions", response_model=TransactionResponse)
def add_transaction(tx: TransactionInput):
    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero.")
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (type, item, amount, category) VALUES (?, ?, ?, ?)",
        (tx.type, tx.item, tx.amount, tx.category)
    )
    tx_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {**tx.dict(), "id": tx_id}

# 🚀 API Endpoint 2: Read transaction list from database
@app.get("/api/transactions", response_model=List[TransactionResponse])
def get_transactions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, type, item, amount, category FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {"id": row[0], "type": row[1], "item": row[2], "amount": row[3], "category": row[4]}
        for row in rows
    ]
