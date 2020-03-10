--DELETE FROM public.todos;

INSERT INTO public.todolists
(id, name)
VALUES(1, 'Uncategorized');


-- update table & add foreign key reference
ALTER TABLE public.todos
ADD list_id INTEGER NOT NULL REFERENCES todolists(id);

-- add new row with foreign key just added
INSERT INTO public.todos
(id, description, completed, list_id)
VALUES(1, 'Fix Udacity mistakes', FALSE, 1);

INSERT INTO public.todos
(id, description, completed, list_id)
VALUES(2, 'Finish Lesson #7', FALSE, 1);


INSERT INTO public.todolists
(id, name)
VALUES(2, 'Urgent');

INSERT INTO public.todos
(id, description, completed, list_id)
VALUES(3, 'Dust my broom', FALSE, 2);

INSERT INTO public.todos
(id, description, completed, list_id)
VALUES(4, 'Eat veggies', FALSE, 2);


SELECT * FROM public.todolists;

SELECT t.id, description, completed, list_id, l.id, l.name
FROM public.todos t
RIGHT JOIN public.todolists l
ON t.list_id = l.id
ORDER BY l.id, t.id
