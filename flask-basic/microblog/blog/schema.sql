/**
 * @Author: lucky
 * @Date:   2017-04-12T23:50:03+08:00
 * @Last modified by:   lucky
 * @Last modified time: 2017-04-12T23:51:28+08:00
 */



drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
