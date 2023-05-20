select press_city, count(*) as num_of_books from book
where extract(year from date_of_comming) = 2021
group by press_city
HAVING count(*) > 0
order by num_of_books DESC
