Yelp (yelp-client)
==================

.. contents:: Table of Contents

A simple wrapper around the version 2 YelpAPIs_

Not yet completed

Installation
-------------

Via pip:
    pip install yelp


Configuration
--------------
Settings for Django settings.py.  Key values found at `http://www.yelp.com/developers/request_apiv2_key`
::
    YELP_CONSUMER_KEY = ''
    YELP_CONSUMER_SECRET = ''
    YELP_TOKEN = ''
    YELP_TOKEN_SECRET = ''


Or call the client with the 4 arguments above:
::
    yelp_client = yelp.client(client_key=YELP_CONSUMER_KEY,
                              client_secret=YELP_CONSUMER_SECRET,
                              resource_owner_key=YELP_TOKEN,
                              resource_owner_secret=YELP_TOKEN_SECRET)


Usage
------

All of the names listed on the SearchAPI_ page are attributes you may set on the yelp_client.

.. _YelpAPIs: http://www.yelp.com/developers/documentation/v2/overview
.. _SearchAPI: http://www.yelp.com/developers/documentation/v2/search_api
