import streamlit as st
import sqlite3

# 1. Initialize SQLite Database
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

# 2. Build the User Interface
st.title("Industrial Finance Tracker")

st.subheader("Add New Transaction")
trans_type = st.selectbox("Type", ["Income", "Expense"])
item = st.text_input("Item Name")
amount = st.number_input("Amount", min_value=0.01, step=0.01)
category = st.text_input("Category")

if st.button("Save Transaction"):
    if item and category:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transactions (type, item, amount, category) VALUES (?, ?, ?, ?)",
            (trans_type, item, amount, category)
        )
        conn.commit()
        conn.close()
        st.success("Transaction saved successfully!")
    else:
        st.error("Please fill out all fields.")
