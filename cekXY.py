import cv2
from datetime import datetime

# Variabel untuk menyimpan posisi mouse
mouse_x, mouse_y = -1, -1

def Capture_Event(event, x, y, flags, params):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        # Update posisi mouse
        mouse_x, mouse_y = x, y
        # Print koordinat mouse secara live
        print(f"Dimana? (x,y): ({mouse_x}, {mouse_y})")
        
    elif event == cv2.EVENT_LBUTTONDOWN:
        # Ambil tanggal dan waktu lokal
        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M")

        # Print koordinat dan waktu klik
        print(f"Clicked at: ({x}, {y}) | {current_time}")
        
        # Simpan koordinat dan waktu ke file
        with open('XY/xy.txt', 'a') as f:
            f.write(f"Clicked at: ({x}, {y}) | {current_time}\n")
        
        print(f"Tersimpan cuy: ({x}, {y}) | {current_time} to xy.txt")

if __name__ == "__main__":
    # Baca gambar
    img = cv2.imread('assets/1.jpeg', 1)
    
    while True:
        img_copy = img.copy()
        
        if mouse_x != -1 and mouse_y != -1:
            cv2.circle(img_copy, (mouse_x, mouse_y), 10, (0, 255, 255), -1) 
        
        cv2.imshow('image', img_copy)
        
        # Set Mouse Callback function
        cv2.setMouseCallback('image', Capture_Event)

        # Tunggu 1ms untuk deteksi key press
        key = cv2.waitKey(1)
        if key == 27:  # Jika tombol 'esc' ditekan
            break

    cv2.destroyAllWindows()
