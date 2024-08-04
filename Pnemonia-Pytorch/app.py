from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse 
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pneumonia.components.model_trainer import Net
from PIL import Image
import shutil
import os
import io 
import joblib 
import torch 
import numpy as np
import pickle 

PREDICTION_LABEL: dict = {0: "NORMAL", 1: "PNEUMONIA"} 

model = Net()

train_transforms_obj = joblib.load("models/train_transforms.pkl")

app = FastAPI()

os.makedirs("static", exist_ok=True) 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_image(request:Request, file: UploadFile = File(...)):
    with open(f"static/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename} 

@app.post("/predict/")
async def predict_image(request: Request, file: UploadFile = File(...)):
    with Image.open(f"static/{file.filename}") as img:
        b = io.BytesIO()
        img.save(b, format="JPEG")
        im_bytes = b.getvalue() 
        image = Image.open(io.BytesIO(im_bytes)).convert("RGB")
        with open("models/train_transforms.pkl", "rb") as f:
            my_transforms = pickle.load(f)
        image = torch.from_numpy(np.array(my_transforms(image).unsqueeze(0)))
        image = image.reshape(1, 3, 224, 224) 
        model = torch.load("models/trained_model.pt")
        model.eval()  
        image_tensor = torch.tensor(image, dtype=torch.float32) 
        with torch.no_grad():
            output = model(image_tensor)
        prediction_index = torch.argmax(output, dim=1).item()   

        pred = PREDICTION_LABEL[prediction_index]  

    return JSONResponse({"prediction": pred})  
    # return templates.TemplateResponse("index.html", {"request": request, "status": pred})     

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="localhost", port=8000)
