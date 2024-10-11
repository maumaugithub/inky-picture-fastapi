from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from datetime import datetime
from inky_picture_service.model import InkyPicture, inky_pics_db
from inky_picture_service.resize import resize_pic
import inky_picture_service.utils.file_utils as fu


app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    # TODO: move this to configuration
    uvicorn.run("inky-pic-api:app", host="localhost", port=9000)

pics_cache = inky_pics_db()

@app.get("/pics", response_model=List[InkyPicture])
async def get_all_pics():
    return pics_cache


@app.get("/pics/daily")
async def get_daily_inky_pic():
    pic_path = Path("test/asset/cacti-hi.jpg")
    if not pic_path.is_file():
        raise HTTPException(status_code=404, detail="Picture not found")

    # Resize image
    resize_folder = 'resized'
    resized_res = resize_pic(pic_path, resize_folder)
    resized_image_path = pic_path if str(pic_path) in str(resized_res) else Path(resized_res)
    if not resized_image_path.is_file():
        raise HTTPException(status_code=404, detail="Resized Picture not found")
    _add_to_pic_db(resized_image_path)
    return FileResponse(resized_image_path)


@app.get("/pics/{pic_id}")
async def get_inky_pics_by_id(pic_id: int):
    if pic_id <= len(pics_cache)-1:
        print(f'Requested pic: {pic_id}')
        record: InkyPicture = pics_cache[pic_id]
        pic_path = Path(record.uri)
        if not pic_path.is_file():
            raise HTTPException(status_code=404, detail=f"Picture path error {pic_path}")
        return FileResponse(pic_path)
    else:
        print(f'failed to get pic: {pic_id}')
        raise HTTPException(status_code=404, detail=f"Picture id {pic_id} not found")


def _add_to_pic_db(resized_image_path):
    size = len(pics_cache)
    created_dt = datetime.today()
    base_name = fu.get_file_basename_no_ext(resized_image_path)
    created_text = created_dt.strftime('%Y-%m-%d %H:%M:%S')
    resized_image = InkyPicture(
        id=size,
        title=f'{base_name} resized on {created_text}',
        uri=fu.get_relative_path(resized_image_path),
        created_at=created_dt
    )
    pics_cache.append(resized_image)
