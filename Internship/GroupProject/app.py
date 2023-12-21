from fastapi import Depends, File, HTTPException, UploadFile, status
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from repo import UploadRepo, ListRepo, DownloadRepo


app = FastAPI()


@app.get("/")
def test_request():
    return {"message": "Hello, World!"}


@app.post(
    "/upload",
    status_code=status.HTTP_200_OK,
)
async def upload_a_file(
    file: UploadFile = File(...),
    up_repo: UploadRepo = Depends(UploadRepo)
):
    upload_string_name, upload_location = await up_repo.upload_file(file)
    return {"detail": f"File path is: {upload_location}/{upload_string_name}"}


@app.get(
        "/list",
        status_code=status.HTTP_200_OK,
)
async def list_files(
    list_f: ListRepo = Depends(ListRepo)
):
    try:
        list_response = await list_f.list_of_files()
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return list_response



# @app.get(
#     "/download/{filename}",
#     status_code=status.HTTP_200_OK,
# )
# async def download_file(
#     filename: str,
#     up_repo: UploadRepo = Depends(UploadRepo)
# ):
#     file_path = up_repo.get_uploaded_file_path(filename)
#     if os.path.exists(file_path):
#         return FileResponse(file_path, filename=filename)
#     else:
#         raise HTTPException(status_code=404, detail="File not found")


@app.get(
    "/download/{filename}",
    status_code=status.HTTP_200_OK,
)
async def download_file(
    filename: str,
    dw_repo: DownloadRepo = Depends(DownloadRepo)
):
    try:
        download_path = await dw_repo.download_files(filename)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return FileResponse(download_path, filename=filename)
