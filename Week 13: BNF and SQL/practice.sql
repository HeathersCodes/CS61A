create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";
   
select 'west coast' as region, name from cities where longitude >= 115 union
select 'other',                name from cities where longitude <  115;

/*scratch*/
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";
  
/*projecting table*/
select child from parents where parent = "abraham";
select * from parents where parent = "abraham";

/*Arithmetic
sqlite3 -init x.sql
*/
create table lift as
  select 101 as chair, 2 as single, 2 as couple union
  select 102         , 0          , 3           union
  select 103         , 4          , 1;

select chair, single + 2 * couple as total from lift;
/* Table
*/
CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur UNION
  SELECT "barack"         , "short"       UNION
  SELECT "clinton"        , "long"        UNION
  SELECT "delano"         , "long"        UNION
  SELECT "eisenhower"     , "short"       UNION
  SELECT "fillmore"       , "curly"       UNION
  SELECT "grover"         , "short"       UNION
  SELECT "herbert"        , "curly";
/* parent in parents */ 
SELECT parent FROM parents, dogs WHERE child = name AND fur = "curly";
SELECT * FROM parents, dogs WHERE child = name AND fur = "curly";

select * from parents, dogs; /* get all arrangement */

/* from <table> gives power to use every info in table
   as gives power to have another name to use in sql */
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child; /* also first < second works */
  
 select 'hello,' || 'world'
 create table phrase as select 'hello, world' as s;
 select substr(s, 4,2) || substr(s, instr(s,'')+1,1) from phrase;
 /* <> different from */

CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42,              71,              "Cambridge"        UNION
  SELECT 45,              93,              "Minneapolis"      UNION
  SELECT 33,             117,              "San Diego"        UNION
  SELECT 26,              80,              "Miami"            UNION
  SELECT 90,               0,              "North Pole";

CREATE TABLE cold AS
  SELECT name FROM cities WHERE latitude > 43 UNION
  SELECT "Chicago";

SELECT name, "is cold!" FROM cold;

CREATE TABLE distances AS
  SELECT a.name AS first, b.name AS second,
         60*(a.latitude-b.latitude) AS distance
         FROM cities AS a, cities AS b
         WHERE a.name != b.name  /* or <> */
         ORDER BY a.longitude;

SELECT second FROM distances WHERE first="Minneapolis" ORDER BY -distance; /* or DESC */



