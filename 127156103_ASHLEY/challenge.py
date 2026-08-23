import json


def parse(v):
    v = v.strip()

    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        return v[1:-1]

    if v.lower() == 'true':
        return True

    if v.lower() == 'false':
        return False

    try:
        return float(v) if '.' in v else int(v)
    except ValueError:
        return v


def compare(a, op, b):
    if type(a) == bool:
        if op == '=':
            return a == b

        if op == '!=':
            return a != b

        return False

    if type(a) in [int, float]:
        try:
            a, b = float(a), float(b)
        except (ValueError, TypeError):
            return False
    else:
        a, b = str(a), str(b)

    if op == '=':
        return a == b

    if op == '!=':
        return a != b

    if op == '>':
        return a > b

    if op == '>=':
        return a >= b

    if op == '<':
        return a < b

    if op == '<=':
        return a <= b

    return False


def check(record, field, op, value):
    if field not in record:
        return False

    return compare(record[field], op, parse(value))


n = int(input())

records = [input() for _ in range(n)]

expr = input().strip()

conditions = []

for c in expr.split(' AND '):
    field, op, value = c.split(' ', 2)
    conditions.append((field, op, value))



print("*****OUTPUT*****")
for line in records:
    record = json.loads(line)

    if all(check(record, f, op, v) for f, op, v in conditions):
        print(line)