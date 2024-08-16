from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/podcasts.db')
Session = sessionmaker(bind=engine)

session = Session()
