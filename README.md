# Steps

1. Setup a virtual environment.
2. Fork the repository for [Django REST task 1](https://github.com/JoinCODED/REST_task_01/) in JoinCODED’s Github and Clone it.
3. Install the packages from the requirements file.
4. Install `Django Rest Framework`.
5. A new app has been created for you called `flights`, your API views should be in there.
6. Create a `view` that shows a list of `Flights`:
   - Complete it so that it displays the following fields for each flight:
     - `id`
     - `destination`
     - `time`
     - `price`
   - Create a `URL` with name `flights-list` for the above view and test it in `postman`.
   - Replace the api in the **frontends** `flights_list` view with this api.
7. Create a `view` that shows a list of **upcoming** `Bookings`:
   - Complete it so that it displays the following fields for each booking.
     - `flight`
     - `date`
     - `id`
   - Create a `URL` with name `bookings-list` for the above view and test it in `postman`.
   - Replace the api in the **frontends** `profile` view with this api.
8. Push your code
