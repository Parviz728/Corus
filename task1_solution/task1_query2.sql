select count(*) as num_of_examples from book join books_issue on book.example_id = books_issue.example_id
where name='Война и мир'
ANd
author='Л.Н.Толстой'
