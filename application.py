from fastapi import FastAPI
import logging


class Application:

    def __init__(self):
        self.api = FastAPI()
        self.api.on_event("shutdown")
        self.api.get("/")(self.root)
        self.api.get("/hello/{name}")(self.say_hello)

    async def root(self):
        return {"message": "Hello World"}

    async def say_hello(self, name: str):
        return {"message": f"Hello {name}"}

    async def close(self):
        logging.warning("Shutting down the app.")
