import cv2

def draw_label(frame, region, text, color=(0, 255, 0)):
    x, y, w, h = region
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    cv2.putText(frame, text, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
