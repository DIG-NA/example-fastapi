from fastapi import FastAPI
from pydantic import BaseModel
from translatepy.translators.google import GoogleTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.deepl import DeeplTranslate
from translatepy.translators.bing import BingTranslate
from translatepy.translators.libre import LibreTranslate
from translatepy.translators.mymemory import MyMemoryTranslate
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.translatecom import TranslateComTranslate
from translatepy.translators.microsoft import MicrosoftTranslate
from translatepy.translators.deepl import DeeplTranslateException
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:38737",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/res/test")
async def fetmode():
   return "a successful test"

class text(BaseModel):
    toBeTranslated: str

@app.post("/res/g")
def trans(response:text):
        g=GoogleTranslate().translate( text= response.toBeTranslated,destination_language='English').result.encode()
        # print(g)
        return g

@app.post("/res/y")
def trans(response:text):
    return YandexTranslate().translate(text= response.toBeTranslated,destination_language='English').result

@app.post("/res/d")
def trans(response:text):
    print(DeeplTranslateException())
    return DeeplTranslate().translate(text= response.toBeTranslated,destination_language='English').result

@app.post("/res/m")
def trans(response:text):
    return MyMemoryTranslate().translate(text= response.toBeTranslated,destination_language='English').result

@app.post("/res/r")
def trans(response:text):
    return ReversoTranslate().translate(text= response.toBeTranslated,destination_language='English').result

@app.post("/res/t")
def trans(response:text):
    return TranslateComTranslate().translate(text= response.toBeTranslated,destination_language='English').result


# 2 not working 

#bingtranslator also doesn't work
# @app.post("/res/b")
# def trans(response:text):
#     return MicrosoftTranslate().translate(text= response.toBeTranslated,destination_language='English')

# @app.post("/res/l")
# def trans(response:text):
#     return LibreTranslate().translate(text= response.toBeTranslated,destination_language='English')
