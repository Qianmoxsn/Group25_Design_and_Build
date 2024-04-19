import json

import mysql.connector
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from ultralytics import YOLO

app = FastAPI()

ROOT = '**/ultralytics'
# Load a model
model = YOLO(ROOT + '/ultralytics/trainresult/v8_170best.pt')  # pretrained YOLOv8n model
testimg = ROOT + '/webui/images/cube1.jpg'


def get_location(court_id, device_id):
    # 连接到MySQL数据库
    conn = mysql.connector.connect(

        host="43.143.**",  # MySQL服务器主机
        user="**",  # 用户名
        password="**",  # 密码
        database="**"  # 数据库名
    )

    # 创建一个游标对象
    cursor = conn.cursor()
    # query template
    # SELECT file_path FROM courtimages WHERE court_id = 1 AND device_id = 1 ORDER BY insert_time DESC LIMIT 1;
    query = "SELECT file_path FROM courtimages WHERE court_id = %s AND device_id = %s ORDER BY insert_time DESC LIMIT 1;"
    cursor.execute(query, (court_id, device_id))

    # 获取查询结果
    result = cursor.fetchone()
    if result:
        print("DB query got: ", end="")
        print(result)

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()
    return result


# Define a function to run inference on a list of images
def run_inference(image):
    results = model.predict(image)  # return a generator of Results objects
    json_data = json.loads(results[0].tojson())
    return JSONResponse(content=json_data)

# 配置允许的来源、允许的方法和头部，以及其他 CORS 选项
origins = [
    "http://localhost:5173",
    "http://10.21.**:5173",
    "http://10.28.**:5173",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}


# Define an endpoint to post the detection results to the web
@app.get("/detect_results")
async def detect_results(court_id: int, device_id: int):
    path = get_location(court_id, device_id)
    json_str = run_inference(path)

    # return json_str
    return json_str


@app.get("/fake_detect")
async def fake_detect():
    testimg = ROOT + '/webui/images/cube2.jpg'
    results = run_inference(testimg)  # Run inference on test images
    return JSONResponse(content=results)


# To run the FastAPI app, use the following command:
# uvicorn filename:app --reload
# For example: uvicorn webui.detectapi:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1234)
