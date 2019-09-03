# Matt Hudson - CS4830 Fall '19 - Tuesday Week 3 Lab

## Requirements for newspaper photographic manager application
( first person - making the original document )

**Stakeholders** - photographers, editors, journalists and journalism companies (CNN, NBC, FOX, etc)

## System Requirements

	- The system will need a database management system to store information including keywords, date, and filepath.
	- The system will need an interface (Web based and/or mobile application) for photographers to upload images and editors to use those images.
	- The system will require sufficient storage space to centrally store image files.
	- The filesystem of the server will organize images based on keywords in filesystem.
	- The server will impose aspect ratio limitations on uploaded images.



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

