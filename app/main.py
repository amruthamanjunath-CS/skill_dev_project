from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Corporate Facility Management API")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tickets/", response_model=schemas.TicketResponse)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@app.get("/tickets/", response_model=list[schemas.TicketResponse])
def get_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Ticket).offset(skip).limit(limit).all()