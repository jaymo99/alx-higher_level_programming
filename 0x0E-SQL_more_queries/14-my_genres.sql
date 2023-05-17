-- list all genres of the show `Dexter`
SELECT tv_genres.name
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id = tv_genres.id
AND tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
