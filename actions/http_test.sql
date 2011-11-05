-- This file is part of Bunk.
-- Copyright (c) 2011 Brandon Orther. All rights reserved.
--
-- The full license is available in the LICENSE file that was distributed with this source code.

-- --
-- Bunk http_test SQL
-- --

-- create bunk_db database
create database bunk_db;

-- create bunk user and grant privileges to bunk_db
grant usage on *.* to bunk@localhost identified by 'RESTing';
grant all privileges on bunk_db.* to bunk@localhost;
flush privileges;

-- create http_test table
use bunk_db;
CREATE TABLE IF NOT EXISTS `http_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `route_id` varchar(255) NOT NULL,
  `request_ip` varchar(30) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1;
