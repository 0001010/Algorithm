select
  t1.artist_id,
  name
from
  (
    select
      artist_id,
      name
    from
      artists
    where
      death_year is not null
  ) as t1
  left join (
    select distinct
      (artist_id) as artist_id
    from
      artworks_artists
  ) as t2 on (t1.artist_id = t2.artist_id)
where
  t2.artist_id is null;