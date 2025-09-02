from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import socket
import os

def index(request):
    """Enhanced index view with more server information"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    python_version = f"{os.sys.version.split()[0]}"
    pod_ip = os.getenv('POD_IP', 'localhost')
    
    html = f"""
    <html>
        <head>
            <title>Hello from Django on Kubernetes - Enhanced</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    color: white;
                    margin-top: 80px;
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
                    padding: 30px 50px;
                    border-radius: 15px;
                    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
                }}
                .server-info {{
                    background: rgba(255,255,255,0.1);
                    padding: 15px;
                    border-radius: 8px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🚀 Hello from Django on Kubernetes!</h1>
                <p>Current server time: <b>{current_time}</b></p>
                <p>Served by Pod: <b>{hostname}</b></p>
                <div class="server-info">
                    <p>Python Version: <b>{python_version}</b></p>
                    <p>Pod IP: <b>{pod_ip}</b></p>
                    <p>Health Status: <b>✅ Healthy</b></p>
                </div>
                <p>This app is running inside a container, deployed on Kubernetes ✨</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)

def health(request):
    """Health check endpoint for Kubernetes probes"""
    return JsonResponse({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'hostname': socket.gethostname()
    })

def readiness(request):
    """Readiness probe endpoint"""
    return HttpResponse('OK', status=200)