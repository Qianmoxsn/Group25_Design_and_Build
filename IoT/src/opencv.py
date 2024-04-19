import subprocess as sp
import time
import os
import cv2
from ultralytics import YOLO

# Load a model
# model = YOLO()  # load a pretrained model (recommended for training)
# model = YOLO("t24_best.pt")  # load a pretrained model (recommended for training)
model = YOLO("v8_170best.pt")  # load a pretrained model (recommended for training)

## source(from camera)
# source_path = "rtsp://192.168.**:8554/mjpeg/1"
source_path = "test.mp4"

## destination(to webui)
# rtsp://localhost:8554/anno
dest_path = "rtsp://[2001:da8:**]:8554/anno"


# configration
var_conf = 0.3
show_opencv = True
push_rtsp = True
push_gradio = False

logo = """
                              ,--,                                                                                  ,---,  
                 ,----..   ,---.'|       ,----..                                                                 ,`--.' |  
                /   /   \  |   | :      /   /   \            .--.--.       ___                            ___    |   :  :  
        ,---,  /   .     : :   : |     /   .     :          /  /    '.   ,--.'|_                        ,--.'|_  '   '  ;  
       /_ ./| .   /   ;.  \|   ' :    .   /   ;.  \        |  :  /`. /   |  | :,'              __  ,-.  |  | :,' |   |  |  
 ,---, |  ' :.   ;   /  ` ;;   ; '   .   ;   /  ` ;        ;  |  |--`    :  : ' :            ,' ,'/ /|  :  : ' : '   :  ;  
/___/ \.  : |;   |  ; \ ; |'   | |__ ;   |  ; \ ; |        |  :  ;_    .;__,'  /    ,--.--.  '  | |' |.;__,'  /  |   |  '  
 .  \  \ ,' '|   :  | ; | '|   | :.'||   :  | ; | '         \  \    `. |  |   |    /       \ |  |   ,'|  |   |   '   :  |  
  \  ;  `  ,'.   |  ' ' ' :'   :    ;.   |  ' ' ' :          `----.   \:__,'| :   .--.  .-. |'  :  /  :__,'| :   ;   |  ;  
   \  \    ' '   ;  \; /  ||   |  ./ '   ;  \; /  |          __ \  \  |  '  : |__  \__\/: . .|  | '     '  : |__ `---'. |  
    '  \   |  \   \  ',  / ;   : ;    \   \  ',  /          /  /`--'  /  |  | '.'| ," .--.; |;  : |     |  | '.'| `--..`;  
     \  ;  ;   ;   :    /  |   ,/      ;   :    /          '--'.     /   ;  :    ;/  /  ,.  ||  , ;     ;  :    ;.--,_     
      :  \  \   \   \ .'   '---'        \   \ .'             `--'---'    |  ,   /;  :   .'   \---'      |  ,   / |    |`.  
       \  ' ;    `---`                   `---`                            ---`-' |  ,     .-./           ---`-'  `-- -`, ; 
        `--`                                                                      `--`---'                         '---`"  
"""

print(logo)


cap = cv2.VideoCapture(source_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) % 100
sizeStr = str(width) + "x" + str(height)

command = [
    'ffmpeg',
    # 're',#
    '-y', # 无需询问即可覆盖输出文件
    '-f', 'rawvideo',  # 强制输入或输出文件格式
    '-vcodec', 'rawvideo',  # 设置视频编解码器。这是-codec:v的别名
    '-pix_fmt', 'bgr24',  # 设置像素格式
    '-s', sizeStr,  # 设置图像大小
    '-r', '24',  # 设置帧率
    '-i', '-',  # 输入
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'ultrafast',
    '-f', 'rtsp',  # 强制输入或输出文件格式
    dest_path]

pipe = sp.Popen(command, shell=False, stdin=sp.PIPE)

print("CAP: ", end="")
print(cap.isOpened())

# clear images in "/save_images"
dir = "/**/save_images/"
if os.path.exists(dir):
    for file in os.listdir(dir):
        os.remove(dir + file)


# Loop through the video frames
time_last = 0
time_space = 3
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    time_now = time.time()
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, conf=var_conf)
        # print(results.keys())

        if time_now - time_last > time_space:
            # save frame to /images
            cv2.imwrite("save_images/" + str(time_now) + ".jpg", frame)
            time_last = time_now

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        annotated_frame_str = annotated_frame.tobytes()
        # Display the annotated frame
        if show_opencv:
            cv2.imshow("YOLOv8 Inference", annotated_frame)
        # Push the annotated frame to the output stream
        if push_rtsp:
            pipe.stdin.write(annotated_frame_str)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
pipe.terminate()
