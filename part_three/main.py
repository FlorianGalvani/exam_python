from flask import Flask, render_template
import platform 
import cpuinfo
import socket
import os
import psutil
import uuid
import re

os.environ['FLASK_APP'] = 'main.py'
os.environ['FLASK_DEBUG'] = 'True'

class FlaskApp:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/stop')
    def stop(self):
        self.app.stop()

    @app.route('/system-info')
    def system_info():
        infos = {
            'platform': platform.platform(),
            'cpu': {
                'name': cpuinfo.get_cpu_info()['brand_raw'],
                'cores': psutil.cpu_count(logical=False),
                'threads': psutil.cpu_count(logical=True),
                'maxFrequency': str(round(psutil.cpu_freq().max / 1000))+' GHz',
            },
            'ram': {
                'total': str(round(psutil.virtual_memory().total / (1024.0 **3)))+' Go',
            },
            'network': {
                'hostname': socket.gethostname(),
                'ip': socket.gethostbyname(socket.gethostname()),
                'mac': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
            },
            'os': {
                'name': os.name,
                'version': platform.version(),
            }
        }

        return render_template('system_infos.html',infos=infos)
