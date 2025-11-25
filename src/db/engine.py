from sqlalchemy import create_engine, Engine


def get_engine(connection_string: str, fast_executemany: bool = True) -> Engine:
    engine = create_engine(connection_string, fast_executemany=fast_executemany)
    return engine
