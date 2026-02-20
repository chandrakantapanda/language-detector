from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from langdetect import detect, DetectorFactory, LangDetectException

DetectorFactory.seed = 0

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Language code mapping
LANGUAGE_MAP = {
    "hi": "Hindi",
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "ta": "Tamil",
    "te": "Telugu",
    "zh-cn": "Chinese",
    "ja": "Japanese"
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/detect")
async def detect_language(data: dict):
    text = data.get("text")
    if not text:
        return JSONResponse({
            "success": False,
            "message": "Please enter some text"
        })
    try:
        code = detect(text)
        if not code:
            raise Exception("No detection")
        print(code)
        # return
        language = LANGUAGE_MAP.get(code, "Unknown")
        return JSONResponse({
             "success": True,
            "language": language,
            "code": code
        })
    except:
        return JSONResponse({
             "success": False,
            "language": "Could not detect",
            "code": None
        })
