import os
import random
import aiofiles
from fastapi import UploadFile


class UploadRepo:
    async def upload_file(self, file: UploadFile):
        upload_location = os.path.join(os.getcwd(), "Storage")
        if not os.path.exists(upload_location):
            os.makedirs(upload_location)
        upload_string_name = file.filename
        file_location = os.path.join(upload_location, upload_string_name)
        async with aiofiles.open(file_location, "wb") as f:
            await f.write(await file.read())
        return upload_string_name, upload_location
    
    def get_uploaded_file_path(self, filename:str):
        upload_location = os.path.join(os.getcwd(), "Storage")
        file_location = os.path.join(upload_location, filename)
        return file_location


class ListRepo:
    async def list_of_files(self):
        upload_location = os.path.join(os.getcwd(), "Storage")
        files = []
        if not os.path.exists(upload_location):
            raise FileNotFoundError("No files uploaded yet")
        files = os.listdir(upload_location)
        return files


class DownloadRepo(UploadRepo):
    async def download_files(self, filename):
        file_path = self.get_uploaded_file_path(filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError("No files available to download")
        return file_path

