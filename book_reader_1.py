from pyzbar.pyzbar import decode
import cv2

cap = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (0, 154, 87)

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        d = decode(frame)
        if d:
            for barcode in d:
                barcodeData = barcode.data.decode('utf-8')

            # if barcodeData not in barcodes:
            #     barcodes.append(barcodeData)
            #     winsound.Beep(2000, 50)
            #     font_color = (0, 0, 255)
            #     with open(BUF_FILE_PATH, mode='a') as buf:
            #         buf.write(barcodeData + '\n')
            # else:
            #     font_color = (0, 154, 87)

                x, y, w, h = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), font_color, 2)
                frame = cv2.putText(frame, barcodeData, (x, y - 10),
                                    font, .5, font_color, 2, cv2.LINE_AA)

        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

