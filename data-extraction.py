from sqlalchemy import create_engine

import logging
import pandas as pd

class SQLReader:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.engine = create_engine(
                self.connection_string
            )

    def run_query(self, query: str) -> pd.DataFrame:
        results = pd.read_sql(query, self.engine)
        logging.info(f"Read {len(results)} lines")
        return results


def get_scope(reader: SQLReader) -> pd.DataFrame:


    

    return pd.DataFrame()