import cv2

# detect a face in an image  
def face_detect(camera_index=0, classifier_path=None, window_name= 'SHOW', frame_rate=10, stop_button='s'):
    cap = cv2.VideoCapture(camera_index)

    if classifier_path is not None:
        face_cascade = cv2.CascadeClassifier(classifier_path)

        while True:
            _, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow(window_name, img)
            if cv2.waitKey(frame_rate) & 255 == ord(stop_button):
                break
        cv2.destroyAllWindows()
        cap.release()

        
def capture_image(camera_index=0, window_name="SHOW", frame_rate=10, capture_button='c', stop_button='s'):
    cap = cv2.VideoCapture(camera_index)
    counter = 0
    while True:
        _, img = cap.read()
        cv2.imshow(window_name, img)
        if cv2.waitKey(frame_rate) & 255 == ord(capture_button):
            cv2.imwrite('image{}.png'.format(counter), img)
            counter += 1
        elif cv2.waitKey(frame_rate) & 255 == ord(stop_button):
            break
