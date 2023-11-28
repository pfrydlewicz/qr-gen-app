""""""

from enum import Enum


class FileFormatEnums(str, Enum):
    """Enum for exportable QR code file formats."""

    PNG = "png"
    JPG = "jpeg"
    SVG = "svg"


def get_content_type(format: FileFormatEnums):
    match (format):
        case FileFormatEnums.PNG:
            return "image/png"
        case FileFormatEnums.JPG:
            return "image/jpeg"
        case FileFormatEnums.SVG:
            return "image/svg+xml"
