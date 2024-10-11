# inky-picture-fastapi
 Fast Open API for inky_picture_service.
 This API will serve a new Portrait Device.


# Development Setup
1. Create a venv environment with Python 3.12
Linux:
```bash
.\.venv\bin\activate
```
with Microsoft:
```bash
.\\.venv\Scripts\Activate.ps1
```
verify:
```bash
python --version
```
2. Install requirements
```bash
pip install -r requirements.txt
```
3. Run the API
go to api location:
```bash
uvicorn inky-pic-api:app --reload --port 5000
```
Press CTRL+C to quit

or 
```bash
python inky_picture_service/inky-pic-api.py
```

## Installation

```bash
pip install -U inky_picture_service
```

Then you can run

```bash
inky_picture_service --help
```
