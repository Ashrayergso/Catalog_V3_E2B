```python
import pandas as pd
from sqlalchemy import create_engine

# Establish a connection to the database
engine = create_engine('sqlite:///product_catalog.db')

def export_product_list():
    # Query all records in the database
    query = "SELECT * FROM product_catalog"
    df = pd.read_sql_query(query, engine)

    # Export the dataframe to a CSV file
    df.to_csv('product_catalog.csv', index=False)

    print("Product list has been exported to product_catalog.csv")
```