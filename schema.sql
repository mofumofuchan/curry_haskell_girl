drop table if exists user_ans;
create table quiz(
  quiz_id integer primary key autoincrement,
  quiz_name text not null,
  quiz_text text not null,
  quiz_hint text not null,
  quiz_ans text not null
);

create table user (
  user_id integer primary key autoincrement,
  user_name text not null
);

create table answers (
  user_id integer not null,
  answered integer not null
);

create table story (
  quiz_section_id integer not null,
  section_story text not null
)