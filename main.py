import requests
import time

from currencydraw import currencydraw as dibuja_cotizaciones
from userinput import exit_on_keypress as salir_al_pulsar


def cotizacion_de(moneda, moneda_ref):
    base_url = 'https://api.coinbase.com/v2/exchange-rates?currency='
    r = requests.get(base_url + moneda)
    valor_str = r.json()["data"]["rates"][moneda_ref]
    valor = "{:.2f}".format(float(valor_str))

    return f"{moneda}: {valor} {moneda_ref}(s)"


def muestra_cotizaciones():
    moneda_ref = 'EUR'
    monedas = ['BTC', 'ETH']
    buffer = []

    for moneda in monedas:
        buffer.append(cotizacion_de(moneda, moneda_ref))

    for i in range(5):
        dibuja_cotizaciones(buffer)
        time.sleep(300)


if __name__ == '__main__':

    salir_al_pulsar()

    while(True):
        muestra_cotizaciones()
