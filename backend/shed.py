# -*- coding: cp1251 -*-
#print 'Content-Type: text/plain'
#print ''
import urllib2
import re
res = urllib2.urlopen("http://volnorez.com/bigboss-fm").read()
p = re.compile('class=\"afisha_sidebar_container\">.*([^<>]+?)</div>')
match = re.search( p, res )
print """
<html>
<head>
<link href="http://radio-bigboss-fm.narod.ru/style.css" rel="stylesheet"type="text/css" />
</head>
<body>
"""
try:
    print "<div "+ match.group()
except AttributeError:
         print "Расписания на сегодня нет. Пока нет :)"
else:
    print """
    </body>
    </html>
    """
