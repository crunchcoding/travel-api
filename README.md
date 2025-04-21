# 🌍 Travel Destination API

A simple backend API built with FastAPI to store and retrieve travel destinations by country, name, or season.

## 🚀 Features
- Add new travel destinations
- Retrieve all destinations
- Search destinations by name
- Data stored in SQLite using SQLAlchemy ORM
- Fully documented with Swagger UI

## Operations

- **GET** `/destinations` - Get a list of all destinations.
- **GET** `/destinations/{id}` - Get a single destination by ID.
- **POST** `/destinations` - Add a new destination.
- **PUT** `/destinations/{id}` - Update an existing destination.
- **DELETE** `/destinations/{id}` - Delete a destination.

## 🧠 Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

## 📦 Installation

```bash
git clone https://github.com/crunch-coding/travel-api.git
cd travel-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload



