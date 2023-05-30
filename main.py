import win32gui, win32con, win32ui
import numpy as np
import cv2 as cv

def screenImg():
    w = 330 #Minimap width
    h = 316 #Minimap height
    
    hwnd = win32gui.FindWindow(None, 'winnable')

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (1570, 740), win32con.SRCCOPY) #(1570, 740) = top left corner of minimap

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (h,w,4)


    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    img = img[...,:3]
    img = np.array(img)
    return img


while True:
    image = cv.resize(screenImg(),(330*3,316*3)) #Resize minimap to 3x size
    cv.imshow('Minimap', image)
    cv.waitKey(1)
