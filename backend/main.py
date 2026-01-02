from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class impost Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()


app = start_application()


@app.get("/")
def health():
    return {"Status": "System is healthy"}

