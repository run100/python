use douban;

CREATE TABLE IF NOT EXISTS  douban_ip_queue(
  id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  ip varchar(15) NOT NULL DEFAULT '',
  port varchar(10) NOT NULL DEFAULT '',
  lo varchar(125) NOT NULL DEFAULT '',
  isdo tinyint(1) NOT NULL DEFAULT 0,
  addtime datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS  douban_ip(
  id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  ip varchar(15) NOT NULL DEFAULT '',
  port varchar(10) NOT NULL DEFAULT '',
  lo varchar(125) NOT NULL DEFAULT '',
  addtime datetime DEFAULT NULL,
  KEY `douban_ip_i_1` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS  douban_crawl_ip(
  id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  ip varchar(15) NOT NULL DEFAULT '',
  port varchar(10) NOT NULL DEFAULT '',
  lo varchar(125) NOT NULL DEFAULT '',
  speed varchar(125) NOT NULL DEFAULT '',
  addtime datetime DEFAULT NULL,
  KEY `douban_ip_i_1` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;