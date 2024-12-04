import datetime

def data_atual():
    agora = datetime.datetime.now()
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))

data_atual()
