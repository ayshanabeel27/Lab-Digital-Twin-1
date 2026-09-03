from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)

    computer_id = Column(String, nullable=False)
    room_id = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    cpu_pct = Column(Float)
    ram_pct = Column(Float)
    ram_used_gb = Column(Float)
    ram_available_gb = Column(Float)

    disk_pct = Column(Float)

    net_sent_mb = Column(Float)
    net_recv_mb = Column(Float)

    process_count = Column(Integer)
