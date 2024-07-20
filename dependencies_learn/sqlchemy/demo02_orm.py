from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users2'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 创建表（如果它们不存在）
Base.metadata.create_all(engine)

new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()  # 提交事务保存数据

users = session.query(User).filter(User.age >= 18).all()
for user in users:
    print(f'{user.name}, {user.age}')


session.close()
