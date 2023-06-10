import cv2
from pyzbar import pyzbar

# Initialize the USB camera
cap = cv2.VideoCapture(1)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        continue

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the grayscale image
    qr_codes = pyzbar.decode(gray)

    # Loop over the detected QR codes
    for qr_code in qr_codes:
        # Extract the bounding box location of the QR code
        x, y, w, h = qr_code.rect

        # Draw a rectangle around the QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract the data from the QR code
        qr_data = qr_code.data.decode("utf-8")

        # Print the data
        print("QR Code:", qr_data)

    # Display the frame with detected QR codes
    cv2.imshow("QR Code Reader", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
