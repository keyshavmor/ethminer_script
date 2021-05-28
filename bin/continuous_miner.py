import subprocess
import sys
import signal

print("Launching Ethminer")

def signal_handler(signal, frame):
    print("You pressed Ctrl+C")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

return_val = -2 #Process return -2 on exit

while return_val == -2:
    process = subprocess.Popen("./ethminer -G -P stratum1+ssl://0x3c8FF37553E1b925CDec19DF035969e94e9A0d9c@eu1.ethermine.org:5555 --noeval --report-hashrate --response-timeout 999 --work-timeout 999",stdout=subprocess.PIPE,shell=True)
    stdout = process.communicate()[0]

    return_val = process.poll()
    print('Ethminer exited with return value:'+str(return_val)+'. Restarting Ethminer.')
    
print('Ethminer exited with return value:'+str(return_val))
    


	

