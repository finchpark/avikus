from sqlalchemy import Column, Integer, String, Text, DataTime

from database import Base

class Vessel(Base):
	__tablename__ = "vessel"

	id = Column(Integer, primary_key=True)
	created = Column(DataTime, nulable=False)
	name = Column(String, nullable=False)
	content = Column(Text)