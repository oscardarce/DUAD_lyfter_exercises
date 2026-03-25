SELECT a.id,
    a.name AS author_name,
    b.name AS book_name
FROM author AS a
    INNER JOIN book AS b ON a.id = b.id_author;