cd /deploy/app/server
gunicorn -w 4 -b 0.0.0.0:8000 main:app & python worker.py