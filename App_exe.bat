@echo off
echo Starting Semantic Search Engine...

REM Start Redis
start cmd /k "cd /d C:\Users\USER && redis-server"

REM Start Ollama
start cmd /k "ollama serve"


REM Start Django Backend
start cmd /k "cd /d %cd%\backend && python manage.py runserver"

REM Start Streamlit UI
start cmd /k "cd /d %cd% \ui && streamlit run app.py"

echo All services are starting...
pause