from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 全域變數：預設開啟查詢
query_open = True

# 起始與結束號碼
start_num = 0
end_num = 0

@app.route('/')
def home():
    return 'Lyminnn Calling System API'

@app.route('/status')
def get_status():
    global query_open, start_num, end_num
    if not query_open:
        return jsonify({'disabled': True})
    return jsonify({'start': start_num, 'end': end_num})

@app.route('/update', methods=['POST'])
def update_range():
    global start_num, end_num
    data = request.get_json()
    start_num = int(data.get('start', 0))
    end_num = int(data.get('end', 0))
    return jsonify({'success': True})

@app.route('/toggle_query', methods=['POST'])
def toggle_query():
    global query_open
    data = request.get_json()
    query_open = bool(data.get('open'))
    return jsonify({'success': True, 'query_open': query_open})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
