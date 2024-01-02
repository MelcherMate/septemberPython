from sqlalchemy import create_engine, text



class DatabaseHandler:
    def __init__(self, url):
        self.url = url
        self.engine = create_engine(self.url)

    def get_engine(self, url):
        return create_engine(url)

    def run_sql(self, sql_script, data=[]):
            
            with self.engine.connect() as conn:
                try:
                    conn.execute(text(sql_script), data)
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    print(f"Error occured: {str(e)}")




if __name__ == '__main__':
    from params import url
    db = DatabaseHandler(url)

    db.url = url
