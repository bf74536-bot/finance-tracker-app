# 💰 Industrial Finance Tracker API (FastAPI & SQLite)

A professional backend REST API built with Python to handle multi-user personal finance records, log variable income streams, and calculate real-time analytics using a persistent SQL database structure.

## 📊 Application Architecture
- **Persistent Data Store:** Engineered using structured relational tables in **SQLite** via formal SQL parameters (`CREATE TABLE`, `INSERT INTO`).
- **RESTful Endpoints:** Fully functioning network interface endpoints to handle secure client-side communication over the web.
- **Input Validation System:** Implemented strict data typing validation schemas using **Pydantic** models to catch malformed payloads instantly.

## 🛠️ Tech Stack & Core Engines
- **Language Core:** Python 3
- **Web Server Framework:** FastAPI / Uvicorn
- **Database Engine:** SQLite3 (Native Relational Database Engine)
- **Data Validation Layer:** Pydantic

## 🚀 API Endpoints Matrix
- `GET /` - Check web service status and confirm live database connectivity.
- `POST /api/transactions` - Securely saves a new Income or Expense record directly into the SQL relational engine.
- `GET /api/transactions` - Reads and returns the complete list of saved cash flow transaction profiles.

## ⚙️ How to Download and Run Locally

1. Clone this repository onto your terminal workspace:
   ```bash
   git clone https://github.com
   ```
2. Navigate into your project working environment directory:
   ```bash
   cd finance-tracker-app
   ```
3. Install the industry web server packages:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
4. Boot up your live backend database application server routine:
   ```bash
   uvicorn app:app --reload --port 5000
   ```
