alter database scraping character set = utf8mb4 collate = utf8mb4_unicode_ci;
alter table pages convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter table pages change title title varchar(200)
  character set utf8mb4 collate utf8mb4_unicode_ci;
alter table pages change content content varchar(10000)
  character set utf8mb4 collate utf8mb4_unicode_ci;
