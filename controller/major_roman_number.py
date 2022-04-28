def majorRomanNumber(text):
    nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    maior_valor = 0
    number = ""

    for i in range(len(text)):
        value = nums.get(text[i], 0)
        if value == 0:
            if sum > maior_valor:
                maior_valor = sum
                maior_numero = number
            sum = 0
            number = ""
            continue
        number += text[i] if text[i] in nums else ""
        if i + 1 < len(text) and nums.get(text[i + 1], 0) > value:
            sum -= value
        else:
            sum += value
            if sum > maior_valor:
                maior_valor = sum
                maior_numero = number

    return {"number": maior_numero, "value": maior_valor}
