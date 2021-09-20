from django.conf import settings

def set_default_signal():
    if hasattr(settings, 'DJANGO_WEIGHT_SORT_SIGNAL'):
        if settings.DJANGO_WEIGHT_SORT_SIGNAL.get('DEFAULT_SIGNAL',False):
            from django import dispatch
            from django_weight_sort_signal import dispatcher

            dispatch.Signal = dispatcher.WeightSortSignal

    