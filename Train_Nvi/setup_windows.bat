@echo off
setlocal
cd /d "%~dp0"

py -3.11 -m venv .venv
call .venv\Scripts\activate

python -m pip install -U pip
pip install -r requirements.txt

python check_env.py
pause
