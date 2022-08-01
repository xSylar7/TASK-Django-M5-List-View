# Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M5-List-View).
2. Create a `virtual environment`.
3. Install the packages using `pip install -r dev-requirements.txt`.
4. Install `Django Rest Framework` using `pip install djangorestframework`.
5. Migrate and run your server.
6. A new app has been created for you called `flights`, and your API views should be in there.
7. Create a `view` that shows a list of `Flights`, and complete it so that it displays the following fields for each flight:
   - `id`
   - `destination`
   - `time`
   - `price`
8. Create a `URL` named `flights-list` for the above view and test it in `Postman`.
9. Create a `view` that shows a list of **upcoming** `Bookings`, and complete it so that it displays the following fields for each booking.
   - `flight`
   - `date`
   - `id`
10. Create a `URL` named `bookings-list` for the above view and test it in `Postman`.
11. Push your code.
