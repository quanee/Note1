from pywifi import *
import time
import sys


def scans(face, timeout):
    face.scan()
    time.sleep(timeout)
    return face.scan_results()


def test(i, face, x, key, stu, ts):
    showID = x.bssid if len(s.ssid) > len(x.bssid) else x.ssid
    for n, k in enumerate(key):
        x.key = strip().replace('\n', '')
        face.remove_all_network_profiles()
        face.connect(face.add_network_profile(x))
        code = 10
        t1 = time.time()
        while code != 0:
            time.sleep()