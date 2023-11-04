import cv2
import mediapipe as mp
import pyautogui
import math

"""
menggunakan cv2 dan hand tracking mediapipe
"""
cap = cv2.VideoCapture(0)
hands_track = mp.solutions.hands.Hands()
utils = mp.solutions.drawing_utils
"""
mendapatkan ukuran layar
"""
screen_w, screen_h = pyautogui.size()

def DetectedLandmark(id, pointX, pointY, pointZ):
    print(f"id : {id} | pointX : {pointX}, pointY : {pointY}, pointZ : {pointZ}")
    
def Distance(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))     
    
# global telapak_x, telapak_y  
def MovePointer(id, x, y, frame_w, frame_h):
    telapak_x = screen_w/frame_w*x
    telapak_y = screen_w/frame_h*y
    if id == 16:
        print(f"move to : {telapak_x} | {telapak_y}")
        pyautogui.moveTo(telapak_x, telapak_y)

def LeftClick(x:dict, y:dict,frame,frame_w, frame_h):
    global telunjuk_x, telunjuk_y, jempol_x, jempol_y
    # print(f"left-click id : {id1}, {id2}")
    """
    hitung posisi jempol 
    """
    x1 = x["x1"]   
    y1 = y["y1"]
    x_circle1 = int(x["x1"] * frame_w)
    y_circle2 = int(y["y1"] * frame_h)
       
    jempol_x = screen_w/frame_w*x1
    jempol_y = screen_w/frame_h*y1 
    cv2.circle(img=frame, center=(x_circle1, y_circle2), radius=10, color=(0,168,198))
    
    """
    hitung posisi telunjuk 
    """
    x2 = x["x2"]
    y2 = y["y2"]
    telunjuk_x = screen_w/frame_w*x2
    telunjuk_y = screen_w/frame_h*y2 
    # cv2.circle(img=frame, center=(x2, y2), radius=10, color=(0,168,198))
    
    # if cek1 == True and cek2 == True:        
    # jarak_klik = telunjuk_y - jempol_y
    jarak_klik = Distance(telunjuk_x, jempol_x,telunjuk_y, jempol_y)
    if abs(jarak_klik) < 0.3:
                pyautogui.click()
                pyautogui.sleep(1)
    else:
        pyautogui.mouseUp()            
    print(f"jarak jempol-telunjuk : {abs(jarak_klik)}")    
                

def LeftDoubleClick(x:dict, y:dict,frame,frame_w, frame_h):
    global tengah_x, tengah_y, jempol_x, jempol_y
    # print(f"left-click id : {id1}, {id2}")
    """
    hitung posisi jempol 
    """
    x1 = x["x1"]   
    y1 = y["y1"]
    x_circle1 = int(x["x1"] * frame_w)
    y_circle2 = int(y["y1"] * frame_h)
       
    jempol_x = screen_w/frame_w*x1
    jempol_y = screen_w/frame_h*y1 
    cv2.circle(img=frame, center=(x_circle1, y_circle2), radius=10, color=(0,168,198))
    
    """
    hitung posisi tengah 
    """
    x2 = x["x2"]
    y2 = y["y2"]
    tengah_x = screen_w/frame_w*x2
    tengah_y = screen_w/frame_h*y2 
    # cv2.circle(img=frame, center=(x2, y2), radius=10, color=(0,168,198))
    
    # if cek1 == True and cek2 == True:        
    # jarak_klik = tengah_y - jempol_y
    jarak_klik = Distance(tengah_x, jempol_x, tengah_y, jempol_y)
    if abs(jarak_klik) < 0.3:
                pyautogui.doubleClick()
                pyautogui.sleep(1)
    print(f"jarak jempol-tengah : {abs(jarak_klik)}")

def RightClick(x:dict, y:dict,frame,frame_w, frame_h):
    global telunjuk_x, telunjuk_y, jempol_x, jempol_y
    # print(f"left-click id : {id1}, {id2}")
    """
    hitung posisi jempol 
    """
    x1 = x["x1"]   
    y1 = y["y1"]
    x_circle1 = int(x["x1"] * frame_w)
    y_circle2 = int(y["y1"] * frame_h)
       
    jempol_x = screen_w/frame_w*x1
    jempol_y = screen_w/frame_h*y1 
    cv2.circle(img=frame, center=(x_circle1, y_circle2), radius=10, color=(0,168,198))
    
    """
    hitung posisi manis 
    """
    x2 = x["x2"]
    y2 = y["y2"]
    manis_x = screen_w/frame_w*x2
    manis_y = screen_w/frame_h*y2 
    # cv2.circle(img=frame, center=(x2, y2), radius=10, color=(0,168,198))
    
    # if cek1 == True and cek2 == True:        
    # jarak_klik = manis_y - jempol_y
    jarak_klik = Distance(manis_x, jempol_x, manis_y, jempol_y)
    
    if abs(jarak_klik) < 0.3:
                pyautogui.rightClick()
                pyautogui.sleep(1)
    print(f"jarak jempol-manis : {abs(jarak_klik)}")    

def Scroll(x:dict, y:dict,frame,frame_w, frame_h):
    global kelingking_x, kelingking_y, jempol_x, jempol_y
    # print(f"left-click id : {id1}, {id2}")
    """
    hitung posisi jempol 
    """
    x1 = x["x1"]   
    y1 = y["y1"]
    x_circle1 = int(x["x1"] * frame_w)
    y_circle2 = int(y["y1"] * frame_h)
       
    jempol_x = screen_w/frame_w*x1
    jempol_y = screen_w/frame_h*y1 
    cv2.circle(img=frame, center=(x_circle1, y_circle2), radius=10, color=(0,168,198))
    
    """
    hitung posisi kelingking 
    """
    x2 = x["x2"]
    y2 = y["y2"]
    kelingking_x = screen_w/frame_w*x2
    kelingking_y = screen_w/frame_h*y2 
    # cv2.circle(img=frame, center=(x2, y2), radius=10, color=(0,168,198))
    
    # if cek1 == True and cek2 == True:        
    # jarak_klik = kelingking_y - jempol_y
    jarak_klik = Distance(kelingking_x, jempol_x, kelingking_y, jempol_y)
    
    if abs(jarak_klik) < 0.3:
                pyautogui.vscroll(-20)
                # pyautogui.sleep(1)
    elif abs(jarak_klik) > 0.3 and abs(jarak_klik) < 0.6:
                pyautogui.vscroll(20)
                # pyautogui.sleep(1)            
    print(f"jarak jempol-kelingking : {abs(jarak_klik)}")    


while True:
    """
    frame menyimpan data image, _ menyimpan data boolean := True
    """
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    """
    menyimpan data height&width frame := 480 x 640 x3(rgb)
    """
    frame_h, frame_w, _ = frame.shape
    print(frame.shape)
    """
    konversi BGR ke RGB := agar bisa dimanipulasi
    """
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detect_hand = hands_track.process(rgb_img)
    hands = detect_hand.multi_hand_landmarks
    #untuk simpan koordinat
    #move pointer
    posisi_move = {}
    #left klik
    posisiX_click = {}
    posisiY_click = {}
    #right klik
    posisiXR_click = {}
    posisiYR_click = {}
    #double klik
    posisiX_doubleClick = {}
    posisiY_doubleClick = {}
    #scroll
    posisiX_scroll = {}
    posisiY_scroll = {}

    if hands:
        for tangan in hands:
            utils.draw_landmarks(frame, tangan) 
            landmarks = tangan.landmark
            for id, landmark in enumerate(landmarks):
                # print(f"id : {id} -> landmark : {landmark}")
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                # print(x)
                # DetectedLandmark(id, landmark.x, landmark.y, landmark.z)   
                MovePointer(id, x, y, frame_w=frame_w, frame_h=frame_h)
                    
                """
                posisi jempol
                """
                if id == 4:
                    posisiX_click["x1"] = landmark.x
                    posisiXR_click["x1"] = landmark.x
                    posisiY_click["y1"] = landmark.y
                    posisiYR_click["y1"] = landmark.y
                    posisiX_doubleClick["x1"] = landmark.x
                    posisiY_doubleClick["y1"] = landmark.y
                    posisiX_scroll["x1"] = landmark.x
                    posisiY_scroll["y1"] = landmark.y
                    
                    # print(f"id : {id} -> {landmark.x}")
                """
                posisi telunjuk
                """
                if id == 8:
                    posisiX_click["x2"] = landmark.x
                    posisiY_click["y2"] = landmark.y
                print(f"posisi X :  {posisiX_click}" )                
                print(f"posisi Y :  {posisiY_click}" )                
                
                """
                posisi jari tengah
                """
                if id == 12:
                    posisiX_doubleClick["x2"] = landmark.x
                    posisiY_doubleClick["y2"] = landmark.y
                print(f"posisi X :  {posisiX_click}" )                
                print(f"posisi Y :  {posisiY_click}" )                
                
                """
                posisi jari manis
                """
                if id == 16:
                    posisiXR_click["x2"] = landmark.x
                    posisiYR_click["y2"] = landmark.y
                print(f"posisi X :  {posisiXR_click}" )                
                print(f"posisi Y :  {posisiYR_click}" )                
                
                if id == 20:
                    posisiX_scroll["x2"] = landmark.x
                    posisiY_scroll["y2"] = landmark.y
                print(f"posisi X :  {posisiX_scroll}" )                
                print(f"posisi Y :  {posisiY_scroll}" )                
                
                if len(posisiX_click) == 2 and len(posisiY_click) == 2:    
                    LeftClick(x=posisiX_click, y=posisiY_click, frame=frame, frame_w=frame_w,frame_h=frame_h)
                    """
                    netralkan kembali posisi
                    """
                    posisiX_click = {}     
                    posisiY_click = {}   
                
                if len(posisiX_doubleClick) == 2 and len(posisiY_doubleClick) == 2:    
                    LeftDoubleClick(x=posisiX_doubleClick, y=posisiY_doubleClick, frame=frame, frame_w=frame_w,frame_h=frame_h)
                    """
                    netralkan kembali posisi
                    """
                    posisiX_doubleClick = {}     
                    posisiY_doubleClick = {}
                
                if len(posisiXR_click) == 2 and len(posisiYR_click) == 2:    
                    RightClick(x=posisiXR_click, y=posisiYR_click, frame=frame, frame_w=frame_w,frame_h=frame_h)
                    """
                    netralkan kembali posisi
                    """
                    posisiXR_click = {}     
                    posisiYR_click = {}
                
                if len(posisiX_scroll) == 2 and len(posisiY_scroll) == 2:    
                    Scroll(x=posisiX_scroll, y=posisiY_scroll, frame=frame, frame_w=frame_w,frame_h=frame_h)
                    """
                    netralkan kembali posisi
                    """
                    posisiX_scroll = {}     
                    posisiY_scroll = {}
                
                # if len(posisi_move) == 2:    
                #     MovePointer(posisi_move, frame_w=frame_w, frame_h=frame_h)                       
    else:
            cv2.imshow('Virtual Mouse', frame)
    key = cv2.waitKey(1)
    if key == ord('v'):
        break
cap.release()                   
             