def onMouse(event, x, y, flags, param):
    global title, pt
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        pt = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(image, pt, (x, y), (192, 0, 0), 2)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            temp_image = image.copy()
            pt2 = (x, y)
            cv2.rectangle(temp_image, pt, pt2, (192, 192, 192), 2)
            cv2.imshow(title, temp_image)
        elif flags & cv2.EVENT_FLAG_RBUTTON:
            temp_image = image.copy()
            dx, dy = pt[0] - x, pt[1] - y
            radius = int(np.sqrt(dx*dx + dy*dy))
            cv2.circle(temp_image, pt, radius, (192, 192, 192), 2)
            cv2.imshow(title, temp_image)
    elif event == cv2.EVENT_RBUTTONUP:
        dx, dy = pt[0] - x, pt[1] - y
        radius = int(np.sqrt(dx*dx + dy*dy))
        cv2.circle(image, pt, radius, (0, 0, 192), 2)
        cv2.imshow(title, image)