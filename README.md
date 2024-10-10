# inky-picture-fastapi
 Fast Open API for inky-picture-service

# Development Setup
1. Create a venv environment with Python 3.12
Linux:
```bash
.\.venv\bin\activate
```
MS:
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