import cv2
from datetime import datetime
def get_image_rtsp(rtsp_url):
    # Địa chỉ URL của luồng RTSP
    #rtsp_url = "rtsp://admin:Thanghm1@10.1.90.112:554/Streaming/Channels/101"

    # Mở luồng RTSP
    cap = cv2.VideoCapture(rtsp_url)

    # Kiểm tra xem luồng có mở thành công hay không
    if not cap.isOpened():
        print("Lỗi: Không thể mở luồng RTSP.")
        ret_string = "Lỗi: Không thể mở luồng RTSP."
        ret_code = 0
    else:
        # Chụp một khung hình từ luồng
        ret, frame = cap.read()

        if ret:
            # Lưu khung hình dưới dạng tệp ảnh
            now = datetime.now()
            ret_string = f"{now.microsecond}.jpg"
            cv2.imwrite(ret_string, frame)
            print("Đã chụp và lưu ảnh thành công.")

            ret_code = 1
        else:
            print("Lỗi: Không thể đọc khung hình.")
            ret_string = "Lỗi: Không thể đọc khung hình."
            ret_code = 2

    # Giải phóng bộ nhớ
    cap.release()
    return ret_code,ret_string
