import json
import urllib.parse
import urllib.request

import requests  # видимо лишний

fetch_xml_url = 'http://0.0.0.0:5000/initial_data?'   # лучше получать из cli с дефолтным значениемю Хотя бы хост-порт
fetch_xml_values = (
    ('filename', 'File1.txt'),
    ('filename', 'File2.txt'),
    ('filename', 'File3.txt'))

write_data_url = 'http://0.0.0.0:5555/xml_result'   # и это тоже из cli


def main():
    """Main controller function, controls the microservices interaction flow.

    Returns:
        str: filename.
    """
    # здесь все в try и поймать в конце исключение
    # ловить по отедльным функциям имеет смысл если
    # есть специфическая обработка
    # плюс печатая только исключение ты теряешь контекст где оно прозошло
    # и затрудняешь отладку. Так что я бы сказал что лучше его вообше не ловить
    # пусть все упадет, но будет видно где именно упало
    xml_get_result = get_xml()
    if isinstance(xml_get_result, urllib.error.HTTPError):
        return
    xml_save_result = put_xml(xml_get_result)
    if isinstance(xml_save_result, urllib.error.HTTPError):
        return
    print(xml_save_result)
    return xml_save_result   # этот return вникуда.
    # Из main имеет смысл возвращать или ничего, или инт - код возврата
    # и тогда писать exit(main(sys.argv)) внизу
    # если нужно что-то возвращать - нужно завести еще одну функцию,
    # куда положить весь этот код и дергать ее из main
    # а в main - только парсинг CLI(его тоже лучше отдельно положить)
    # и вызов функции, которая все это делает


def get_xml():
    """Fetch xml from fetch_xml service.

    Returns:
        dict: XML string.
    """
    try:
        url_params = urllib.parse.urlencode(fetch_xml_values)
        request = urllib.request.Request(fetch_xml_url + url_params)
        response = urllib.request.urlopen(request)
        # data = urllib.request.urlopen(fetch_xml_url + url_params).read()
        result = binary_to_dict(response.read())
        return result  # result - лишняя переменная
    except urllib.error.HTTPError as e:  # лучше ловить и печатать прямо в main
        print(e)
        return e


def put_xml(xml_str_to_save):
    """Perform PUT request to write_data microservice to save XML.

    Args:
        xml_str_to_save (dict): dict containing XML string to write to file.

    Returns:
        str: filename.
    """
    # тут почти тоже, что и в get_xml - я бы убрал try/except и сократил
    # несколько строк, например без переменной response можно обойтись,
    # хотя это мелочь
    try:
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps(xml_str_to_save).encode('utf8')
        request = urllib.request.Request(
            url=write_data_url, data=payload,
            method='PUT', headers=headers)
        # request = urllib.request.Request(
        #     url=write_data_url,
        #     data=json.dumps(xml_str_to_save).encode('utf8'),
        #     method='PUT',
        #     headers={'Content-Type': 'application/json'})        
        response = urllib.request.urlopen(request)
        result = binary_to_dict(response.read())
        return result
    except urllib.error.HTTPError as e:
        print(e)
        return e


def binary_to_dict(binary_data):
    """Convert binary data to dictionary.

    Args:
        binary_data (binary): data to convert.

    Returns:
        dict: data converted to dict.
    """
    decoded_res = binary_data.decode('ascii')
    result = json.loads(decoded_res)
    return result   # return json.loads(binary_data.decode('ascii'))


if __name__ == '__main__':
    main()  # exit(main(sys.argv))
