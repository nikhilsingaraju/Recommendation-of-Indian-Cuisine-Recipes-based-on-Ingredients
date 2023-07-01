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

/*Table structure for table `customer_recommendmodel` */

DROP TABLE IF EXISTS `customer_recommendmodel`;

CREATE TABLE `customer_recommendmodel` (
  `id` int(11) NOT NULL auto_increment,
  `email` varchar(100) NOT NULL,
  `recommend` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
