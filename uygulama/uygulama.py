import cv2
import numpy as np
def hsv_degistir(value):
    hsv[..., 0] = value
    guncelresim = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("Resim", guncelresim)
def hsl_degistir(value):
    hsl[..., 2] = value
    guncelresim = cv2.cvtColor(hsl, cv2.COLOR_HLS2BGR)
    cv2.imshow("Resim", guncelresim)
def tiklama_olayi(olay, x, y, flags, param):
    if olay == cv2.EVENT_LBUTTONDOWN:
        hsv_piksel = hsv[y, x]
        hsl_piksel = hsl[y, x]
        hsv_metin = f"HSV: {hsv_piksel[0]}, {hsv_piksel[1]}, {hsv_piksel[2]}"
        hsl_metin = f"HSL: {hsl_piksel[0]}, {hsl_piksel[1]}, {hsl_piksel[2]}"
        cv2.putText(resim, hsv_metin, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(resim, hsl_metin, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow("Resim", resim)
resim = cv2.imread('kemalsunal.png')
cv2.imshow("Resim", resim)
hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
hsl = cv2.cvtColor(resim, cv2.COLOR_BGR2HLS)
cv2.setMouseCallback('Resim', tiklama_olayi)
cv2.createTrackbar("HSV :", "Resim", 0, 179, hsv_degistir)
cv2.createTrackbar("HSL :", "Resim", 0, 255, hsl_degistir)
cv2.waitKey(0)
cv2.destroyAllWindows()
