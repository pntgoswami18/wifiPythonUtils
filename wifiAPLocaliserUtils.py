from rssi import RSSI_Localizer
from wifiScanRSSI import scan_for_specific_access_points

# Example reference array
# ap_ref_array=[{
#         'signalAttenuation': 3, 
#         'location': {
#             'y': 1, 
#             'x': 1
#         }, 
#         'reference': {
#             'distance': 4, 
#             'signal': -50
#         }, 
#         'name': 'dd-wrt'
#     },
#     {
#         'signalAttenuation': 4, 
#         'location': {
#             'y': 1, 
#             'x': 7
#         }, 
#         'reference': {
#             'distance': 3, 
#             'signal': -41
#         }, 
#         'name': 'ucrwpa'
#     }]

def estimate_distance_from_access_point(ap_ref_array, ap_index, interface):
    rssi_localizer_instance = RSSI_Localizer(ap_ref_array)
    ap_info = scan_for_specific_access_points(interface,ap_ref_array[ap_index])
    
    if(ap_info):
        signal_strength = ap_info['0']['signal']

        ap = rssi_localizer_instance.getDistanceFromAP(ap_ref_array[ap_index], signal_strength)
        return ap['distance']
    else:
        return ap_info