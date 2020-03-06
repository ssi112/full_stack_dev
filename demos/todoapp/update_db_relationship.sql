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


SELECT * FROM public.todolists;

SELECT t.id, description, completed, list_id, l.name
FROM public.todos t
INNER JOIN public.todolists l
ON t.list_id = l.id
ORDER BY id;
