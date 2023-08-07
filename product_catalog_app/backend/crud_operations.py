```python
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Product

Base.metadata.create_all(bind=engine)

def create_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def read_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product: Product):
    db_product = db.query(Product).filter(Product.id == product.id).first()
    db_product.name = product.name
    db_product.description = product.description
    db_product.number = product.number
    db_product.vendor = product.vendor
    db_product.cost = product.cost
    db_product.image = product.image
    db_product.link = product.link
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
```