import uvicorn

from codingchallenge_qa_service.app import create_app

if __name__ == "__main__":
    uvicorn.run(app=create_app(), host="127.0.0.1", port=8000)
