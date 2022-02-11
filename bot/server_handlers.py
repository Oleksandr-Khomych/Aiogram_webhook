from aiohttp.web import Response
from aiohttp.web_request import Request


async def hello(request: Request) -> Response:
    return Response(text="Hello, world")
