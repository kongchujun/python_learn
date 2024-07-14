from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

# 数据库连接设置
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 使用元数据定义表结构
metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer))

# 创建表了
metadata.create_all(engine)

# 创建一个选择（查询）对象
query = select(users.c.id, users.c.name, users.c.age)  # 正确使用 select 创建查询对象

# 执行查询
with engine.connect() as connection:
    result = connection.execute(query)  # 使用查询对象，而不是字符串
    for row in result:
        print(row)
