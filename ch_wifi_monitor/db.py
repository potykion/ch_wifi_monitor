import contextlib
import os
from typing import Dict

import dotenv
import sqlalchemy as sa
from clickhouse_sqlalchemy import Table, types, engines, make_session
from sqlalchemy.orm import Session

dotenv.load_dotenv(dotenv.find_dotenv())

DATABASE_URL = os.environ["DATABASE_URL"]

engine = sa.create_engine(DATABASE_URL)

metadata = sa.MetaData(engine)
session: Session = make_session(engine)


wifi_table = Table(
    "wifi", metadata,
    sa.Column("dt", types.DateTime),
    sa.Column("client_ip", types.String),
    sa.Column("download_speed", types.Float),
    sa.Column("upload_speed", types.Float),
    sa.Column("ping", types.Float),
    sa.Column("bytes_sent", types.Int),
    sa.Column("bytes_received", types.Int),
    engines.Memory()
)


def insert_speed(speed: Dict) -> None:
    with contextlib.suppress(RuntimeError):
        session.execute(wifi_table.insert(), speed)


if __name__ == '__main__':
    with contextlib.suppress(RuntimeError):
        wifi_table.create()
