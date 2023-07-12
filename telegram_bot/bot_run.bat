@echo off

call %~dp0telegram_bot/venv/bin/activate

cd %~dp0telegram_bot

set TOKEN=5935424823:AAEQYLYpI-xEF5JqtTgUvC71VUhzu865w3I

python bot_telegram.py

pause
