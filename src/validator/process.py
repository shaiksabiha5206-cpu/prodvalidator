import asyncio
from validator.logger  import log
from typing import List
async def check_url(url:str) ->bool:
    log.info(f"checking {url}")
    await asyncio.sleep(2)
    log.info(f"checked {url}")
    return True
async def check_all(urls:List[str]):
    log.info(f"starting check")
    results= await asyncio.gather(
        check_url,
        check_all
    )
    log.info(f"finished")
    return results