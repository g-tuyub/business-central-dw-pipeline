from sqlalchemy import create_engine, Engine, URL

def get_engine(connection_url: URL, fast_executemany: bool = True) -> Engine:
    engine = create_engine(connection_url, fast_executemany=fast_executemany)
    return engine
