-- When to index





-- Situation 1: looking for specific value

select
  *
from
  restaurant
where
  name = 'NaanStop';

-- But this:
--   name like '%Naan%';
-- won't be able to use the index

-- solution:

CREATE INDEX on restaurant (name);










-- Situation 2: sorting

select
  *
from
  reviewer
order by
  stars desc
limit
  5;

-- Reduce O(n * log n) time sort to O(log n):

CREATE INDEX on reviewer (stars);









-- Situation 3: join

select
	tweet.content
from
	author
inner join
	tweet on author.id = tweet.author_id
where
	author.name = 'phamous2day';






-- FIN
