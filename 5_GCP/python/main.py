import functions_framework
import requests

@functions_framework.http
def hello_http(request):
    print('Hello World')
    return 'Hello Billy Bob Joe'