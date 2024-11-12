from django.shortcuts import render
import subprocess
import os
import datetime
import getpass 

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def htop(request):
    name = "Chaitra Adiga"
    try:
        username = getpass.getuser()
    except Exception as e: # Handle any potential exceptions
        username = "unknown"
    server_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M:%S %Z')  # IST
    try:
        top_output = subprocess.check_output(['top', '-bn1'], text=True).strip()
    except FileNotFoundError:
        top_output = "top command not found"
    except Exception as e:
        top_output = str(e)

    context = {
        'name': name,
        'username': username,
        'server_time': server_time,
        'top_output': top_output,
    }
    return render(request, 'htop.html', context)
