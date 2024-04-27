from sqlalchemy import Column, Integer, String, Text, DataTime

from database import Base

# model 생성
class Vessel(Base):
	# 모델이 사용할 Table
	__tablename__ = "vessel"

	# Model의 Column 속성
	id = Column(Integer, primary_key=True)
	created = Column(DataTime, nulable=False)
	name = Column(String, nullable=False)
	content = Column(Text)