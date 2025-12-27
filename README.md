# Smart Site Task Manager

Smart Site Task Manager is a production-ready task management backend built with **FastAPI**.  
It automatically classifies, prioritizes, and tracks tasks while maintaining a complete audit history.  
The system is designed with clean architecture principles and is frontend-ready for a Flutter mobile application.

---

## 🚀 Tech Stack

- FastAPI
- SQLAlchemy (ORM)
- SQLite (development)
- PostgreSQL (production-ready)
- Pydantic (data validation)
- Uvicorn (ASGI server)

---

## ✨ Features

- Create tasks with intelligent rule-based classification
- Automatic priority detection
- Read tasks with pagination and filtering
- Update tasks using PATCH (partial updates)
- Full task history tracking (audit log)
- Clean REST APIs with Swagger / OpenAPI documentation
- Frontend-ready API design (Flutter compatible)

---

## 🏗️ Project Structure

app/
├── main.py # Application entry point
├── database.py # Database connection and session handling
├── config.py # Environment and configuration settings
├── models/ # SQLAlchemy database models
├── schemas/ # Pydantic request/response schemas
├── routers/ # API route definitions
└── services/ # Business logic and task processing




---

## ▶️ How to Run Locally

### 1️⃣ Create virtual environment
```bash
python -m venv venv


---

## ▶️ How to Run Locally

### 1️⃣ Create virtual environment
```bash
python -m venv venv

2️⃣ Activate virtual environment
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the server
python -m uvicorn app.main:app --reload

5️⃣ Open Swagger documentation
http://127.0.0.1:8000/docs





📌 API Endpoints
➕ Create Task
POST /api/tasks

📄 Get Tasks (with pagination & filters)
GET /api/tasks?page=1&limit=5

✏️ Update Task
PATCH /api/tasks/{task_id}

🧠 Architecture Explanation.

I built a FastAPI backend using clean architecture with routers, services, models, and schemas.
Tasks are automatically classified and prioritized on creation, stored in a relational database, and all updates are tracked using a task history table for audit purposes.
The APIs support pagination, filtering, and PATCH updates, making them production-ready and frontend-friendly.


for pushihng git code 

git status
git add .
git commit -m "Complete Smart Site Task Manager backend"


👤 Author
Name    :- Chetan Nagnath Shinde
Email   :- chetanshinde2643@gmail.com
Phone No:- 9665809591
git link:- https://github.com/Chetan0521/Chetan0521
