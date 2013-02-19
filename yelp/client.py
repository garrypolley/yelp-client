# -*- coding: utf-8 -*-

from urlparse import urljoin

import requests
from requests_oauthlib import OAuth1

# Attempt to get settings from Django
try:
    from django.conf import settings
except ImportError:
    settings = {}


BASE_API_URL = u'http://api.yelp.com/v2/'
SEARCH_API_URL = urljoin(BASE_API_URL, 'search/')

# Set our default values for our client
CONSUMER_KEY = getattr(settings, 'YELP_CONSUMER_KEY', None)
CONSUMER_SECRET = getattr(settings, 'YELP_CONSUMER_SECRET', None)
TOKEN = getattr(settings, 'YELP_TOKEN', None)
TOKEN_SECRET = getattr(settings, 'YELP_TOKEN_SECRET', None)


class YelpClient(object):
    """
    A simple client wrapper around the yelp v2 apis.
    """

    def __init__(self, client_key=CONSUMER_KEY,
                       client_secret=CONSUMER_SECRET,
                       resource_owner_key=TOKEN,
                       resource_owner_secret=TOKEN_SECRET):
        """
        Override init so default values can be passed to create
        a valid yelp client.  If using django set these values in
        your settings.py See the yelp docs for your keys:
        http://www.yelp.com/developers/request_apiv2_key

        Django settings
        ===============

        * YELP_CONSUMER_KEY := the yelp consumer key
        * YELP_CONSUMER_SECRET := the yelp consumer secret
        * YELP_TOKEN := the yelp token
        * YELP_TOKEN_SECRET := the yelp token secret

        Parameters
        ==========

        * client_key := the yelp consumer key
        * client_secret := the yelp consumer secret
        * resource_owner_key := the yelp token
        * resource_owner_secret := the yelp token secret

        """
        pass
