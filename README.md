# Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M5-List-View).
2. Create a `virtual environment`.
3. Install the packages using `pip install -r dev-requirements.txt`.
4. Install `Django Rest Framework` using `pip install djangorestframework`.
<!-- Two steps are missed: the run migrations and the run server. Or you didn't add them on purpose so students have to be familiar with them till this point?-->
5. A new app has been created for you called `flights`, and your API views should be in there.
6. Create a `view` that shows a list of `Flights`, and complete it so that it displays the following fields for each flight:
   - `id`
   - `destination`
   - `time`
   - `price`
7. Create a `URL` named `flights-list` for the above view and test it in `Postman`.
8. Create a `view` that shows a list of **upcoming** `Bookings`, and complete it so that it displays the following fields for each booking.
   - `flight`
   - `date`
   - `id`
9. Create a `URL` named `bookings-list` for the above view and test it in `Postman`.
10. Push your code.
