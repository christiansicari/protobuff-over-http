from fastapi import FastAPI, Response
import uvicorn 
app = FastAPI()
from gtfs_realtime_pb2 import VehiclePosition

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/rt")
def rt(response: Response):
    with open("./testFile.pb", "rb") as f:
        data = f.read()
        return Response(content=data, media_type="application/protobuf")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

