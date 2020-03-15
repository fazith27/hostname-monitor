import socket
import logging
import time
import platform

def main():
    frequency=5
    logfilepath = 'C:\Process\process.log'
    if platform.system() == 'Linux':
        logfilepath = '/app/process.log'
    logging.basicConfig(filename=logfilepath, level=logging.INFO, format='[%(asctime)s] %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    while True:
        logging.info('Printing Host Name : '+socket.gethostname()+' with frequency : '+str(frequency)+' second(s)')
        #print('Host Name : '+socket.gethostname()+' with frequency : '+str(frequency)+' logging file '+logfilepath)
        time.sleep(frequency)
if __name__ == '__main__':
    main()