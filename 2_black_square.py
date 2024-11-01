import cv2
cap = cv2.VideoCapture(0)
'''
list_example = [0, 1, 2 ,3 ]
print(list_example[1:3])S

exit()
'''
square_lentgh = 100
while True:
    ret, frame = cap.read()
    print(frame.shape)
    height , width, _ = frame.shape

    frame[:square_lentgh, :square_lentgh] = [0, 0, 0]
    frame[height - square_lentgh:, width -square_lentgh:] = [0, 0, 0]
    frame[:square_lentgh:, width - square_lentgh:] = [0, 0, 0]
    frame[height - square_lentgh:, :square_lentgh] = [0, 0, 0]
    frame[height // 2 - square_lentgh //2: height // 2 + square_lentgh // 2, width // 2 - square_lentgh // 2: width // 2 + square_lentgh // 2] = [0,0,0]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    print(key)
    if key == ord(' '):
        break
cv2.destroyAllWindows()
cap.release()