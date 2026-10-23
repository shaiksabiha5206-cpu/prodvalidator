import asyncio
from validator.modules import UrlRequest
from validator.process import check_all
from validator.logger import log
async def main():
    request=UrlRequest(urls=["https://google.com","https://github.com","https://sabi.com"])
    log.info(f"valid request:{request}")
    await check_all(request.urls)
if __name__ == "__main__":
    asyncio.run(main())