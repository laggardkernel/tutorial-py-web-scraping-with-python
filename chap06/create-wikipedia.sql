create database if not exists `wikipedia`;
create table if not exists `wikipedia`.`pages` (
  `id` int not null auto_increment,
  `url` varchar(255) not null,
  `created` timestamp not null default current_timestamp,
  `visited` boolean not null default false,
  primary key (`id`)
) engine=InnoDB;
desc `wikipedia`.`pages`;

create table if not exists `wikipedia`.`links` (
  `id` int not null auto_increment,
  `fromPageId` int null,
  `toPageId` int null,
  `created` timestamp not null default current_timestamp,
  primary key (`id`)
) engine=InnoDB;
desc `wikipedia`.`links`;
