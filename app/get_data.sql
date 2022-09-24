SELECT
    a.name,
    b.price
FROM my_project.my_dataset.my_table AS a
LEFT JOIN my_project.my_dataset.another_table AS b
    ON a.article_id = b.article_id
