# IoT - Image Detection & Graphic Interface
---

> According to author's requirement, some private information (like ip address, file path, etc.) is not shown in this source code.
---

## 1. Introduction of file architecture
```plaintext
|--template (template images and videos)
|--save_images (realtime images saved by detect process)
|--src
    |--detect.py (main yolo detect process)
    |--gradio.py (graphic interface[server])
    |--api.py    (api interface[server])
|--weights
    |--yolov8n.pt (yolo pretrained weights)
    |--t24_best.pt
    |--v8_170best.pt
|--RTSP-cam
    |--main.cpp (code for esp-cam board)
    |--platformio.ini
|--Readme.md
|--requirements.txt
```
---

## 2. Deployment
### 2.1. Python(Conda) Environment
You can use the following command to create a new environment:
```bash
conda create -n <env_name> python=3.9
conda activate <env_name>
```
Then, you can use the following command to install the required packages:

```bash
pip install -r requirements.txt
```

**requirements.txt**

You can feel free to comment some packages if you don't need.

```plaintext
# requirements
# Usage: pip install -r requirements.txt

# Base ----------------------------------------
ultralytics==8.0.195

# YOLO with GPU -------------------------------
# replace torch and torchvision with needed versions:
# see more in torch website: https://pytorch.org/get-started/locally/

# torch~=2.1.0.dev20230624+cu121
# torchvision~=0.16.0.dev20230625+cu121

# Server with gradio --------------------------
gradio==3.47.1

# Server with FastAPI -------------------------
fastapi==0.103.2
uvicorn>=0.15.0

# Mysql ---------------------------------------
mysql-connector-python==8.1.0
```
### 2.2 ffmpeg
You can download ffmpeg from [here](https://ffmpeg.org/download.html) and copy the exec to src.

### 2.3 RTSP-cam(esp-32-cam)
use [platformio](https://platformio.org/) to compile and upload the `RTSP-cam/main.cpp` to esp-32-cam.