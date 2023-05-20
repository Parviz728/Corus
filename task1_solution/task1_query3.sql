select name, count(*) as num_of_taken_books from customers 
join books_issue on customers.library_card = books_issue.library_card
where books_issue.on_date >= date_trunc('month', current_date - interval '1' month)
  and books_issue.on_date < date_trunc('month', current_date)
group by customers.name, customers.birthdate
order by num_of_taken_books DESC, customers.birthdate ASC

