# WIFI Utilities

Uses python module of RSSI to determine the beacon strength of a given access point.
It utilises the classes `RSSI_Scan` and `RSSI_Localizer`.
Along with this, numpy is used to do mathematical operations.  
Wifi access points send out beacon signals through which their name, their beacon strength and their signal quality can be determined.  
The beacon strength is broadcasted in decibel-milliwatts units(dBM). Higher reading indicates a higher beacon strength.  
Considering the research paper [here](https://file.scirp.org/pdf/CN_2013071010352139.pdf), presence of more than two access points can be used for indoor localization. Measuring their relative signal strengths, it can be determined what the position of the client is by contrasting against a book value, although the position will always be addressed in realtive terms to the access points.


### wifiAPLocaliserUtils.py
* estimate_distance_from_access_point()
---
Takes access points reference array as input with the book value of the signal strengths of the access points. Other inputs are the index of the access point for which current distance is to be determined and the name of the network interface. Then compares the current signal strength of the selected access point to determine the current distance from the access point. The distance returned is in meters.

### wifiScanRSSI.py
---
* scan_for_specific_access_points()
Takes name of the interface and array of strings of names of access points of interest. Returns the signal strength, quality of signal for the access points mentioned.

* scan_for_all_access_points()
Takes name of the interface. Returns the signal strength, quality of signal for all the access points whose beacon signal is detected in the vicinity.