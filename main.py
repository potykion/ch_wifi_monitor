import os

import dotenv
import sqlalchemy as sa

dotenv.load_dotenv(dotenv.find_dotenv())

DATABASE_URL = os.environ["DATABASE_URL"]

engine = sa.create_engine(DATABASE_URL)
