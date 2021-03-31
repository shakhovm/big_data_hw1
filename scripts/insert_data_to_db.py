import psycopg2
import pandas as pd
from datetime import datetime
import datetime
from cassandra.cqlengine import columns
from django.db import connections

from scripts.DBInserter import CassandraInserter, RDBMSInserter

from time import time
def insert_data():
    x = 0
    path = "~/Downloads/amazon_reviews_us_Books_v1_02.tsv"
    rdbms_inserter = connections['default'].cursor()

    cassandra_inserter = connections['cassandra'].cursor()
    functions = [
        (CassandraInserter.insert_review_by_customer, cassandra_inserter),
        (CassandraInserter.insert_review_by_product, cassandra_inserter),
        (CassandraInserter.insert_haters, cassandra_inserter),
        (CassandraInserter.insert_backers, cassandra_inserter),
        (CassandraInserter.insert_customer_review, cassandra_inserter),
        (CassandraInserter.insert_reviewed_items, cassandra_inserter),
        # (RDBMSInserter.insert_to_reviews, rdbms_inserter),
        # (RDBMSInserter.insert_to_products, rdbms_inserter)

    ]

    start = time()
    for line in pd.read_csv(path, sep='\t', nrows=10000, chunksize=30):
        if x % 5000 == 0:
            print(time() - start)
        for i, row in line.iterrows():
            x += 1
            row.product_id = str(row.product_id)
            row.review_headline = str(row.review_headline)
            for function in functions:
                try:
                    function[0](row, function[1])
                except Exception as e:
                    pass
                    # print(e)
                    # print(row)
                    # print('-------------------------------')


    print("OK")
