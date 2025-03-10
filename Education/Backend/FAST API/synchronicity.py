import time
import asyncio
from fastapi import FastAPI, BackgroundTasks
import uvicorn

app = FastAPI()

def sync_task():
    time.sleep(3)
    print("Отправлен email")

async def async_task():
    await asyncio.sleep(3)
    print("Сделан запрос в сторонний API")

@app.post('/')
async def some_route(bg_tasks: BackgroundTasks):
    ...
    bg_tasks.add_task(sync_task)
    # asyncio.create_task(async_task())
    return {'ok': True}

if __name__ == '__main__':
    uvicorn.run('synchronicity:app', reload=True)