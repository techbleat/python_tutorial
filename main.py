
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI ()


@app.get ("/hello", response_class=HTMLResponse)
async def say_hello():
    html_content ="hello guys"
    return HTMLResponse(content=html_content)


@app.get ("/welcome", response_class=HTMLResponse)
async def welcome():
    html_content ="<b>welcome guys. This is your portal</b>"
    return HTMLResponse(content=html_content)
    



