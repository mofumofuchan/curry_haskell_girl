drop table if exists user_ans;
create table user_ans (
  user_id INTEGER primary key autoincrement,
  quiz_id integer not null,
  result integer not NULL
);