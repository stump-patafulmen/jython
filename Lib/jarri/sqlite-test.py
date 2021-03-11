#!/usr/bin/jython
# -*- coding: utf-8 -*-

from com.ziclix.python.sql import zxJDBC

jdbc_url = r"jdbc:sqlite:sample.sqlite.db"
username = None
password = None
driver   = "org.sqlite.JDBC"


if __name__ == '__main__' :
    # obtain a connection using the with-statement
    with zxJDBC.connect( jdbc_url, username, password, driver ) as conn :
        with conn :
            print( 'connected' )

