from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from typing import List


# fastapi配置项
API_PREFIX = "/api"

config = Config(".env")

DEBUG = config('DEBUG', cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="141mbdx4cu^3sf-=*jp$!(=)ek@wccghzmu!i=l+0!=9t+tm5s")

PROJECT_NAME: str = config("PROJECT", default="robot")
ALLOWED_HOSTS: List[str] = config(
    "127.0.0.1",
    cast=CommaSeparatedStrings,
    default=""
)