from fastapi import FastAPI

from api.models.iris import PredictResponse, PredictRequest
from interference import load_model

model = load_model()
app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = model.predict(request.dict())
    print(PredictResponse(prediction=prediction))
    return PredictResponse(prediction=prediction)
