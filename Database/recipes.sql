/*
SQLyog - Free MySQL GUI v5.0
Host - 5.0.16-nt : Database - recipes
*********************************************************************
Server version : 5.0.16-nt
*/


create database if not exists `recipes`;

USE `recipes`;

/*Table structure for table `customer_customeringredientsmodel` */

DROP TABLE IF EXISTS `customer_customeringredientsmodel`;

CREATE TABLE `customer_customeringredientsmodel` (
  `id` int(11) NOT NULL auto_increment,
  `loginid` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `ingredients` varchar(100) NOT NULL,
  `recipes` varchar(100) NOT NULL,
  `descriptions` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `customer_customeringredientsmodel` */

insert into `customer_customeringredientsmodel` values 
(19,'Meghana','arumallameghana7@gmail.com','butter,chicken','Butterchicken','No Data found','sent','notassigned'),
(20,'Meghana','arumallameghana7@gmail.com','garammasala,Cauliflower,turmeric','Aloogobi','No Data found','waiting','notassigned'),
(21,'Meghana','arumallameghana7@gmail.com','garammasala,Cauliflower,turmeric','Chicken65','No Data found','sent','notassigned'),
(22,'Meghana','arumallameghana7@gmail.com','garammasala,Cauliflower,turmeric','Aloogobi','No Data found','waiting','notassigned'),
(23,'Meghana','arumallameghana7@gmail.com','garammasala,Cauliflower,turmeric','Chicken65','No Data found','waiting','notassigned'),
(24,'Maggi','meghana@gmail.com','Onions,chicken','Eggomelette','No Data found','waiting','notassigned'),
(25,'Maggi','meghana@gmail.com','Onions,chicken','Butterchicken','No Data found','sent','notassigned');

/*Table structure for table `customer_customerregistrationmodel` */

DROP TABLE IF EXISTS `customer_customerregistrationmodel`;

CREATE TABLE `customer_customerregistrationmodel` (
  `id` int(41) NOT NULL auto_increment,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `loginid` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `authkey` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `customer_customerregistrationmodel` */

insert into `customer_customerregistrationmodel` values 
(1,'Meghana','Arumalla','Meghana','123','arumallameghana7@gmail.com','9676358258','Vijayawada','Ap','12720078','activated'),
(2,'Nandana','Arumalla','Nandana','123','nandana@gmail.com','9247129626','Vijayawada','AP','91240350','activated'),
(3,'Maggi','Meghu','Maggi','123','meghana@gmail.com','7780110618','Hyderabad','Telagana','24071176','activated'),
(4,'teju','Teju','Teju','123','teju@gmail.com','7780110618','Htd','Telagana','27163172','activated');

/*Table structure for table `customer_recommendmodel` */

DROP TABLE IF EXISTS `customer_recommendmodel`;

CREATE TABLE `customer_recommendmodel` (
  `id` int(11) NOT NULL auto_increment,
  `email` varchar(100) NOT NULL,
  `recommend` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `customer_recommendmodel` */

insert into `customer_recommendmodel` values 
(1,'arumallameghana7@gmail.com','nice'),
(2,'nandana@gmail.com','This item is verynice'),
(3,'arumallameghana7@gmail.com','gy'),
(4,'nandana@gmail.com','Wanna try this one'),
(5,'arumallameghana7@gmail.com','once try it..');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert into `django_session` values 
('3js0p1ejnl9yy52g0qwltanx0mhipagr','YTA5MjQ0YmFiYTU3YjIzNjBiNWM3YmQzMWU4Y2Y2MmJjZjFjMDA1MDp7ImN1c3RvbWVyaWQiOiJNZWdoYW5hIiwiZW1haWwiOiJhcnVtYWxsYW1lZ2hhbmE3QGdtYWlsLmNvbSJ9','2019-09-04 05:50:14'),
('4qjtfzou1t0ewaa659eh15nkq5repik4','YTA5MjQ0YmFiYTU3YjIzNjBiNWM3YmQzMWU4Y2Y2MmJjZjFjMDA1MDp7ImN1c3RvbWVyaWQiOiJNZWdoYW5hIiwiZW1haWwiOiJhcnVtYWxsYW1lZ2hhbmE3QGdtYWlsLmNvbSJ9','2019-09-04 07:18:13'),
('aong53pgm3u7eu7vhd85jln5xc5psh20','ZTA1NWIxMjM5YjQ5M2NmYTY0MzUwNGQyMWVkY2NhYTgwYzUzMjRiZDp7ImN1c3RvbWVyaWQiOiJNZWdoYW5hIiwiZW1haWwiOiJuYW5kYW5hQGdtYWlsLmNvbSIsImlkIjoiTmFuZGFuYSJ9','2019-09-03 09:31:36'),
('byoa81vbxsnpa38oqfp0zubtatwcjgqz','MjVlN2U4NTFlY2NmMDkwMmNjYmIxMTg3MzIyZTg1MmJlMGNlN2E5Mjp7ImlkIjoiTWVnaGFuYSIsImVtYWlsIjoiYXJ1bWFsbGFtZWdoYW5hN0BnbWFpbC5jb20iLCJjdXN0b21lcmlkIjoiTWVnaGFuYSJ9','2019-09-09 04:24:45'),
('k1p9m4q7v5or83qe0nprwsufsfj5ejwi','ZjEyMTk3OGY1MmU0YTMxNzJiMjc3YzdjY2I1Y2NmNzg4YTM0ZTgxODp7ImlkIjoiTmFuZGFuYSIsImVtYWlsIjoibmFuZGFuYUBnbWFpbC5jb20iLCJjdXN0b21lcmlkIjoiTWVnaGFuYSJ9','2019-09-04 08:45:51'),
('tukpgqtqnmgrt1xzvzbi2haqae3altwr','MjViM2E3Mjk4MDcwM2Q2ZTc0YzVjNDM3N2QyOWM5YWYzNzUwMGIzNjp7ImlkIjoiTmFuZGFuYSIsImVtYWlsIjoiYXJ1bWFsbGFtZWdoYW5hN0BnbWFpbC5jb20iLCJjdXN0b21lcmlkIjoiTWVnaGFuYSJ9','2019-09-04 04:16:58');

/*Table structure for table `foodcourt_addrecipemodel` */

DROP TABLE IF EXISTS `foodcourt_addrecipemodel`;

CREATE TABLE `foodcourt_addrecipemodel` (
  `id` int(11) NOT NULL auto_increment,
  `recipename` varchar(100) NOT NULL,
  `ingredients` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `file` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `foodcourt_addrecipemodel` */

insert into `foodcourt_addrecipemodel` values 
(1,'Chicken','chicken,garlic past,chilli powder,oil,salt.','yummy','files/pdfs/meghana_4YrBsC2.mp4'),
(2,'ChilliCapsicum','capsicum,chilli','nice','files/pdfs/CHILLI_CAPSICUM_-_CAPSICUM_MASALA_-_CAPSICUM_DRY_FRY_-_EASY_CAPSICUM_RECIPE_1.mp4'),
(3,'EggCurry','egg,tomato,onions','tasty','files/pdfs/meghana.mp4');

/*Table structure for table `foodcourt_foodcourtregistrationmodel` */

DROP TABLE IF EXISTS `foodcourt_foodcourtregistrationmodel`;

CREATE TABLE `foodcourt_foodcourtregistrationmodel` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `loginid` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `authkey` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `foodcourt_foodcourtregistrationmodel` */

insert into `foodcourt_foodcourtregistrationmodel` values 
(1,'Nandana','Nandana','123','nandana@gmail.com','9247129626','Vijayawada','68582453','activated'),
(2,'Meghana','Meghana','123','arumallameghana7@gmail.com','9676358258','Hyderabad','41036796','activated'),
(3,'Teju','Teju','123','teju@gmail.com','7780110618','Hyd','42290866','activated');
