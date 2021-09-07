=====================
django-cropper-image
=====================


django_weight_sort_signal is change order of Django signals sorting by using weight



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

        
We can dispatch signal anywhere as following.

#. ::

    from .signals import order_refresh


    order = Order.objects.get(pk=10001)
    order.status="review"
    order.save()
    order_refresh.send(sender=None,order=order)





    

