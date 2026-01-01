import cv2

face_ref = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

if face_ref.empty():
    print("❌ Gagal load model deteksi wajah.")
    exit()
else:
    print("✅ face_ref.xml berhasil dimuat!")

def face_detection(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_ref.detectMultiScale(
        optimized_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )
    return faces

def drawer_box(frame):
    for x, y, w, h in face_detection(frame):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(frame, "Face Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def close_window():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)  # <-- supaya nggak mirror
        drawer_box(frame)
        cv2.imshow("Coba_kode_yt", frame)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    close_window()

if __name__ == '__main__':
    main()
