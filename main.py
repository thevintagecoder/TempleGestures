import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1, # We only need one hand for Temple Run
    min_detection_confidence=0.7
)

# 2. Open the Webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally so it acts like a mirror
    image = cv2.flip(image, 1)
    
    # Convert color from BGR (OpenCV default) to RGB (MediaPipe needs this)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 3. Process the image to find hands
    results = hands.process(image_rgb)

    # 4. Draw the landmarks if a hand is found
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )
            
            # This is where we will eventually add our Game Logic!
            # For now, let's just print the coordinates of the index finger tip (ID 8)
            index_tip = hand_landmarks.landmark[8]
            # Coordinates are normalized (0.0 to 1.0), so we see values like 0.5 (center)
            print(f"Index Finger X: {index_tip.x}")

    # Show the window
    cv2.imshow('Temple Run Controller', image)

    # Press 'q' to quit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()