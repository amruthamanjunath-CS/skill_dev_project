from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True) # e.g., AC, IT, Electrical
    description = Column(String, nullable=False)
    status = Column(String, default="Open") # Open, In Progress, Resolved
    created_at = Column(DateTime, default=datetime.utcnow)
    employee_email = Column(String, nullable=False)