from fastapi import FastAPI

from api.routes import router

app = FastAPI(title="WJX Auto Filler", version="0.2.0")

app.include_router(router)


def main():
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info",
    )


if __name__ == "__main__":
    main()
