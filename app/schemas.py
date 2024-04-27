from typing import Union
from pydantic import BaseModel
from datetime import datetime

class VesselBase(BaseModel):
	name: str
	content: Union[str, None] = None

class VesselCreate(VesselBase):
	pass

class Vessel(VesselBase):
	id: int
	created: datetime

	class Config:
			orm_mode = True