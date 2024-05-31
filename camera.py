import cv2
import os

# Create the "frames" folder if it doesn't exist
if not os.path.exists("frames"):
    os.mkdir("frames")

# Open video file (replace with your video path)
cap = cv2.VideoCapture("IMG_0667.mp4")

# Or use camera (replace 0 with camera index if you have multiple)
# cap = cv2.VideoCapture(0)

# Frame counter
count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Save frame as PNG image
    filename = f"frames/frame_{count:04d}.png"  # Pad with zeros (e.g., frame_0001.png)
    cv2.imwrite(filename, frame)

    count += 1

cap.release()
cv2.destroyAllWindows()
