import ety
from pydantic import BaseModel


class TK(BaseModel):
    word: str
    language_code: str

    @validator('language_code')
    def language_must_be_valid_iso_code(cls, v):
        if v not in ety.data.iso_639_3_codes:
            raise ValueError('must be valid iso 639-3 code')
        return v
