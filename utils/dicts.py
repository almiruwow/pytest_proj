def get_val(collection, key, default='git'):
    if len(collection) == 0 or collection.get(key) is None:
        return default
    else:
        return collection.get(key)
