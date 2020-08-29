Movie Theatre Ticket Booking System

The following created is a REST interface for a movie theater ticket booking system just like that of Bookmyshow

A "Ticket" table is created which includes:

1. ticket_id = Ticket Id.
2. ticket_time = The time when the ticket was booked.
3. user_name = Name of the user who booked the tikcet.
4. user_contact = Contact number of user.
5. ticket_status = Status for validation of ticket booked.

The framework allows a person to book tickets, and the booking process has a few constraints like:

1. At most 20 tickets can be booked fora particular timespan.
2. A ticket is only valid till the there is a maximum difference of 8 hours between the ticket time and current time.

User can make queries about checking the ticket validation or can know about the ticket details one has booked. 

Also the framework provides one with the customer details like name and contact number.

APIs Created:

1. To Book a ticket: This API call for the user name and user contact number to book a ticket for a particular time.
	URL: 

2. Update timing: This API uses the ticket timing and updates the timing of ticket booked.
	URL: 
	
3. Tickets for a particular time: If one need to see the details and the number of tickets booked at a particular time, the this API helps to do so.
	URL: 

4. Delete a  ticket: API provides the option to delete a particular ticket fora user.
	URL: 

5. User Details: The API provides the details of the user who has booked a ticket.
	URL:

6. Validate the Ticket: To check weather a ticket is valid or not, this API helps a user.
	URL: 