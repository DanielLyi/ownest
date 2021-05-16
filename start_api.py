import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserInput(BaseModel):
    text: str
    type: int


@app.post("/")
def call_api(inp: UserInput):
    return {"text": inp.text,
            "type": inp.type}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
