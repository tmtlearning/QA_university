def __tripple_to_dict(string):
    '''Вспомогательная функция. Представляет триплексную строку в виде
    внутреннего типа данных "словарь" вида {(pref, name): value}.'''
    dic = {}
    pref = []
    index = []
    value = []

    string = string.replace('$', '')
    arr = string.split(';')
    arr = list(map(lambda x: x.split('='), arr))
    for n in arr:
        n[0] = n[0].split('.')
    del(arr[-1])
    for x in range(len(arr)):
        n = arr[x]
        pref.append(n[0][0])
        index.append(n[0][1])
        value.append(n[1])
    dic = dict(zip(list(zip(pref, index)), value))
    return dic


def __dict_to_tripple(dict):
    '''Вспомогательная функция. Преобразует словарь в триплексную строку.'''
    string = ''
    for x in dict:
        string += '$' + x[0] + '.' + x[1] + '=' + dict[x] + ';'
    return string


def __to_tripple(pref, name, value):
    '''функция формирует триплет из заданных значений префикса, имени и значения.'''
    if type(value) == str:
        value = '\'' + value + '\''
    triplet = pref + '.' + name + '=' + str(value) + ';'
    return triplet


def add_to_tripple(item, string):
    dic = __tripple_to_dict(string)
    new_item = __tripple_to_dict(item)
    res = dict(list(dic.items()) + list(new_item.items()))
    return __dict_to_tripple(res)


def trpsort(tripple):
    '''функция сортирует триплеты в триплексной строке по префиксу'''
    dict = __tripple_to_dict(tripple)
    res = sorted(dict.items())
    return res


def trpdelpref(key, tripple):
    '''функция удаляет триплеты с указанным префиксом из триплексной строки'''
    dict = __tripple_to_dict(tripple)
    res = {k: v for k, v in dict.items() if key not in k}
    return __dict_to_tripple(res)


def trpmergestr(firststr, secondstr):
    '''функция объединяет две триплексные строки'''
    result = add_to_tripple(firststr, secondstr)
    return result


def del_trp(pref, name, trpstr):
    '''функция удаляет из триплесной строки триплет с заданным значением префикса и имени'''
    dict = __tripple_to_dict(trpstr)
    res = {k: v for k, v in dict.items() if ((pref not in k[0]) or (name not in k[1]))}
    return res


def trpadd(trpstr, pref, name, value):
    '''Функция формирует триплет из заданных параметров pref, name, value
    и добавляет его в триплексную строку trpstr. В данной фунции реализуется
    добавления как строковых значение value, так и целочисленных, то есть
    реализация дополнительных фунцкций trpaddint и trpaddstr не требуется'''
    trp = __to_tripple(pref, name, value)
    print (trp)
    return add_to_tripple(trp, trpstr)


def trpget(trpstr, pref, name):
    '''Фунция ищет триплет с заданными pref, name в триплексной строке
     и возвращает кортеж вида (True, значение), если триплет присутствует
     в заданной строке, в противном случает возращает (False, None). Прототип
     функции изменен по сравнению с предложенным изначально из-за различий в
     языках С и Python. При программировании в функциональном стиле на Python
     рекомендуется избегать изменения передаваемых аргументов. '''
    temp = __tripple_to_dict(trpstr)
    try:
        value = temp[(pref, name)]
        return (True, value)
    except KeyError:
        return (False, None)


def trpSetStr(first, second):
    '''функция аналогична trpmergesrt, выполняет слияние двух триплексных строк'''
    result = add_to_tripple(firststr, secondstr)
    return result
