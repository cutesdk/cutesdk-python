from .cache import ICache, DefaultCache


def get_access_token(app):
    # get from cache
    key = 'abc'
    cache_data = app.cache.get(key)

    return cache_data