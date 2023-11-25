from fastapi import APIRouter, Query
from fastapi.responses import Response
from pydantic import AnyHttpUrl
from typing import Annotated

from interfaces.functions.encode import create_qr

router = APIRouter()


@router.get(
    "/v1/encode_url",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
    tags=["Encoding"],
)
async def encode_url(url: Annotated[AnyHttpUrl, Query(max_length=1024)]):
    """"""
    result_bytes = create_qr(text=str(url))
    return Response(content=result_bytes, media_type="image/png")
