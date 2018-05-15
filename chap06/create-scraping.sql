create database if not exists scraping;
use scraping;

create table if not exists pages(
  id bigint(7) not null auto_increment,
  title varchar(200),
  content varchar(10000),
  created timestamp default current_timestamp,
  primary key(id)
) ENGINE=InnoDB;

describe pages;

INSERT INTO pages (title, content) VALUES ("Test page title",
"This is some test page content. It can be up to 10,000 characters long.");

INSERT INTO pages (id, title, content, created) VALUES (2,
"Test page title",
"This is some test page content. It can be up to 10,000 characters long.",
"2014-09-21 10:25:32");

SELECT * FROM pages WHERE id = 2;
SELECT * FROM pages WHERE title LIKE "%test%";
SELECT id, title FROM pages WHERE content LIKE "%page content%";
UPDATE pages SET title="A new title",
content="Some new content" WHERE id=2;
SELECT * FROM pages\G
