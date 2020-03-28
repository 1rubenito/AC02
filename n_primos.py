import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def primos():
    primos = [2]
    print(2, end=' ')
    i = 3
    while len(primos) < 100:
        for p in primos:
            if (i % p == 0) or (p*p > i):
                break
        if i % p != 0:
            primos.append(i)
            print(i,  end=' ')
        i += 1
    print('<---- 100˚ Número Primo!')
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)