SELECT b.id,
       b.name
FROM book AS b
INNER JOIN rent AS r
    ON b.id = r.id_book
WHERE r.status = 'Overdue';