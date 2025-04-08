@echo off
echo Installing backend dependencies...
cd backend
pip install -r requirements.txt
start python manage.py runserver

echo Installing frontend dependencies...
cd ../frontend
npm install
start npm start

echo Servers are running!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000 