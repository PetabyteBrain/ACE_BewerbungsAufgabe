# Api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example route: home
@app.route("/", methods=["GET"])
def home():
    return jsonify([{"message": "Welcome to the ACE API"},{"description": "you can visit /api/temp, /api/prime or /api/number"}])

# Temperature conversion kelvin to celsius
@app.route("/api/temp", methods=["GET"])
def get_temp():
    # request value
    celsius = request.args.get("celsius", type=float)
    kelvin = request.args.get("kelvin", type=float)

    # convert temperature based on given input
    if celsius is not None:
        kelvin = celsius + 273.15
    elif kelvin is not None:
        celsius = kelvin - 273.15
    else:
        return jsonify({"error": "Please provide either a 'celsius' or 'kelvin' parameter."}), 400

    return jsonify({ "kelvin": kelvin, "celsius": celsius})

# Show all Prime Numbers up to a given number
@app.route("/api/prime", methods=["GET"])
def get_primes():
    limit = request.args.get("limit", type=int)

    if limit == None or limit > 10000:
        return jsonify({"error": "Please provide a number under 10'000"}), 400

    # finished list of primess
    primes_finished = []

    # bool array
    prime = [True for i in range(limit+1)]
    p = 2
    while (p * p <= limit):

        # if prime[p] unchanged is prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, limit+1, p):
                prime[i] = False
        p += 1

    # add primes to primes list based on finished bool list
    for p in range(2, limit+1):
        if prime[p]:
            primes_finished.append(p)
    return jsonify({"primes": primes_finished})

#  give number fibonacci
@app.route("/api/number", methods=["GET"])
def get_number():
    n = request.args.get("n", type=int)

    # input must be between 0 and 50
    if (n == None or n < 0 or n > 50):
        return jsonify({"error": "Please provide a number between 0 and 50"}), 400

    # fibonaci sequence 0 = 0
    if n == 0:
        return jsonify({"number": 0})
    # fibonaci sequence 0 + 1 = 1
    if n == 1:
        return jsonify({"number": 1})

    # calculation if n is larger than 1
    numbers = [0, 1]
    # creates list from 2 till n
    for i in range(2, n + 1 ):
        numbers.append(numbers[-2] + numbers[-1])

    return jsonify({"number": numbers[n]})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
