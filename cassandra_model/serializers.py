def review_to_dict(review):
    return {
        "review_headline": review.review_headline,
        "helpful_votes": review.helpful_votes,
        "star_rating": review.star_rating,
        "review_body": review.review_body,
        "review_date": str(review.review_date)
    }


def review_serialize(res):
    res = list(res)
    for i in res:
        i['review_date'] = str(i['review_date'])
        # i['review'] = review_to_dict(i['review'])
    return res
