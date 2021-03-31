from django.db import connections


class DBInserter:
    def __init__(self, cursor):
        self.cursor = cursor


class CassandraInserter(DBInserter):

    @staticmethod
    def insert_review_by_product(row, cursor):
        query = """
        INSERT INTO review_by_product (
                            product_id,
                            review_id,
                            review_headline,
                            helpful_votes,
                            star_rating,
                            review_body,
                            review_date
                            )
        VALUES (
        %s, %s,  %s, %s, %s, %s, %s
        )


        """
        cursor.execute(query, [
            row.product_id,
            row.review_id,
            row.review_headline,
            row.helpful_votes,
            row.star_rating,
            row.review_body,
            row.review_date
        ])

    @staticmethod
    def insert_review_by_customer(row, cursor):
        query = """
        INSERT INTO review_by_customer (
                        customer_id,
                        review_id,
                        review_headline,
                        helpful_votes,
                        star_rating,
                        review_body,
                        review_date)
        VALUES (
        %s, %s, %s, %s, %s, %s, %s
        )
        
        
        """
        cursor.execute(query, [
            row.customer_id,
            row.review_id,
            row.review_headline,
            row.helpful_votes,
            row.star_rating,
            row.review_body,
            row.review_date
        ])

    @staticmethod
    def insert_reviewed_items(row, cursor):
        query = """
        INSERT INTO reviewed_items (
                            product_id,
                            review_id,
                            review_date,
                            star_rating,
                            verified_purchase,
                            product_title,
                            product_category)
        VALUES (
        %s, %s, %s, %s, %s, %s, %s
        )

        """
        cursor.execute(query, [
            row.product_id,
            row.review_id,
            row.review_date,
            row.star_rating,
            row.verified_purchase,
            row.product_title,
            row.product_category
        ])

    @staticmethod
    def insert_customer_review(row, cursor):
        query = """
        INSERT INTO customer_review (
                            customer_id,
                            review_id,
                            review_date,
                            star_rating,
                            verified_purchase)
        VALUES (
        %s, %s, %s, %s, %s
        )

        """
        cursor.execute(query, [
            row.customer_id,
            row.review_id,
            row.review_date,
            row.star_rating,
            row.verified_purchase
        ])

    @staticmethod
    def insert_haters(row, cursor):
        if row.star_rating != 1 and row.star_rating != 2:
            return
        query = """
                INSERT INTO hater_reviews (
                                    review_id,
                                    customer_id,
                                    review_date
                                    )
                VALUES (
                %s, %s, %s
                )

                """
        cursor.execute(query, [
            row.review_id,
            row.customer_id,
            row.review_date
        ])

    @staticmethod
    def insert_backers(row, cursor):
        if row.star_rating != 4 and row.star_rating != 5:
            return
        query = """
                INSERT INTO backer_reviews (
                                    review_id,
                                    customer_id,
                                    review_date
                                    )
                VALUES (
                %s, %s, %s
                )

                """
        cursor.execute(query, [
            row.review_id,
            row.customer_id,
            row.review_date
        ])


class RDBMSInserter(DBInserter):

    @staticmethod
    def insert_to_products(row, cursor):
        query = """ 
        INSERT INTO products 
        (ID, product_parent, product_title, product_category) 
        VALUES (%s, %s, %s, %s)"""

        cursor.execute(query, [
            row.product_id,
            row.product_parent,
            row.product_title,
            row.product_category
        ])

    @staticmethod
    def insert_to_reviews(row, cursor):
        query = """ 
        INSERT INTO reviews
            (customer_id, id, product_id, star_rating, helpful_votes, 
            total_votes, vine, verified_purchase, review_headline, 
            review_body, review_date) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, [
            row.customer_id,
            row.review_id,
            row.product_id,
            row.star_rating,
            row.helpful_votes,
            row.total_votes,
            row.vine,
            row.verified_purchase,
            row.review_headline,
            row.review_body,
            row.review_date
        ])

