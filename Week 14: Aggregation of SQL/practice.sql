create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;

select max(legs) from animals;

select sum(weight) from animals;

select max(legs - weight) + 5 from animals;

select min(legs), max(weight) from animals where kind <> "t-rex";

select max(legs) + min(weight) from animals;


select count(legs) from animals;

select count(*) from animals; /* 6 */

select count(distinct legs) from animals; /* 20 6 10 12000 */

select kind, max(weight) from animals; /* "t-rex" 12000 */

select kind, max(legs) from animals; /* 4 "cat" not excatly right answer */

select kind, avg(weight) from animals; /* 2009.33 "t-rex" not give meaningful value */
/*having clause filter the set of groups */
select weight/legs, count(*) from animals group by weight/legs having count(*)>1;

select max(legs)-min(legs) as diff from animals group by weight order by -diff limit 1;

select kind, max(legs)-min(legs) from animals group by weight order by -diff limit 6;
/* Notes: 4 rows, so display 4 rows */

/* 
select some columns from different tables to get a new table.
merge: left if right does not have the rows that left has, will be auto created
inner: get rows 2 table both have
*/
