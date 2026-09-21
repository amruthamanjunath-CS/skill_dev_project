from sqlalchemy.orm import Session
from . import models, schemas


def get_ticket(db: Session, ticket_id: int):
  return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()


def get_tickets(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Ticket).offset(skip).limit(limit).all()


def create_ticket(db: Session, ticket: schemas.TicketCreate):
  db_ticket = models.Ticket(
      category=ticket.category,
      description=ticket.description,
      employee_email=ticket.employee_email,
      status="Open",  # Default status when raised
  )
  db.add(db_ticket)
  db.commit()
  db.refresh(db_ticket)
  return db_ticket