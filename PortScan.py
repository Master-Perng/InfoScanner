import nmap
def scan(ip,port,args) :
    port = nmap.PortScanner()
    port.scan(ip,port,args)
    print(port)
if __name__ == '__main__':
    ip = '47.101.131.6'
    port = '0-65535'
    args = '-n -sP -PE'
    port.scan(ip,port,args)
