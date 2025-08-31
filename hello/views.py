from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
import socket

def index(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    html = f"""
    <html>
        <head>
            <title>Hello from Django on Kubernetes</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    color: white;
                    margin-top: 100px;
                }}
                h1 {{
                    font-size: 50px;
                    margin-bottom: 20px;
                }}
                p {{
                    font-size: 20px;
                }}
                .box {{
                    background: rgba(0,0,0,0.3);
                    display: inline-block;
                    padding: 20px 40px;
                    border-radius: 15px;
                    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
                }}
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🚀 Hello from Django on Kubernetes!</h1>
                <p>Current server time: <b>{current_time}</b></p>
                <p>Served by Pod: <b>{hostname}</b></p>
                <p>This app is running inside a container, deployed on Kubernetes ✨</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)
