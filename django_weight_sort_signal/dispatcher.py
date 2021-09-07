import django.dispatch
from django.dispatch.dispatcher import _make_id
import weakref
from django.utils.inspect import func_accepts_kwargs


def receiver(signal, **kwargs):
    """
    A decorator for connecting receivers to signals. Used by passing in the
    signal (or list of signals) and keyword arguments to connect::

        @receiver(post_save, sender=MyModel)
        def signal_receiver(sender, **kwargs):
            ...

        @receiver([post_save, post_delete], sender=MyModel)
        def signals_receiver(sender, **kwargs):
            ...
    """
    def _decorator(func):
        if isinstance(signal, (list, tuple)):
            for s in signal:
                s.connect(func, **kwargs)
        else:
            signal.connect(func, **kwargs)
        return func
    return _decorator

    
class WeightSortSignal(django.dispatch.Signal):

    def connect(self, receiver, sender=None, weak=True, dispatch_uid=None, weight=50):
        if dispatch_uid is None:
            dispatch_uid = _make_id(receiver)

        dispatch_weight_uid = f'{weight}{dispatch_uid}'
        super(WeightSortSignal, self).connect(receiver, sender=sender, weak=weak, dispatch_uid=dispatch_weight_uid)
    
    def _live_receivers(self, sender):
        self.receivers.sort()
        return super(WeightSortSignal, self)._live_receivers(sender=sender)
