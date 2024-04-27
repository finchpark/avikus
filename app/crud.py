from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app import models, schemas

# Create, Read, Update, Delete

def get_vessels(db: Session, skip: int=0, limit: int=100):
	return db.query(models.Vessel).offset(skip).limit(limit).all()

# Get data from ID
def get_vessel(db: Session, id: int):
	return db.query(models.Vessel).filter(models.Vessel.id == id).first()

# Create data
def create_vessel(db: Session, vessel: schemas.VesselCreate):
	vid = db.query(func.max(models.Vessel.id)).scalar()
	vid = vid + 1 if vid is not None else 1

	db_vessel = models.Vessel(**vessel.dict(), id=vid)
	db.add(db_vessel)
	db.commit()
	db.refresh(db_vessel)

	return db_vessel

# Update data
def update_vessel(db: Session, vessel: models.Vessel, updated_vessel: schemas.VesselCreate):
	for key, value in updated_vessel.dict().items():
		setattr(vessel, key, value)

	db.commit()
	db.refresh(vessel)

	return vessel

# Delete data
def delete_vessel(db: Session, vessel: models.Vessel):
	db.delete(vessel)
	db.commit()