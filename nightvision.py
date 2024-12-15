import cv2
import time  # For potential delay between frames

# Define a variable to track mode
mode = "day"

# Set up image collection
video = cv2.VideoCapture(0)  # Assuming default webcam

while True:
    check, frame = video.read()

    if check:  # Check if frame was read successfully
        # Apply brightness and contrast adjustment based on mode
        if mode == "night":
            # Boost brightness and contrast drastically for night vision effect
            frame = cv2.convertScaleAbs(frame, alpha=10, beta=200)  # High contrast and brightness increase

            # Add a green tint to simulate night vision goggles (realistic green effect)
            frame[:, :, 0] = 0  # Remove the blue channel
            frame[:, :, 2] = 0  # Remove the red channel

        elif mode == "day":
            # You can leave this unchanged or adjust for daytime if needed
            frame = cv2.convertScaleAbs(frame, alpha=1, beta=-30)  # Reduce brightness in day mode for contrast

        # Display the resulting frame
        cv2.imshow("FLL Night Vision Model", frame)

        key = cv2.waitKey(1)


        # Exit when Q is pressed
        if key == ord('q'):
            break

    else:
        print("Error: Could not read frame from camera.")
        break

# Release resources
video.release()
cv2.destroyAllWindows()
