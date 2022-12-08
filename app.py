from fastapi import FastAPI, File, UploadFile
import uvicorn
import pandas as pd
import pickle

app = FastAPI()
MODEL_PATH = "model/rfc.pkl"

# Load model that we have trained
with open(MODEL_PATH, "rb") as file:
    rfc = pickle.load(file)

# FastAPI test    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict/{variance,skewness,curtosis,entropy}")
def predict(variance: float, skewness:float, curtosis:float, entropy:float):
    labels = [variance, skewness, curtosis, entropy]
    features = [[variance, skewness, curtosis, entropy]]
    to_predict = pd.DataFrame(features, columns=labels)
    prediction = rfc.predict(to_predict)
    return {"predicted value": int(prediction)}

@app.post("/predict_file")
async def predict_file(file:UploadFile=File(...)):
    dataframe = pd.read_csv(file.file)
    prediction = rfc.predict(dataframe)
    return {"prediction": str(prediction)}

if __name__ == "__main__":
    # you can run by using uvicorn app:app --reload or python app.py
    uvicorn.run(app, host="0.0.0.0", port=8000)