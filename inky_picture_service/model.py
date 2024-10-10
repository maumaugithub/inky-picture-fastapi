from pydantic import BaseModel

class InkyPicture(BaseModel):
    id: int
    title: str
    uri: str
   
    # pictures = {1: {"title": "The Happy Cacti says hi!", "fileUri": "test/resources/cacti-hi.jpg"}} 
def inkyPicsDB():
    return [
    InkyPicture(id=1, title="The Happy Cacti says hi!", uri="test/resources/cacti-hi.jpg")
]