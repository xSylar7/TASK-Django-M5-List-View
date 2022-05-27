# Steps

1. Fork and clone [this repository](https://github.com/JoinCODED/JoinCODED-TASK-Django-M5-List-View).
2. Create a `virtual environment`.
3. Install the packages using `pip install -r dev-requirements.txt`.
4. Install `Django Rest Framework`.
5. A new app has been created for you called `flights`, your API views should be in there.
6. Create a `view` that shows a list of `Flights`:
   - Complete it so that it displays the following fields for each flight:
     - `id`
     - `destination`
     - `time`
     - `price`
   - Create a `URL` with name `flights-list` for the above view and test it in `Postman`.
7. Create a `view` that shows a list of **upcoming** `Bookings`:
   - Complete it so that it displays the following fields for each booking.
     - `flight`
     - `date`
     - `id`
   - Create a `URL` with name `bookings-list` for the above view and test it in `Postman`.
8. Push your code.
