'''
@author: Punit Goswami
Working only on MacOS
'''
import subprocess

# scan the available access points


def get_aps():
    scan_cmd = subprocess.Popen(
        ['airport', '-s'],    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scan_out, scan_err = scan_cmd.communicate()
    scan_out_data = {}
    scan_out_lines = str(scan_out).split("\\n")[1:-1]
    print(scan_out_lines)
    for each_line in scan_out_lines:
        split_line = [e for e in each_line.split(" ") if e != ""]
        line_data = {"SSID": split_line[0], "RSSI": int(str(split_line[2])), "channel": split_line[3], "HT": (
            split_line[4] == "Y"), "CC": split_line[5], "security": split_line[6]}
        scan_out_data[split_line[1]] = line_data
    return scan_out_data

print(get_aps())