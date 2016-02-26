
==========================
Leonardo leonardo-auth-kerberos
==========================

Kerberos authentication backend for Leonardo CMS.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-auth-kerberos

Configure
---------

.. code-block:: python

    # kerberos realm and service
    KRB5_REALM = 'REALM.COM'
    KRB5_SERVICE = '[hostname]/REALM.COM'

    # Enabled KDC verification defending against rogue KDC responses
    # by validating the ticket against the local keytab.
    KRB5_VERIFY_KDC = True

    # Enable case-sensitive matching between Kerberos and database user names
    KRB5_USERNAME_MATCH_IEXACT = True

    # redirect url after login
    LOGIN_REDIRECT_URL = '/'


Read More
=========

* https://github.com/django-leonardo/django-leonardo
