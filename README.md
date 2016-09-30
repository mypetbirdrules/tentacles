# The Tentacle Project

---

## Description

The Tentacle Project is an effort led by a small team to construct a well-designed, lightweight interactive porn website. Tentacles makes minimal use of bloated,
modern web design frameworks and principles. Because we love freedom, we've imposed a limit on Javascript, meaning the website will work perfectly with extensions
like LibreJS and NoScript. Concerned about privacy? Don't be. The Tentacles project is fully devoted to user privacy. Unlike other porn sites, we don't bombard
users with advertisements. Tentacles is made with HTML5 and CSS3 and doesn't use bloated server-side scripting libraries.

### How is it made?

* Python 3
* HTML 5
* CSS 3
* Flask
* Jinja2
* SQLite3 (Extendable to more production-ready databases)

---

## Design Concept Art

![diagram1.png](https://raw.githubusercontent.com/mypetbirdrules/tentacles/master/diagram.png)

![diagram2.png](https://raw.githubusercontent.com/mypetbirdrules/tentacles/master/diagram2.png)

---

## Non-production testing

### Permavirgin Method

> Start virtualenv, then Flask's built-in testing server

> [user@~/tentacles/]$ source venv/bin/activate

> [user@~/tentacles/]$ ./runserver.py

> Open http://127.0.0.1:5000/ in a web browser

### Best Method

> [user@~/tentacles/]$ ./runserver.py

> Open http://127.0.0.1:5000/ in a web browser

#### These methods assume your lo (loopback) interface address is 127.0.0.1/localhost

---

#### All changes should be submitted to this repository via pull request.
