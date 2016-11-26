drop table if exists entries;
create table entries (
  quiz_id integer primary key autoincrement,
  result integer not NULL
);