from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from inky_picture_service.model import InkyPicture


app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("inky-pic-api:app", host="localhost", port=9000)


inkyPicsDB = [
        InkyPicture(id=0, title="The Happy Cacti says hi!", uri="test/sample/cacti-hi.jpg")
    ]

@app.get("/pics/", response_model=List[InkyPicture])
async def get_all_pics():
    return inkyPicsDB

@app.get("/pics/daily")
async def get_daily_inky_pic():
    pic_path = Path("src/cacti-hi.jpg")
    if not pic_path.is_file():
        raise HTTPException(status_code=404, detail="Picture not found")
    return FileResponse(pic_path)

@app.get("/pics/{pic_id}")
async def get_inky_pics_by_id(pic_id: int):
    if inkyPicsDB.get(pic_id, None) is not None:
        print(f'Requested pic: {pic_id}')
        pic_path = Path("test/sample/cacti-hi.jpg")
        if not pic_path.is_file():
            raise HTTPException(status_code=404, detail="Picture path error")
        return FileResponse(pic_path)
    else:
        print(f'failed to get pic: {pic_id}')
        raise HTTPException(status_code=404, detail="Picture id not found")