from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": "Я люблю Майнкрафт",
    "age": 12,
}

data_wo_age = {
    "email": "abc@mail.ru",
    "bio": "Я люблю Майнкрафт"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str or None = Field(max_length=100)
    model_config = ConfigDict(extra='forbid')

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "Пользователь добавлен"}

@app.get("/users")
def get_users():
    return users
    
if __name__ == "__main__":
    uvicorn.run("pydantic_test:app", reload=True)