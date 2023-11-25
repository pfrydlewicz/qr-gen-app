from fastapi import APIRouter, Query
from fastapi.responses import Response
from pydantic import AnyHttpUrl
from typing import Annotated

from interfaces.enums import file_formats
from interfaces.functions.encode import create_qr

router = APIRouter()


@router.get(
    "/v1/encode_url",
    responses={
        200: {
            "content": {
                file_formats.get_content_type(fmt): {}
                for fmt in file_formats.FileFormatEnums
            }
        }
    },
    response_class=Response,
    tags=["Encoding"],
)
async def encode_url(
    url: Annotated[AnyHttpUrl, Query(max_length=1024)],
    border_width: Annotated[int, Query(ge=0, le=20)] = 2,
    file_format: file_formats.FileFormatEnums = file_formats.FileFormatEnums.PNG,
):
    """"""
    result_bytes, exported_format = create_qr(
        text=str(url), border_width=border_width, file_format=file_format
    )
    return Response(
        content=result_bytes,
        media_type=file_formats.get_content_type(exported_format),
        headers={"Content-Type": file_formats.get_content_type(exported_format)},
    )
