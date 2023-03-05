#Simple Async HTTP server 
# Requires: Flask, asgiref(for async-flask), asyncio

from flask import Flask, request, jsonify
import asyncio
from datetime import datetime

app = Flask(__name__)

@app.route('/dummy_api/', methods=['GET'])
async def root():
    start_time=datetime.now()
    title = request.args['title']
    time = int(request.args['time'])
    await asyncio.sleep(time)
    payload={
        'time_stamp': str(datetime.now()),
        'title': title,
        'processing_time':str(datetime.now()-start_time)
    }
    return jsonify(payload)

if __name__ == '__main__':
    app.run()