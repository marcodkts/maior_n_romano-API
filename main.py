from flask import Flask, request, jsonify
app = Flask(__name__)
    
@app.route('/search', methods=['POST'])
def maior_n_romano():
    nums = {
        'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
        }
    content = request.get_json()["text"]
    sum = 0
    number = ""
    sum_results = []
    num_results = []

    for i in range(len(content)):
        try:
            value = nums[content[i]]
            number += content[i]
            if content[i+1] not in nums:
                sum += value
            elif i+1 < len(content) and nums[content[i+1]] > value:
                sum -= value
            else: sum += value
            if i+1 == len(content):
                sum_results.append(sum)
                num_results.append(number)
        except Exception:
            sum_results.append(sum)
            sum = 0
            num_results.append(number)
            number = ""
            
    maior_valor = max(sum_results)
    maior_numero = num_results[sum_results.index(maior_valor)]

    return jsonify({
        "number": maior_numero,
        "value": maior_valor
    })

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port='8080')
