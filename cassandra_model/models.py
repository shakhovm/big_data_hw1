from django.db import connections


class ReviewByProduct:
    @staticmethod
    def get_review_by_product(product_id):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
            """
            SELECT * FROM review_by_product WHERE 
            product_id = %s
            """, [product_id])
        return res

    @staticmethod
    def get_review_by_product_star_rating(product_id, star_rating):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
            """
            SELECT * FROM review_by_product WHERE 
            product_id = %s AND star_rating = %s ALLOW FILTERING
            """, [product_id, star_rating])
        return res


class ReviewByCustomer:
    @staticmethod
    def get_review_by_customer(customer_id):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
                """
                SELECT * FROM review_by_customer WHERE 
                customer_id = %s
                """, [customer_id])

        return res
