from dataclasses import dataclass
from pydantic import BaseModel,HttpUrl
from typing import List
@dataclass
class Show:
    path:str
    size_kb:float
class UrlRequest(BaseModel):
    urls:List[HttpUrl]
    timeout:int=5