from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TicketBase(BaseModel):
  category: str  # e.g., "AC", "IT", "Electrical", "Housekeeping", "Security", "Meeting Room"
  description: str
  employee_email: str


class TicketCreate(TicketBase):
  pass  # Used when an employee submits a new ticket


class TicketResponse(TicketBase):
  id: int
  status: str
  created_at: datetime

  # Allows Pydantic to read data from SQLAlchemy models
  model_config = ConfigDict(from_attributes=True)