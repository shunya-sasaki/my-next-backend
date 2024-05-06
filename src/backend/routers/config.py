from fastapi import APIRouter
from fastapi import Query
from pathlib import Path
import datetime


router = APIRouter()


@router.get("/config/directory_exist/")
async def directory_exist(
    directory: str = Query(
        title="Directory",
        description="Directory to check if it exists",
        example="/Users/Shun/Downloads",
        required=True,
    )
):
    response: dict[str, str | bool | None] = {"directory_path": directory}
    if directory is not None:
        dirpath = Path(directory)
        response["directory_exist"] = dirpath.exists()
        if dirpath.exists():
            st_mtime = dirpath.stat().st_mtime
            str_mtime = datetime.datetime.fromtimestamp(st_mtime).strftime(
                r"%Y-%m-%d %H:%M:%S")
            response["directory_last_modified_time"] = str_mtime
        else:
            response["directory_last_modified_time"] = None
    else:
        response["directory_exist"] = False
    print(f"Directory: {response["directory_path"]}")
    print(f"Directory exist: {response["directory_exist"]}")
    print(f"Directory timestamp: {response["directory_last_modified_time"]}")
    return response
