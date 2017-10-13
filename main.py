import asyncio
import uvloop
from sqlalchemy import create_engine
import config
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

engine = create_engine(config.DB_ENGINE, echo=True)