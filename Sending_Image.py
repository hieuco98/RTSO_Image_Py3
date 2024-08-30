import requests
from datetime import datetime
from PIL import Image

def send_image(image_url):
    # Địa chỉ URL của luồng RTSP
    #rtsp_url = "rtsp://admin:Thanghm1@10.1.90.112:554/Streaming/Channels/101"

    # Mở luồng RTSP
    url = 'https://eznote.vn/AgriNoteAPIs/iot/testsendingpicture'

# Mở file ảnh ở chế độ đọc nhị phân
    #img = Image.open(image_url)
    with open(image_url, 'rb') as img_file:
    # Tạo một dictionary chứa file để gửi đi
     files = {'file': img_file}
     data = {'object_process_id': 2777}  # Các thông số bổ sung (nếu có)
    # Gửi yêu cầu POST tới API với file ảnh
     response = requests.post(url, files=files,data=data)

# Kiểm tra kết quả trả về
    if response.status_code == 200:
     print('Upload thành công!')
     print(response.json())  # Nếu API trả về JSON
    else:
     print('Upload thất bại!')
     print(response.status_code)
     print(response.text)
