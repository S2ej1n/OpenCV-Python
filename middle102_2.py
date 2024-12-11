import numpy as np, cv2
background_img = cv2.imread("background.jpg",cv2.IMREAD_COLOR)
logo = cv2.imread("logo.jpg",cv2.IMREAD_COLOR)

title = "mid1022"
font = cv2.FONT_HERSHEY_PLAIN

def onMouse(event, x, y, flags, g):
    count=0
    if event == cv2.EVENT_LBUTTONDOWN:
        mask = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
        masks = cv2.split(mask)
        fg_mask = cv2.bitwise_or(masks[0], masks[1])
        fg_mask = cv2.bitwise_or(masks[2], fg_mask)
        bg_mask = cv2.bitwise_not(fg_mask)
        (H, W), (h, w) = background_img.shape[:2], logo.shape[:2]
        x, y = (H - h) // 2, (W - w) // 2
        roi = background_img[x:x + h, y:y + w]
        newlogo = cv2.bitwise_and(logo, logo, mask=fg_mask)
        newback = cv2.bitwise_and(roi, roi, mask=bg_mask)
        dst = cv2.add(newlogo, newback)
        background_img[x:x + h, y:y + w] = dst
        cv2.imshow(title, background_img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        count = count + 1
        cv2.rectangle(background_img,(x,y),(x+30,y+30),(255,0,0),2)
        cv2.putText(background_img, str(count), (10+count*10, 330), font, 2, (255, 0, 0))
        cv2.imshow(title, background_img)

cv2.imshow(title,background_img)
cv2.setMouseCallback(title,onMouse)
cv2.waitKey()
cv2.destroyAllWindows()