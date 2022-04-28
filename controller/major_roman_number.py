def majorRomanNumber(text):
    nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    number = ""
    sum_results = []
    num_results = []

    for i in range(len(text)):
        try:
            value = nums[text[i]]
            number += text[i]
            if text[i + 1] not in nums:
                sum += value
            elif i + 1 < len(text) and nums[text[i + 1]] > value:
                sum -= value
            else:
                sum += value
            if i + 1 == len(text):
                sum_results.append(sum)
                num_results.append(number)
        except ValueError:
            sum_results.append(sum)
            sum = 0
            num_results.append(number)
            number = ""

    maior_valor = max(sum_results)
    maior_numero = num_results[sum_results.index(maior_valor)]

    return {"number": maior_numero, "value": maior_valor}
       