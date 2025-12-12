from pynput.keyboard import Controller, Key  # Import thêm Key
import time

keyboard = Controller()

print("Tool đang chạy... Đóng cửa sổ để tắt.")

while True:
    # Sử dụng Key.shift thay vì chuỗi 'shift'
    keyboard.press(Key.shift)   
    keyboard.release(Key.shift)
    
    # In ra để kiểm tra tool có hoạt động không (tùy chọn)
    print("Đã nhấn Shift")
    
    time.sleep(10)