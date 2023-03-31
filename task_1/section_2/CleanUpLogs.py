
logs = {'log1': 'log.INFO', 'log2': 'log.INFO', 'log3': 'log.ERROR', 'log4': 'log.INFO'}
logs_errors= {}

def scan_logs():
    print ("\nListando logs\n" )
    print(type(logs))
    print(logs)
    
    print ("\nScanning logs\n" )
    for log in logs:
        value = logs[log]
        print (log, value)
        moving_logs(log, value)
    send_email(logs_errors)

def moving_logs(log, value):
    if value =="log.ERROR":
        print(f"Moviendo {log} a la carpeta de errores\n")
        logs_errors[log] = value
    else:
        print(f"Moviendo {log} a la papelera de reciclage\n")
    
def send_email(logs_to_review):
    print("Enviando email al administrador")
    print(f"Favor revisar la siguiente lista de errores {logs_to_review}")

if __name__ == '__main__':
    scan_logs()  