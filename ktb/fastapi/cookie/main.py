from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="RESTful JSON Login API")
app.mount("/static", StaticFiles(directory = "public"), name = "static")

@app.get("/")
async def read_root():
    return FileResponse("public/cookie.html")

@app.get("/auth/status")
def get_auth_status(request: Request):
    username = request.cookies.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="unauthorized")
    return {"username": username}

@app.post("/auth/login")
def login(response: Response):
    username = "NewUser"
    response.set_cookie("username", username, httponly=True, path = "/")
    return {"username": username}

@app.delete("/auth/logout")
def logout(response: Response):
    response.delete_cookie("username", path = "/")
    response.status_code = 204
    return response



