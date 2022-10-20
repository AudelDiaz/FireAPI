from fastapi import FastAPI, Depends

from auth import get_user_token
from routers import accounts, addresses

app = FastAPI()
app.include_router(accounts.router)
app.include_router(addresses.router)


@app.get("/")
async def root(jwt: dict = Depends(get_user_token)):
    return {"message": f"Hello {jwt['email']}"}
