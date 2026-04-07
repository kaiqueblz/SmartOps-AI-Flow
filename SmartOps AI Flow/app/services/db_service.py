from sqlalchemy import create_engine, text
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def get_customer_by_email(email: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM customers WHERE email = :email"),
            {"email": email}
        )
        return result.fetchone()