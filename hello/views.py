from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import socket
import os
import platform

def index(request):
    """Enhanced index view with more server information"""
    """Enhanced index view with comprehensive environment information"""
    current_time = datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S")
    hostname = socket.gethostname()
    django_env = os.getenv('DJANGO_ENV', 'development')
    namespace = os.getenv('KUBERNETES_NAMESPACE', 'default')
    
    python_version = f"{os.sys.version.split()[0]}"
    pod_ip = os.getenv('POD_IP', 'localhost')
    
    html = f"""
    <html>
        <head>
            <title>Hello from Django on Kubernetes - Enhanced</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    text-align: center;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    margin-top: 70px;
                }}
                h1 {{
                    font-size: 55px;
                    margin-bottom: 25px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                }}
                p {{
                    font-size: 18px;
                    margin: 10px 0;
                }}
                .box {{
                    background: rgba(0,0,0,0.4);
                    display: inline-block;
                    padding: 35px 55px;
                    border-radius: 20px;
                    box-shadow: 0px 6px 25px rgba(0,0,0,0.6);
                }}
                .env-info {{
                    background: rgba(255,255,255,0.15);
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 20px;
                    border: 1px solid rgba(255,255,255,0.2);
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
                    <p>Pod Name: <b>{hostname}</b></p>
                <div class="env-info">
                    <p>Environment: <b>{django_env}</b></p>
                    <p>Namespace: <b>{namespace}</b></p>
                    <p>OS: <b>{platform.system()}</b></p>
                    <p>Python: <b>{platform.python_version()}</b></p>
                </div>
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
def api_info(request):
    """API endpoint for environment information"""
    return JsonResponse({
        'app_name': 'django-hello-k8s',
        'version': '1.0.0',
        'environment': os.getenv('DJANGO_ENV', 'development'),
        'timestamp': datetime.datetime.now().isoformat(),
        'pod_info': {
            'name': socket.gethostname(),
            'namespace': os.getenv('KUBERNETES_NAMESPACE', 'default')
        }
    })