# Archivo que genera la base de datos
# utilizando sqlalchemy y SQLite3
from sqlalchemy import create_engine, schema, types
from sqlalchemy import MetaData, Column, Table, ForeignKey, Sequence

metadata = schema.MetaData()

table_user = schema.Table("user", metadata,
                          schema.Column("id", types.Integer,
                                        Sequence("idxUserId", start=1,
                                                 increment=1),
                                        primary_key=True),
                          schema.Column("name", types.String(100)),
                          schema.Column("age", types.Integer),
                          schema.Column("password", types.String(20))
                          )

table_address = schema.Table("address", metadata,
                             schema.Column("id", types.Integer,
                                           primary_key=True),
                             schema.Column("userId", None,
                                           ForeignKey("user.id")),
                             schema.Column("email", types.String(50),
                                           nullable=False)
                             )

engine = create_engine("sqlite:///demo.db", echo=True)
metadata.bind = engine

metadata.create_all(checkfirst=True)
