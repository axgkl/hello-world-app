#!/usr/bin/env python3
"""
Simple Hello World Flask application
"""

from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(
        {
            'message': 'Hello, World!',
            'timestamp': datetime.datetime.now().isoformat(),
            'version': os.getenv('APP_VERSION', '1.0.0'),
            'foo': os.getenv('APP_VERSION', '1.0.0'),
            'hostname': os.getenv('HOSTNAME', 'unknown'),
        }
    )


@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
