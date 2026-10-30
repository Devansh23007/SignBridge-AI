
import cv2

def main():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Could not access webcam.")
        return

    print("SignBridge AI webcam test started.")
    print("Press Q to exit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("ERROR: Could not read webcam frame.")
            break

        # Flip image for mirror-like webcam display
        frame = cv2.flip(frame, 1)

        cv2.putText(
            frame,
            "SignBridge AI - Webcam Test",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imshow("SignBridge AI", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    print("Webcam test completed.")

if __name__ == "__main__":
    main()
