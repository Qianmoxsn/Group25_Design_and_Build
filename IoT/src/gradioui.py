## Run this file to launch the webui
## The webui will be available at http://localhost:7860
import os

import cv2
import gradio as gr
from PIL import Image
from ultralytics import YOLO

model = YOLO("v8_170best.pt")


## The predict function(YoloV8)
def predict(input_image, confidence):
    if isinstance(input_image, str):
        # Input is a file path
        img = Image.open(input_image)
    else:
        # Input is a NumPy array
        img = Image.fromarray(input_image, mode="RGB")

    results = model.predict(img, conf=confidence)  # save plotted images

    labeled_img_rgb = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)
    labeled_img = Image.fromarray(labeled_img_rgb)

    logtext = "Speed:" + results[0].speed.__str__()

    return labeled_img, logtext


## The predict function(YoloV8)
def predict_video(input_video, confidence):
    # read the video
    video = cv2.VideoCapture(input_video)

    resolution = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    labeled_video = cv2.VideoWriter('labeled_video.mp4', fourcc, fps, resolution)
    # loop through the video
    while video.isOpened():
        # read the current frame
        ret, frame = video.read()
        # if the frame was read successfully
        if ret:
            # convert the frame to PIL Image
            img = Image.fromarray(frame, mode="RGB")
            # predict the image
            results = model.predict(img, conf=confidence)

            labeled_frame = results[0].plot()
            labeled_frame_rgb = cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB)
            # display the predictions
            # labeled_img.show()
            # generate the labeled video
            labeled_video.write(labeled_frame_rgb)
        else:
            break
    # frame per second
    video.release()
    return 'labeled_video.mp4', fps


def realtime_predict(confidence):
    video = cv2.VideoCapture(0)
    while video.isOpened():
        # read the current frame
        ret, frame = video.read()
        # if the frame was read successfully
        if ret:
            # convert the frame to PIL Image
            img = Image.fromarray(frame, mode="RGB")
            # predict the image
            results = model.predict(img, conf=confidence)

            labeled_frame = results[0].plot()
            labeled_frame_rgb = cv2.cvtColor(labeled_frame, cv2.COLOR_BGR2RGB)
            # display the predictions
            # labeled_img.show()
            # generate the labeled video
            cv2.imshow('frame', labeled_frame_rgb)
            # cv2.imshow('frame', labeled_frame)

            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    video.release()
    cv2.destroyAllWindows()


def stop_stream(grImage):
    grImage.stream = False


def start_stream(grImage):
    grImage.stream = True


# Rewrite the webui with blocking mode
with gr.Blocks() as app:
    gr.Markdown("# TREASURE DETECTION WebUI")
    gr.Markdown("## Powered by Gradio and Ultralytics")
    directory_path = '/Users/qianmoxsn/Documents/Code/yolowebui/Backend/save_images'

    # Get a list of all files in the directory with full paths
    files_list = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if
                  os.path.isfile(os.path.join(directory_path, f))]

    with gr.Tab("Img Detection(image)"):
        gr.Markdown("### This section is for single image detection")
        with gr.Row():
            with gr.Column():
                gr.Markdown("You can upload your image here or use the example image bellow.")
                inputImg = gr.Image()
                exampleImg = gr.Examples(examples=[["images/cube1.jpg"]], inputs=inputImg)
                galleryImg = gr.Examples(examples=files_list, inputs=inputImg)
                gr.Markdown("You can set the confidence here then click Run to see the result.")
                setConfi = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.25, label="Confidence")
                submit = gr.Button(label="Submit")

            with gr.Column():
                outputimg = gr.Image()
        log = gr.Textbox(lines=5, label="Log", placeholder="You may see the log here.")

        submit.click(predict, inputs=[inputImg, setConfi], outputs=[outputimg, log])

    with gr.Tab("Img Gallery"):
        gr.Markdown("### This section is for image display")
        with gr.Row():
            gr.Gallery(files_list, label="Image Gallery")
        with gr.Row():
            gr.Markdown("## You can also see these images in prev tab.")
            gr.Markdown("## And run them again to detect treasures.")
    with gr.Tab("Video Detection(stream)"):
        gr.Markdown("### This section is for a webcam object detection")
        cameraurl = gr.Textbox(lines=1, label="Camera URL", placeholder="rtsp://10.29.78.147:8554/anno")

        imagepreview = gr.Image(source='webcam', streaming=True)
        setConfi = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.25, label="Confidence")
        detect = gr.Button(label="Detect", value="Detect")
        stoppreview = gr.Button(label="Stop Preview", value="Stop Preview")
        output = gr.AnnotatedImage()
        log = gr.Textbox(lines=5, label="Log", placeholder="You may see the log here.")

# app.launch(share=True)
app.queue()
app.launch(server_name="0.0.0.0")
