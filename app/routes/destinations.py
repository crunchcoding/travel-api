from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import TravelDestination
from app.schemas import DestinationCreate, DestinationOut
from app.database import get_db
from fastapi import Depends
from typing import List

router = APIRouter()

@router.get("/", response_model=List[DestinationOut])
def get_destinations(db: Session = Depends(get_db)):
    return db.query(TravelDestination).all()

@router.post("/", response_model=DestinationOut)
def create_destination(destination: DestinationCreate, db: Session = Depends(get_db)):
    db_destination = TravelDestination(**destination.dict())
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination

@router.put("/{destination_id}", response_model=DestinationOut)
def update_destination(destination_id: int, destination: DestinationCreate, db: Session = Depends(get_db)):
    db_destination = db.query(TravelDestination).filter(TravelDestination.id == destination_id).first()
    if db_destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    for key, value in destination.dict().items():
        setattr(db_destination, key, value)
    db.commit()
    db.refresh(db_destination)
    return db_destination

@router.delete("/{destination_id}")
def delete_destination(destination_id: int, db: Session = Depends(get_db)):
    db_destination = db.query(TravelDestination).filter(TravelDestination.id == destination_id).first()
    if db_destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    db.delete(db_destination)
    db.commit()
    return {"message": "Destination deleted successfully"}
