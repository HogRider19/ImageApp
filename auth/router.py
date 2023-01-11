from fastapi import APIRouter


auth_router = APIRouter(prefix='/auth')


@auth_router.post('/createuser')
async def create_user():
    pass

@auth_router.delete('/deleteuser')
async def delete_user():
    pass

@auth_router.post('/login')
async def login():
    pass

@auth_router.get('/me')
async def me():
    pass