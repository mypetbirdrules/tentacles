# To-Do, Reminders, and Ideas/Thoughts

---

## How this document in structured

* To-do statements and reminders will be structured in list format in Markdown
* To assign yourself to an assignment, put your name next to the list item in brackets (ex: {NAME} )
* To confirm completion of your task to other developers, put your name next to the list item in square brackets (ex: [NAME] )

---

## Ideas for Database Schema

> CREATE TABLE posts VALUES(postID integer primary key autoincrement, postTitle text, postDescription text, dateAdded text, categories integer)

### Categories can be stored as combinations of prime numbers, and multiple categories can fit into one number. For example:

> 3 = Asian

> 5 = BBC

> 7 = Lesbian

### A video/image with all three of these attributes becomes:

> 3 * 5 * 7 = 105 = Asian && BBC && Lesbian


---

## Reminders

* For the most part, the Jinja2 templating for render_template in index.html has been done, but it needs some TLC from front-end devs
* The server used to host the site needs to be made available for initial setup stages

---

## To-Do

* A flexbox container needs to be setup and styled around the Jinja2 {% for post in posts %} statement
* The flexbox container needs to be styled with css
* We still need a working database schema
* It may be advantageous to switch the site design to a light material theme to highlight each postObject
* We need an HTML text input field for a search function
* We need an HTML drop down menu to select from categories
* We need an HTML drop down menu to select from popularity
* We need a script to add videos to the database

---
