from fastapi import FastAPI
from auth.router import auth_router
from api.router import api_router


app = FastAPI(
    title='ImageApp',
)

app.include_router(auth_router)
app.include_router(api_router)





