from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import crud, database, models, schemas

# Table 생성
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# vessels 리스트 가져오기
@app.get("/vessels/", response_model=List[schemas.Vessel])
async def read_vessels(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    vessels = crud.get_vessels(db, skip, limit)
    return vessels

# ID로 vessel 조회
@app.get("/vessels/{id}", response_model=schemas.Vessel)
async def read_vessel(id: int, db: Session=Depends(get_db)):
    db_vessel = crud.get_vessel(db, id)
    if db_vessel is None:
        raise HTTPException(status_code=404, detail=("Vessel [%d] not found" %id))
    
    return db_vessel

# vessel 생성
@app.post("/vessels/", response_model=schemas.Vessel)
async def create_vessel(vessel: schemas.VesselCreate, db: Session=Depends(get_db)):
    # ID가 넘어온다면..
    #db_vessel = crud.get_vessel(db, id=vessel.id)
    #if db_vessel:
    #    raise HTTPException(status_code=400, detail="ID has already registered")
    
    return crud.create_vessel(db=db, vessel=vessel)

# ID에 해당하는 vessel Update
@app.put("/vessels/{id}", response_model=schemas.Vessel)
async def update_vessel(id: int, updated_vessel: schemas.VesselCreate, db: Session=Depends(get_db)):
    db_vessel = crud.get_vessel(db, id)
    if db_vessel is None:
        raise HTTPException(status_code=404, detail=("Vessel [%d] not found" %id))
    
    return crud.update_vessel(db, db_vessel, updated_vessel)

# ID로 vessel 삭제
@app.delete("/vessels/{id}")
def delete_vessel(id: int, db: Session=Depends(get_db)):
    db_vessel = crud.get_vessel(db, id)
    if db_vessel is None:
        raise HTTPException(status_code=404, detail=("Vessel [%d] not found" %id))
    
    crud.delete_vessel(db, id)
    return JSONResponse(content={"message": ("Vessel [%d] deleted" %id)})