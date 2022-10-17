from sqlalchemy import create_engine, update, Column, Float, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app/static/data/market.db', echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)


def initialise():
    Base.metadata.create_all(engine)
    session = Session()
    if not session.query(Product).all():
        reset()
    session.close()


def get_products() -> list:
    session = Session()
    products = []
    products_db = session.query(Product).all()
    for product in products_db:
        products.append({
            "id": product.id,
            "nome": product.name,
            "preco": product.price
        })
    session.close()
    return products


def set_product(product) -> None:
    session = Session()
    new_product = Product(
        name=product["nome"],
        price=product["preco"]
    )
    session.add(new_product)
    session.commit()
    session.close()
    return


def update_product(product) -> None:
    session = Session()
    session.query(Product).filter_by(id=product["id"]).update({
        "name": product["name"],
        "price": product["price"]
    })
    session.commit()
    session.close()
    return


def delete_product(product_id) -> None:
    session = Session()
    session.query(Product).filter_by(id=product_id).delete()
    session.commit()
    session.close()
    return


def reset() -> None:
    default_products = [
        {
            "id": 0,
            "nome": "Cenoura",
            "preco": 2.12
        },
        {
            "id": 1,
            "nome": "Cebola",
            "preco": 2.34
        },
        {
            "id": 3,
            "nome": "Tomate",
            "preco": 2.25
        },
        {
            "id": 4,
            "nome": "Picles",
            "preco": 5.79
        },
        {
            "id": 5,
            "nome": "Pepin\u00e3o",
            "preco": 2.3
        },
        {
            "id": 6,
            "nome": "Batata",
            "preco": 3.29
        },
        {
            "id": 7,
            "nome": "Banana",
            "preco": 3.15
        },
        {
            "id": 8,
            "nome": "Ab\u00f3bora",
            "preco": 10.23
        },
        {
            "id": 9,
            "nome": "Kombucha",
            "preco": 5.22
        },
        {
            "id": 10,
            "nome": "Moranguinho do nordeste",
            "preco": 18.98
        },
        {
            "id": 11,
            "nome": "Ma\u00e7\u00e3",
            "preco": 4.15
        },
        {
            "id": 13,
            "nome": "Propolis",
            "preco": 3.75
        },
        {
            "id": 15,
            "nome": "Abacate",
            "preco": 5.4
        }
    ]

    session = Session()

    session.query(Product).delete()

    for product in default_products:
        new_product = Product(
            name=product['nome'],
            price=product['preco']
        )
        session.add(new_product)
        session.commit()

    session.close()
    return
