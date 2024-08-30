from sqlalchemy import create_engine,Column,Integer,String,Float,MetaData,Table
from sqlalchemy.orm import sessionmaker

DB_URI = ''
engine = create_engine(DB_URI)
metaData= MetaData()

products_table = Table(
    'products',metaData,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('price',Float),
    Column('rating',Float),
)

def init_db():
    metaData.create_all(engine)

def insert_data(data):
    with engine.connect() as connection:
        for item in data:
            connection.execute(products_table.insert().values)(
                name = item['name'],
                price = float(item['price'].replace('$',''))
                rating = float(item['rating'])
            )

if __name__ == "__main__":
    init_db()
    data = data() # from proceesor.py
    insert_data(data)