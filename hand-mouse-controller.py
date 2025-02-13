import cv2
import mediapipe as mp
import pyautogui
import win32api

# Initialize Mediapipe and its utilities
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize video capture
video = cv2.VideoCapture(0)

click = 0

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()
        # Convert the frame to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)  # Flip image horizontally
        imageHeight, imageWidth, _ = image.shape

        # Process the frame
        results = hands.process(image)

        # Convert the image back to BGR for display
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:
                    normalized_landmark = hand_landmarks.landmark[point]
                    pixel_coordinates_landmark = mp_drawing._normalized_to_pixel_coordinates(
                        normalized_landmark.x, normalized_landmark.y, imageWidth, imageHeight
                    )

                    if point == mp_hands.HandLandmark.INDEX_FINGER_TIP:
                        try:
                            index_x, index_y = pixel_coordinates_landmark
                            win32api.SetCursorPos((index_x * 4, index_y * 5))
                        except:
                            pass

                    elif point == mp_hands.HandLandmark.THUMB_TIP:
                        try:
                            thumb_x, thumb_y = pixel_coordinates_landmark
                        except:
                            pass

                        # Calculate distance between thumb and index finger
                        try:
                            distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5
                            if distance < 50:  # If distance is small, perform a click
                                click += 1
                                if click % 5 == 0:
                                    pyautogui.click()
                        except:
                            pass

        # Display the image
        cv2.imshow('Hand Tracking', image)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Release resources
video.release()
cv2.destroyAllWindows()