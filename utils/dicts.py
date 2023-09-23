def get_val(collection, key, default="git"):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует
    В ином случае возвращается значение default
    :param collection: Словарь
    :param key: Ключ
    :param default: Значение по умолчанию, если не задавать, то git
    :return:
    """
    if type(key) in [list, dict, set, tuple]:
        return default
    elif key not in collection:
        return default
    elif key in collection:
        return collection[key]
