# import win32api
# import win32con
# import time
#
# time.sleep(2)
# win32api.keybd_event(win32con.VK_NUMPAD7,
#                      win32api.MapVirtualKey(win32con.VK_NUMPAD7,3),
#                      win32con.KEYEVENTF_EXTENDEDKEY,
#                      0)  # press
# win32api.Sleep(50)
# win32api.keybd_event(win32con.VK_NUMPAD7,
#                      win32api.MapVirtualKey(win32con.VK_NUMPAD7,3),
#                      win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP,
#                      0)  # r