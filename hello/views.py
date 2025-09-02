from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import socket
import os
import platform

def index(request):
    """Enhanced index view with comprehensive environment information"""
    current_time = datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S")
    hostname = socket.gethostname()
    django_env = os.getenv('DJANGO_ENV', 'development')
    namespace = os.getenv('KUBERNETES_NAMESPACE', 'default')
    
    html = f"""
    <html>
        <head>
            <title>Django Hello World - Environment Enhanced</title>
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
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🌟 Welcome to Django Hello World!</h1>
                <p>Current time: <b>{current_time}</b></p>
                <p>Pod Name: <b>{hostname}</b></p>
                <div class="env-info">
                    <p>Environment: <b>{django_env}</b></p>
                    <p>Namespace: <b>{namespace}</b></p>
                    <p>OS: <b>{platform.system()}</b></p>
                    <p>Python: <b>{platform.python_version()}</b></p>
                </div>
                <p>Running on Kubernetes with style! ✨</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)

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