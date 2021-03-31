# BIG Data Homework 1


1) Діаграми знаходяться в директорії diagrams


2-3) Скрипти знаходяться в файлах cassandra_scripts.txt і postgres_scripts.txt


6) Результати в директорії - scripts/results

API має наступний вигляд 

(version can be v1 - postgres and v2 - cassandra)

q1 - http://host:port/api/version/review_by_customer/<id>/
q2 - http://host:port/api/version/review_by_product/<id>/
q3 - http://host:port/api/version/review_by_product/<id>/<star_rating>
q4 - http://host:port/api/version/most_reviewed_items/<first_date>/<second_date>/<N>/
q5 = http://host:port/api/version/most_productive_customers/<first_date>/<second_date>/<N>/
q7 = http://host:port/api/version/most_productive_backers/<first_date>/<second_date>/<N>/
q8 = http://host:port/api/version/most_productive_haters/<first_date>/<second_date>/<N>/
