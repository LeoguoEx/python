
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS IPPROXIES(\
                                           ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY ,\
                                           IP CHAR(20) NOT NULL, \
                                           PORT CHAR(4) NOT NULL, \
                                           PROTOCOL CHAR(4), \
                                           SPEED INT NOT NULL,\
                                           CONNECT_TIME INT NOT NULL)"""

INSERT_TABLE = """INSERT INTO IPPROXIES(IP, PORT, PROTOCOL, SPEED, CONNECT_TIME) VALUES \
                  ('%s', '%s', '%s', %d, %d)"""

DROP_TABLE = """DROP TABLE IF EXISTS IPPROXIES"""

TRUNCATE = """TRUNCATE IPPROXIES"""