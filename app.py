from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from pydantic import BaseModel
import logging

logging.getLogger("transformers").setLevel(logging.ERROR)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class InputData(BaseModel):
    prompt: str

class OutputData(BaseModel):
    response: str

model = pipeline("text-generation", model="gpt2")

@app.post("/generate", response_model=OutputData)
def generate(input_data: InputData):
    prompt = input_data.prompt
    response = model(prompt, max_length=50,
                     num_return_sequences=1)[0]["generated_text"]
    return OutputData(response=response)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# # Run the FastAPI application
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
