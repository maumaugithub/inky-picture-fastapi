from datetime import datetime
from pydantic import BaseModel


class InkyPicture(BaseModel):
    id: int
    title: str
    uri: str
    created_at: datetime = datetime.today()


def inky_pics_db():
    return [
        InkyPicture(id=0, title="The Happy Cacti says hi!", uri="test\\asset\\cacti-hi.jpg")
    ]
