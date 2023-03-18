from fastapi import FastAPI
from chatgpt import generate_chat
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


@app.get("/generate_chat")
async def generate_chat_api(message: str):
    
    output_text = generate_chat(message)
    return {"User Input":message, "output_text": output_text}


