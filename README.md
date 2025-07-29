# MAD2_Vehicle_Parking_App
It is a multi-user app (one requires an administrator and other users) that manages different parking lots, parking spots and parked vehicles. Assume that this parking app is for 4-wheeler parking.

## ⚙️ Prerequisites

Ensure the following are installed:

- **Python 3.9+**
- **Node.js 16+**
- **Redis** 
- **Git**

## ✅ Backend Setup (Flask + Celery)

### 1. Navigate to the backend folder

bash
cd backend
### 2. Create and activate a virtual environment
bash
python -m venv venv
source venv/bin/activate         
### 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
### 4. Start the Flask server
bash
Copy
Edit
python app.py
The API will run on: http://localhost:5000
### 5. ⏱️ Start Celery Worker
In a separate terminal:
cd backend
source venv/bin/activate 
celery -A celery_worker.celery worker --loglevel=info
### 6. 🗓️ Start Celery Beat for Scheduled Tasks
In another separate terminal
cd backend
source venv/bin/activate
celery -A celery_worker.celery beat --loglevel=info

## 🌐 Frontend Setup (Vue.js)
### 1. Navigate to frontend folder
cd frontend
### 2. Install Node.js dependencies
npm install
### 3. Start the development server
npm run dev
The frontend will run at: http://localhost:5173
