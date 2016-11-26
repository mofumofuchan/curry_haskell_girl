drop table if exists user_ans;
create table quiz(
  quiz_id integer primary key autoincrement,
  quiz_name string not null,
  quiz_text string not null,
  quiz_hint string not null,
  quiz_ans string not null
);

create table user (
  user_id integer primary key autoincrement,
  user_name stirng not null,
  user_answers string not null
);