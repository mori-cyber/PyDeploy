from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __table_args__ = {"extend_existing":True}# از دوباره ساخته شدن جدول یا همان تیبل در هر بار اجرا جلوگیری می کند
    id : Optional[int]=Field(default=None, primary_key=True)
    email : str
    password: Optional[str]