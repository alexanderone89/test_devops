from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

origins = [
    # "http://localhost:8000",
    # "http://127.0.0.1:8000",
    "*"
]

app.add_middleware(
    # сначапо все запрещаем
    CORSMiddleware,
    # потом начинаем разрешать необходимое
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/monitoring/test/api")
async def monitoring_test():
    print('test in run')
    return 1001

@app.post("/monitoring/test/api", status_code=200)
async def monitoring_test_post(
        arm: int,
        sign: int):
    if sign == 1:
        print(f'test in arm = {arm} is run')
        return {'response': 'OK'}

