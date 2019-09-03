# Matt Hudson - CS4830 Fall '19 - Tuesday Week 3 Lab

## Requirements for newspaper photographic manager application
( first person - making the original document )

**Stakeholders** - photographers, editors, journalists and journalism companies (CNN, NBC, FOX, etc)

## System Requirements

	- The system will need a database management system to store information including keywords, date, filepath
	- Interface (Web based and/or mobile application)
	- Storage space to centrally store image files
	- Organize images based on keywords in filesystem
	- Aspect ratio limitations on uploaded image



## Functional Requirements

	- Editors and Journalists
		- Editors can submit placeholder image in news articles
		- Editors can replace placeholder images with other images
		- Editors should be able to add and check copyright information on images
		- Editors can search for images based on keyword and/or date
		- Journalists will be notified if they try to publish an article containing placeholder images
	- Photographers
		- Photographers can upload images to a central repository from a web or mobile application
		- Photographers can add keywords and date of the image when uploading
		- Photographers can specify which placeholder image their uplaod will replace
	- System
		- The system will remove outdated images based on keywords
		- The system will reject images with a non-standard aspect ratio
		
