from database import Base, engine
import models

# SQLAlchemy to create all tables we defined in models.py
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
