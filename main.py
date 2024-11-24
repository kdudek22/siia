import cv2
import torch
import time
import pyautogui


model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

detection_to_key = {"Stop": "esc", "Thumbs up": "up", "Thumbs Down": "down", "Left": "left", "Right": "right"}


class KeyboardInteractor:
    def __init__(self):
        self.last_move_time: int | None = None
        self.last_move: str | None = None

    def move(self, move: str):
        if self.last_move == move and time.time() - self.last_move_time < 0.3:
            print(f"Did not perform the move {move}, too little time passed since last same move")
            return

        pyautogui.press(move)
        self.last_move_time = time.time()
        self.last_move = move
        print(f"Performed move {move}")


if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    interactor = KeyboardInteractor()

    if not cam.isOpened():
        print("Error: Camera could not be opened.")
        exit()

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Error: Unable to read frame from camera.")
            break

        results = model(frame)

        for *xyxy, conf, cls in results.xyxy[0]: # iterate over the predictions
            interactor.move(detection_to_key[model.names[int(cls)]]) # this makes the move
            x1, y1, x2, y2 = map(int, xyxy)
            label = f"{model.names[int(cls)]} {conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("", frame)

        # Break loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
