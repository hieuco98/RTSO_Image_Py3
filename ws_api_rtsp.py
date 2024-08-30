from flask import Flask, jsonify, request, send_file
from Capture_Image import get_image_rtsp
# Khởi tạo Flask app
app = Flask(__name__)

# Dữ liệu mẫu
data = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is item 2'},
]


@app.route('/rtspgetimage', methods=['GET'])
def get_image():
    try:
        #Bóc tách json data
        new_item = request.get_json()
        rtsp_url = "rtsp://"+new_item["rtsp_user"]+":"+new_item["rtsp_pass"]+"@"+new_item["rtsp_ip_port"]+"/rtspgetimage"

        # Lấy tên file ảnh đã lưu trong ổ cứng
        ret_code, ret_string = get_image_rtsp(rtsp_url)

        if (ret_code == 1):
            # Đường dẫn tới ảnh
            image_path = f"./{ret_string}"
            # Trả về file ảnh
            return send_file(image_path, mimetype='image/jpeg')
        else:
            return jsonify({'error': ret_string}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    updates = request.get_json()
    item.update(updates)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
