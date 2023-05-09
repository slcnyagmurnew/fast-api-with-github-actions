import uvicorn
from multiprocessing import Process
import asyncio
import aiohttp
from application import Application
import asynctest
import unittest


class TestApi(asynctest.TestCase):

    async def setUp(self):
        app = Application()
        self.proc = Process(target=uvicorn.run,
                            args=(app.api,),
                            kwargs={
                                "host": "127.0.0.1",
                                "port": 8000,
                                "log_level": "info"},
                            daemon=True)
        self.proc.start()
        await asyncio.sleep(0.1)  # time for the server to start

    async def tearDown(self):
        self.proc.terminate()

    async def test_say_hello(self):
        name = "Ahmet"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://127.0.0.1:8000/hello/{name}") as response:
                returned = await response.json()
        self.assertEqual(returned, {"message": f"Hello {name}"})


if __name__ == "__main__":
    unittest.main()