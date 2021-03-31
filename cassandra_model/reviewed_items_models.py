from django.db import connections
from collections import OrderedDict

def count_id(res, key, number_of_items):
    results = dict()
    for i in res:
        if i[key] not in results:
            results[i[key]] = 1
        else:
            results[i[key]] += 1
    results = sorted(results.items(), key=lambda x: x[1], reverse=True)[:number_of_items]
    results = list(map(lambda x: {key: x[0]}, results))
    return results


# def filter_id(res):
#     results = dict()
#     for i in res:
#         if i[key] not in results:
#             results[i[key]] = 1
#         else:
#             results[i[key]] += 1
#     results = sorted(results.items(), key=lambda x: x[1], reverse=True)
#     results = list(map(lambda x: {key: x[0]}, results))

class ReviewedItems:
    @staticmethod
    def most_reviewed_items(first_date, second_date, number_of_items):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
                """
                SELECT product_id, product_parent, product_title, product_category FROM reviewed_items WHERE 
                review_date  >= %s and review_date <= %s ALLOW FILTERING;
                """, [first_date, second_date])

        return count_id(res, 'product_id', number_of_items)


class CustomerItems:
    @staticmethod
    def most_productive_customers(first_date, second_date, number_of_customer):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
                """
                SELECT customer_id FROM customer_review WHERE 
                review_date  >= %s and review_date <= %s AND
                verified_purchase = 'Y' ALLOW FILTERING;
                """, [first_date, second_date])
        return count_id(res, 'customer_id', number_of_customer)

    @staticmethod
    def most_productive_haters(first_date, second_date, number_of_customer):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
                """
                SELECT customer_id FROM hater_reviews WHERE 
                review_date  >= %s and review_date <= %s ALLOW FILTERING;
                """, [first_date, second_date])
        return count_id(res, 'customer_id', number_of_customer)

    @staticmethod
    def most_productive_backers(first_date, second_date, number_of_customer):
        with connections['cassandra'].cursor() as cursor:
            res = cursor.execute(
                """
                SELECT customer_id FROM backer_reviews WHERE 
                review_date  >= %s and review_date <= %s ALLOW FILTERING;
                """, [first_date, second_date])
        return count_id(res, 'customer_id', number_of_customer)
