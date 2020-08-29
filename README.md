# Movie Theatre Ticket Booking System

The following created is a REST interface for a movie theater ticket booking system just like that of Bookmyshow.

A "Ticket" table is created which includes:

1. ticket_id = Auto increment integer primary key for the table.
2. ticket_time = The time the user wanted to book the ticket for.
3. user_name = Name of the user who booked the tikcet.
4. user_contact = Contact number of user.
5. ticket_status = Status for validation of ticket booked

		a. Valid - The ticket has been booked for less than 8 hours.
		b. Invalid - The ticket has been marked expired by API since the ticket has been booked 			   beyond 8 hours from the time API was inovked.

The Interface allows a person to book tickets, and the booking process has a few constraints like:

1. At most 20 tickets can be booked for a particular time.
2. A ticket is only valid till the there is a maximum difference of 8 hours between the ticket time and current time.

User can make queries about checking the ticket validation or can know about the ticket details one has booked. Also the Interface provides one with the customer details like name and contact number.

APIs Supported:

1. To Book a ticket: This API call for the user name and user contact number to book a ticket for a particular time.

	Sample Request:
	```
		curl -X POST \
		http://localhost:8000/ticket/create/ \
		-H 'cache-control: no-cache' \
		-H 'content-type: application/json' \
		-H 'postman-token: 5bcc405c-1089-04e7-704f-facc0f407389' \
		-d '{
			"user_name": "paras",
			"user_contact": "9999999999",
			"timings": ["2020-08-29T13:00:00.000000Z", "2020-08-30T13:00:00.000000Z"]
		}'
	```
2. Update timing: This API uses the ticket timing and updates the timing of ticket booked.

	Sample Request:
	```
	curl -X POST \
		http://localhost:8000/ticket/update/ \
		-H 'cache-control: no-cache' \
		-H 'content-type: application/json' \
		-H 'postman-token: 3b2d85b6-775a-df64-8e2f-d70a7a9611ac' \
		-d '{
			"ticket_id": 1,
			"timing": "2020-07-29T13:00:00.000000Z"
		}'

	```

3. Tickets for a particular time: If one need to see the details and the number of tickets booked at a particular time, the this API helps to do so.

	Sample Request:
	```
	curl --location --request GET 'http://localhost:8000/ticket/get/?ticket_time=2020-08-29T13:00:00Z'

	```

4. Delete a  ticket: API provides the option to delete a particular ticket fora user.

	Sample Request:
	```
	curl -X PUT \
		http://localhost:8000/ticket/delete/ \
		-H 'cache-control: no-cache' \
		-H 'content-type: application/json' \
		-H 'postman-token: 0d4bde64-be50-a25c-85d4-db0f8b979226' \
		-d '{
			"ticket_id": 1
		}'

	```


5. User Details: The API provides the details of the user who has booked a ticket.

	Sample Request:
	```
	curl --location --request GET 'http://localhost:8000/ticket/get/1'

	```

6. Validate the Ticket: To make a ticket invalid after 8 hours.

	Sample Request:
	```
	curl -X POST \
		http://localhost:8000/ticket/expire/ \
		-H 'cache-control: no-cache' \
		-H 'content-type: application/json' \
		-H 'postman-token: b2accbf9-fcc1-5e36-4b88-dc87f3d31c0e' \
		-d '{
			"ticket_id": 2
		}'
	```
	

# Note: The screenshots can be found in the screenshot folder.
