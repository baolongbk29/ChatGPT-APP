from fastapi import FastAPI
from hiskit import generate_history
from fastapi.middleware.cors import CORSMiddleware


# output_text = generate_chat("Who is best football player?")
# print(output_text)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MAX_INPUT_LENGTH = 32

@app.get("/home")
async def home():

    return {"Message": "Welcome History Kit"}


@app.get("/generate_history")
async def generate_history_api(message: str):
    
    output_text = generate_history(message)
    return {"name":message, "history": output_text}


