
"""
Simple seed script to pre-fill the database with a few categories and transactions.
Run with:  python -m scripts.seed
"""

from app.db.db_setup import SessionLocal
from app.models.transaction import Category, Transaction

def get_or_create_category(db, name: str):
    cat = db.query(Category).filter(Category.name == name).first()
    if cat:
        return cat
    cat = Category(name=name)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def main():
    db = SessionLocal()
    try:
        # Create (or fetch) a few categories
        groceries = get_or_create_category(db, "Groceries")
        dining    = get_or_create_category(db, "Dining")
        rent      = get_or_create_category(db, "Rent")

        # Add a few transactions only if table is empty (keep it simple)
        existing = db.query(Transaction).count()
        if existing == 0:
            db.add_all([
                Transaction(amount=42.50,  category_id=groceries.id),
                Transaction(amount=18.99,  category_id=dining.id),
                Transaction(amount=1200.0, category_id=rent.id),
            ])
            db.commit()
            print("Seeded 3 example transactions.")
        else:
            print(f"Transactions already present ({existing}); skipping inserts.")
        print("Categories and transactions are ready.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
