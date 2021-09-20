django weight sort signal
=====================

django_weight_sort_signal is change order of Django signals sorting by using weight.
its help you weight signal handling with third-party apps also without changing signal class



Installation
============

#. Install django-weight-sort-signal using ``pip``::

    pip install django-weight-sort-signal

Configuration
=============


#. ``settings.py``::

    INSTALLED_APPS = [
            ...
            'django_weight_sort_signal',
        ]
    '''

Configuration for third party app signal usage
=============
#. ``settings.py``::

    INSTALLED_APPS = [
            
            'django_weight_sort_signal', #django_weight_sort_signal put into top in the INSTALLED_APPS
            'django.contrib.admin',
            'django.contrib.auth',
            ...
        ]
    '''  

    DJANGO_WEIGHT_SORT_SIGNAL ={
        'DEFAULT_SIGNAL':True, #its help you weight signal handling with third-party apps without changing signal class
        
    }

Signal 
======

#. ``signal.py``::

    from django_weight_sort_signal.dispatcher import WeightSortSignal

    order_refresh = WeightSortSignal(providing_args=["order"])

Reciever
=====
In receiver callback we can give weight to sort 

#. ``receiver.py``::

    from .signals import order_refresh

    from django_weight_sort_signal.dispatcher import receiver as weight_sort_receiver


    @weight_sort_receiver(order_refresh,weight=10)
    def tax_order_refresh(sender,order, **kwargs):
        #tax amount calculation functionality triggered on order_refresh signal dispatch
        pass


    @weight_sort_receiver(order_refresh,weight=20)
    def discount_order_refresh(sender,order, **kwargs):
        #discount amount calculation functionality triggered on order_refresh signal dispatch
        pass

    @weight_sort_receiver(order_refresh,weight=30)
    def shipping_order_refresh(sender,order, **kwargs):
        #shipping amount calculation functionality triggered on order_refresh signal dispatch
        pass


Reciever for third-party apps Eg:
=================================
In receiver callback we can give weight to sort without changing the base signal

#. ``receiver.py``::

    from django.contrib.auth.signals import user_logged_in

    def do_stuff(sender, user, request, **kwargs):
        #ADD SOME CODE 
    user_logged_in.connect(do_stuff,weight=10)

    def do_stuff2(sender, user, request, **kwargs):
        #ADD SOME CODE 
    user_logged_in.connect(do_stuff2,weight=20)

We can dispatch signal anywhere as following.

#. ::

    from .signals import order_refresh


    order = Order.objects.get(pk=10001)
    order.status="review"
    order.save()
    order_refresh.send(sender=None,order=order)





    

