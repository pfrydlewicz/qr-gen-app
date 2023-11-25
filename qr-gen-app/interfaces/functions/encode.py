import io
from qrcode import QRCode
from qrcode import constants
from qrcode.image.svg import SvgImage
from xml.etree.ElementTree import tostring

from interfaces.enums import file_formats


def create_qr(
    text: str,
    file_format: file_formats.FileFormatEnums,
    border_width: int = 4,
) -> bytes:
    """"""
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=border_width,
    )
    qr.add_data(text)

    image_factory = None
    save_kwargs = {}
    if file_format == file_formats.FileFormatEnums.SVG:
        image_factory = SvgImage
    else:
        save_kwargs = {"format": file_format.value}

    img = qr.make_image(
        fill_color="black", back_color="white", image_factory=image_factory
    )

    if isinstance(img, SvgImage):
        result = io.BytesIO(img.to_string()).getvalue()
    else:
        img_bytes = io.BytesIO()
        img.save(img_bytes, **save_kwargs)
        result = img_bytes.getvalue()

    return result, file_format
