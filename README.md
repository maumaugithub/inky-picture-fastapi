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

This triggers the Run panel on IntelliJ.

Notice: the port here will be defined in config.
```bash
python inky_picture_service/inky-pic-api.py
```

I have run with the previous command and with the snippet below on VSCode
```bash
uvicorn inky_picture_service/inky-pic-api:app --reload --port 5000
```

## Test with curl
I will share the postman collection later ;)
```bash
curl --location 'http://127.0.0.1:9000/pics'
```

## Installation

```bash
pip install -U inky_picture_service
```

Then you can run

```bash
inky_picture_service --help
```
