import sys
import platform
import base64

from cefpython3 import cefpython as cef

def main():
    check_version()
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    html = ''
    with open('web/index.html', 'r+') as src:
        html = src.read()
    cef.CreateBrowserSync(url=html_to_data_uri(html), window_title='Hello World!')
    cef.MessageLoop()
    cef.Shutdown()
    

def check_version():
    assert cef.__version__ >= '57.0', 'CEF Python v57.0+ required to run this'


def html_to_data_uri(html):
    html = html.encode('utf-8', 'replace')
    b64 = base64.b64encode(html).decode('utf-8', 'replace')
    ret = 'data:text/html;base64,{data}'.format(data=b64)
    return ret


if __name__ == "__main__":
    main()
