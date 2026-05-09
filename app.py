from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import torch
import os

# Import the existing ML components without modifying them
from casestudy import load_model, predict_single, DEVICE
from utils import ESMEmbedder

app = FastAPI(title="SE3-PROTACs UI")

# Mount the static directory to serve HTML, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Global variables to hold the loaded model and embedder
# so they are not reloaded on every request
model = None
esm = None

class PredictionRequest(BaseModel):
    ligase_smi: str
    ligase_fa: str
    target_smi: str
    target_fa: str
    linker_smi: str

@app.on_event("startup")
def load_ml_components():
    global model, esm
    print("Loading SE3-PROTACs Model and ESM Embedder...")
    try:
        model = load_model()
        esm = ESMEmbedder(device=str(DEVICE))
        print("Model and Embedder loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")

@app.get("/")
def read_root():
    # Serve the frontend index.html
    return FileResponse("static/index.html")

@app.post("/predict")
def predict(req: PredictionRequest):
    global model, esm
    if model is None or esm is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Check server logs.")

    try:
        # predict_single takes: (model, ligase_smi, ligase_seq, target_smi, target_seq, linker_smi, esm)
        pred, score = predict_single(
            model,
            req.ligase_smi,
            req.ligase_fa,
            req.target_smi,
            req.target_fa,
            req.linker_smi,
            esm
        )
        return {"prediction": pred, "score": score}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
