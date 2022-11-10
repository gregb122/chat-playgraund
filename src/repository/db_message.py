from sqlalchemy.orm.session import Session
from schemas.plant_schema import PlantBase
from chat.src.inventory_api.models.message_model import DbPlant

def add_plant(db: Session, owner_id: int, request: PlantBase):
    new_plant = DbPlant(
        name=request.name,
        description=request.description,
        is_public=request.is_public,
        owner_id=owner_id
    )
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    
    return new_plant


def get_plant_by_id(db: Session, plant_id: int):
    return db.query(DbPlant).filter(DbPlant.id == plant_id).first()

def update_plant(db: Session, plant_id: int, request: DbPlant):
    plant = db.query(DbPlant).filter(DbPlant.id == plant_id).first()
    if plant:
        plant.name = request.name
        plant.description = request.description
        plant.is_public = request.is_public
        
        db.add(plant)
        db.commit()
        db.refresh(plant)

    return plant

def delete_plant(db: Session, plant_id: int,):
    plant = db.query(DbPlant).filter(DbPlant.id == plant_id).first()
    if plant:
        db.delete(plant)
        db.commit()
    return plant