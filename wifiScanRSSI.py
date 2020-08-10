import rssi

# scan for a specific access point
def scan_for_specific_access_points(interface, access_points):
    rssi_scanner = rssi.RSSI_Scan(interface)

    # sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
    # python file will have to be run with sudo privileges.
    ap_info = rssi_scanner.getAPinfo(networks=access_points, sudo=True)

    return ap_info

# scan for all access points
def scan_for_all_access_points(interface):
    rssi_scanner = rssi.RSSI_Scan(interface)

    # sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
    # python file will have to be run with sudo privileges.
    ap_info = rssi_scanner.getAPinfo(sudo=True)

    return ap_info