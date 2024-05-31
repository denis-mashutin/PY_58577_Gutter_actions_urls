from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/")
def put():
    return {"Hello": "World"}


@router.api_route("/fastapi_app/get_post/", methods=["GET", "POST"])
def get_post():
    pass


app.include_router(router)
