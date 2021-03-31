from django.db import models
from products.models import Product
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class Review(models.Model):
    id = models.\
        CharField(verbose_name='id', db_index=True, max_length=60, primary_key=True)
    star_rating = models.IntegerField()
    helpful_votes = models.IntegerField()
    total_votes = models.IntegerField(null=True)
    review_headline = models.CharField(max_length=10000)
    review_body = models.CharField(max_length=10000)
    review_date = models.DateField()
    vine = models.CharField(max_length=1)
    verified_purchase = models.CharField(max_length=1)
    customer_id = models.IntegerField()
    product = models.ForeignKey(Product,  on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'reviews'

    @staticmethod
    def get_most_reviewed_items(first_time, second_time, number_of_products):
        return Review.objects.raw(
            """
            SELECT
                  products.id, products.product_parent, products.product_title, products.product_category
            FROM reviews INNER JOIN products
                ON reviews.product_id=products.id
            WHERE
            (date(%s) <= reviews.review_date)
                AND
            (date(%s) > reviews.review_date)
                GROUP BY products.id ORDER BY count(products.id)  DESC LIMIT %s;

            """, [first_time, second_time, number_of_products]
        )

    @staticmethod
    def get_productive_customers(first_date, second_date, number_of_customers):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
                  reviews.customer_id
            FROM reviews
            WHERE
                (date(%s) <= reviews.review_date)
                    AND
                (date(%s) > reviews.review_date)
                    AND
                (verified_purchase = 'Y')
            GROUP BY reviews.customer_id ORDER BY count(reviews.customer_id) DESC LIMIT %s;
            """, [first_date, second_date, number_of_customers])
            row = dictfetchall(cursor)
        return row

    @staticmethod
    def get_productive_haters(first_date, second_date, number_of_haters):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
                  reviews.customer_id, count(reviews.customer_id) as rn
            FROM reviews
            WHERE
                (date(%s) <= reviews.review_date)
                    AND
                (date(%s) > reviews.review_date)
                    AND
                (star_rating = 1 OR star_rating = 2)
            GROUP BY reviews.customer_id ORDER BY rn DESC LIMIT %s;
            """, [first_date, second_date, number_of_haters])
            row = dictfetchall(cursor)
        return row

    @staticmethod
    def get_productive_backers(first_date, second_date, number_of_haters):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
                  reviews.customer_id, count(reviews.customer_id) as rn
            FROM reviews
            WHERE
                (date(%s) <= reviews.review_date)
                    AND
                (date(%s) > reviews.review_date)
                    AND
                (star_rating = 4 OR star_rating = 5)
            GROUP BY reviews.customer_id ORDER BY rn DESC LIMIT %s;
            """, [first_date, second_date, number_of_haters])
            row = dictfetchall(cursor)
        return row

