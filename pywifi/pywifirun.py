import pywifi
from pywifi import const
import time

# 判断是否连接到WiFi环境


def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # ifaces = wifi.interfaces
    # print(wifi)
    iface = wifi.interfaces()[0]
    # print(iface.name())
    # print(iface.status())
    iface.scan()
    bessis = iface.scan_results()
    print(bessis)
    for wf in bessis:
        print(wf.ssid)


def wificonnect(wfname, wfpwd):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(0.5)
    if iface.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = wfname
        profile.key = wfpwd
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP
        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)

        iface.connect(temp_profile)
        time.sleep(3)
        if iface.status() == const.IFACE_CONNECTED:
            print("true")
            return True
        else:
            print("false")
            return False

# gic()


wificonnect('SkyLink_01E7DD', '1234567890')
