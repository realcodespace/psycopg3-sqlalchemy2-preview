

account_city_qry = """
    SELECT ac.id, first_name, last_name, ad.city
    FROM account ac
    INNER JOIN address ad ON
        ad.account_id = ac.id
    ORDER BY random()
    LIMIT 1
"""
