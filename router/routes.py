from fastapi import APIRouter,File, UploadFile
from pydantic import BaseModel
from service.crewai.main_crew_run import run
from service.db.db import save_to_mongo
import fitz
router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from another route!"}

class Input(BaseModel):
    topic:str
@router.post("/run")
def runner(input:Input):
    catch = run(input.topic)
    return {"message": catch}

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        doc = fitz.open(stream=await file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        save_to_mongo(text)
        return {"filename": file.filename, "text": text}
    except Exception as e:
        return {"error": str(e)}

     
