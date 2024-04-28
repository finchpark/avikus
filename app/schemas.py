from typing import Union
from pydantic import BaseModel
from datetime import datetime

# pydantic - data parsing 에 사용
# pydantic의 BaseModel을 상속
class VesselBase(BaseModel):
	created: datetime
	name: str
	content: Union[str, None] = None

class VesselCreate(VesselBase):
	pass

# API에서 데이터 읽기/쓰기에 사용할 모델
class Vessel(VesselBase):
	id: int

	class ConfigDict:
			from_attributes = True