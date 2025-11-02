@echo off
echo ================================================
echo Installing Flask-SocketIO Dependencies
echo ================================================
echo.

pip install flask-socketio==5.3.6
pip install python-socketio==5.11.0
pip install eventlet==0.33.3

echo.
echo ================================================
echo Dependencies installed successfully!
echo ================================================
echo.
echo Next steps:
echo 1. Run the chat_schema.sql in Oracle SQL Developer or SQLPlus
echo 2. Start the application with: python app.py
echo 3. Access chat at: http://localhost:5000/chat
echo.
pause
