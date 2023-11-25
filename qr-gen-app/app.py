from fastapi import FastAPI
from starlette.responses import RedirectResponse

from interfaces.api import api_v1

app = FastAPI(title="QR Generator App")
app.include_router(api_v1.router)

@app.get("/")
async def root():
    return RedirectResponse(url='/docs')
