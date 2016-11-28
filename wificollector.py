from subprocess import check_output

def grabpasswords(ssid):
    output=check_output('netsh wlan show profiles name="' + ssid + '" key=clear')
    for line in str(output).splitlines():
        if line.startswith("    Key Content"):
            return line[29:]
        elif line.startswith("    Key Index              : 1"):
            return "[Open Wifi]"

def main():
    print '\n WifiCollector\n'
    output=check_output('netsh wlan show profiles')
    for line in str(output).splitlines():
        if line.startswith("    All"):
            print '[+] ' + line[27:] + ":" + grabpasswords(line[27:])
    print "\nPress Enter to exit..."
    raw_input()


if __name__ == "__main__":
    main()




