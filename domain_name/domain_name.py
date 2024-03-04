def domain_name(url):
    url = url.replace('www.', '').replace('https://', '').replace('http://', '')

    url_parts = url.split('.')

    return url_parts[0]