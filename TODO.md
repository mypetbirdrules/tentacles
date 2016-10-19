# To-Do, Reminders, and Ideas/Thoughts

---

## How this document in structured

* To-do statements and reminders will be structured in list format in Markdown
* To assign yourself to an assignment, put your name next to the list item in brackets (ex: {NAME} )
* To confirm completion of your task to other developers, put your name next to the list item in square brackets (ex: [NAME] )

---

## Database

The database schema has been decided; it is as follows:

* postTitle		(VARCHAR)
* postDescription	(VARCHAR)
* category1		(VARCHAR)
* category2		(VARCHAR)
* category3		(VARCHAR)
* videoSHA256SUM	(VARCHAR)
* yearUploaded		(SMALLINT)
* monthUploaded		(SMALLINT)

## File Storage and Organization of Uploaded Material

Each file will be stored in a folder named after each video's SHA256SUM value.

#### Example

> ┌ Root Directory
> │
> ├── a628d9fe312d8c08dcbadda0ad6ffedc75e619b0fd1bdc6bd26de57858eeafb6
> │
> ├───── video.mkv
> │      thumbnail.jpg
> │
> ├── e764a327e0882475762a5497ddb3f25f9d7b018395fae80b48969b1a59304358
> │
> └───── video.mkv
> 	 thumbnail.jpg

---

## Reminders

* For the most part, the Jinja2 templating for render_template in index.html has been done, but it needs some TLC from front-end devs
* The server used to host the site needs to be made available for initial setup stages

---

## To-Do

* A flexbox container needs to be setup and styled around the Jinja2 {% for post in posts %} statement
* The flexbox container needs to be styled with css
* ~~We still need a working database schema~~
* It may be advantageous to switch the site design to a light material theme to highlight each postObject
* We need an HTML text input field for a search function
* We need an HTML drop down menu to select from categories
* We need an HTML drop down menu to select from popularity
* We need a script to add videos to the database
	
---
