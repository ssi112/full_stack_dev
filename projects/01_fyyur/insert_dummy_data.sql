/* -----------------------------------------------
DROP TABLE public.shows;
DROP TABLE public.artists;
DROP TABLE public.venues;
DROP TABLE public.alembic_version;
----------------------------------------------- */

INSERT INTO public.artists
(name, city, state, phone, seeking_venue, seeking_description)
VALUES
('Molly & the Dragons', 'Newark', 'DE', '7175459213', TRUE, 'Looking for a hot gig');

-- DELETE FROM public.artists WHERE id = 2;
-- SELECT * FROM public.artists;

INSERT INTO public.venues
(name, city, state, address, phone, seeking_talent, seeking_description)
VALUES
('Midtown Arts Network', 'Harrisburg', 'PA', '101 S 2nd St', '7172023991', TRUE, 'Looking chicks that can rock and roll');

INSERT INTO public.venues
(name, city, state, address, phone, seeking_talent, seeking_description)
VALUES
('The Stone Balloon', 'Newark', 'DE', '1109 Stone Bridge Rd', '2051019901', TRUE, 'Seeking bands that don''t suck');

SELECT * FROM public.venues;


INSERT INTO public.shows
(venue_id, artist_id, start_time)
VALUES
(1, 1, '2020-02-11 10:10:25-07' );

SELECT * FROM public.shows;

