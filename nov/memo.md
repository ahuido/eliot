# Specification

> Two approaches to establish the database.

1. For each book source file from Gutenberg, sort in a table:
```
create table book (
before_contents	text,
contents	text,
preface		text,
poetry_item	json,
```
```
json poetry_item
{	
	"title" : ""
	"change_notes" : ""
	"publish_notes" : ""
	"num_of_lines" : ""
	"percy_body" : ""
}
```
