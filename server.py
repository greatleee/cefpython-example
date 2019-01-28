import sys
import platform
import base64
import ctypes
import threading

from cefpython3 import cefpython as cef


def main():
    sys.excepthook = cef.ExceptHook
    app_settings = {
    }
    cef.Initialize(settings=app_settings)

    browser_settings = {
    }
    browser = cef.CreateBrowserSync(url='file:///web/index.html',
                                    settings=browser_settings,
                                    window_title='Hello World!')
    if platform.system() == "Windows":
        window_handle = browser.GetOuterWindowHandle()
        insert_after_handle = 0
        # X and Y parameters are ignored by setting the SWP_NOMOVE flag
        SWP_NOMOVE = 0x0002
        # noinspection PyUnresolvedReferences
        ctypes.windll.user32.SetWindowPos(window_handle, insert_after_handle,
                                          0, 0, 700, 200, SWP_NOMOVE)
    set_javascript_bindings(browser)
    cef.MessageLoop()
    cef.Shutdown()


class External():
    target_dir_path = ''
    def __init__(self, browser):
        self.browser = browser

    def ask_dir_path(self):
        from tkinter.filedialog import askdirectory
        from tkinter import Tk 
        Tk().withdraw()
        self.target_dir_path = askdirectory()
        self.browser.ExecuteFunction('updatePath', self.target_dir_path)


def py_confirm(path):
    print('success: ' + path)


def set_javascript_bindings(browser):
    external = External(browser)
    bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
    bindings.SetFunction('py_confirm', py_confirm)
    bindings.SetObject('external', external)
    browser.SetJavascriptBindings(bindings)


if __name__ == "__main__":
    main()