from urllib.request import urlopen
import json
host = "http://localhost:8000"
api1 = "/api/v1/"
api2 = "/api/v2/"
q1 = 'review_by_customer/{}/'
q2 = 'review_by_product/{}/'
q3 = 'review_by_product/{}/{}'
q4 = 'most_reviewed_items/{}/{}/{}/'
q5 = 'most_productive_customers/{}/{}/{}/'
q6 = 'most_productive_backers/{}/{}/{}/'
q7 = 'most_productive_haters/{}/{}/{}/'
queries = [q1, q2, q3, q4, q5, q6, q7]
params = [
    ['12076615'],
    ['0300108834'],
    ['0300108834', 5],
    ['2005-01-01', '2006-08-26', 100],
    ['2005-01-01', '2006-08-26', 100],
    ['2005-01-01', '2006-08-26', 100],
    ['2005-01-01', '2006-08-26', 100],
]


def make_url(host, api, q, params):
    return host + api + q.format(*params)


def save_response_to_file(url, fileout):
    response = urlopen(url)
    decoded = response.read().decode('utf-8')
    with open(fileout, 'w', encoding='utf-8') as f:
        json_obj = json.loads(decoded)
        json.dump(json_obj, f, indent=4)


if __name__ == "__main__":
    for paramater, query in zip(params, queries):
        cassandra_url = make_url(host, api2, query, paramater)
        print(cassandra_url)
        save_response_to_file(cassandra_url, "responses/" + "cassandra_" + query[:query.find('/')] + ".json")
        db_url = make_url(host, api1, query, paramater)
        save_response_to_file(db_url, "responses/" + "postgres_" + query[:query.find('/')] + ".json")