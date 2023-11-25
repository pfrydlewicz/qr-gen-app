from fastapi import APIRouter
from fastapi.responses import Response
from pydantic import AnyHttpUrl

from interfaces.functions.encode import create_qr_from_url

router = APIRouter()


@router.post(
    "/v1/encode_url",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
    tags=["Encoding"],
)
async def encode_url(url: AnyHttpUrl):
    """"""
    result_bytes = create_qr_from_url(url=url)
    return Response(content=result_bytes, media_type="image/png")
