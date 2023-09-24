import cv2

def main():
    # Khởi tạo đối tượng VideoCapture để mở camera
    cap = cv2.VideoCapture(0)  # Số 0 tương ứng với camera mặc định

    # Kiểm tra xem camera có được mở thành công hay không
    if not cap.isOpened():
        print("Không thể mở camera.")
        return

    # Lặp để đọc và hiển thị hình ảnh từ camera
    while True:
        ret, frame = cap.read()  # Đọc frame từ camera

        # Kiểm tra xem frame có được đọc thành công hay không
        if not ret:
            print("Không thể đọc frame.")
            break

        # Hiển thị frame
        cv2.imshow('Camera', frame)

        # Đợi một khoảng thời gian và kiểm tra nút bấm 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng camera và đóng cửa sổ hiển thị
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
