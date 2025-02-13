# DJANGO WEB APP “CARS”

**Tech stack**: Django, Python, PostgreSQL, HTML, CSS, NGINX, uWSGI, AWS EC2, Gemini AI, Ubuntu

- A website where users can manage car announcement profiles, adding different data about them, including images, which are kept in a PostgreSQL DB. 

- Features the use of Google’s Gemini API to enables an optional automated text-creating functionality for the cars’ descriptions;

- Manages the creation and authentication of users through Django and PostgreSQL;

- Uses AWS’ EC2 to create a virtual server that runs the application 24/7, using a fix IP (Elastic IP) and AMI’s for backup;

- In order for the web app to run successfully its architecture uses both uWSGI and NGINX to handle the exchanges between user and server, with further configurations of Ubuntu’s Systemd in order to make the server run smoothly.
