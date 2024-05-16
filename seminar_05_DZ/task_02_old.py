result = {name: salary * float(b.replace('%', '')) / 100 for name, salary, b in zip(names, salary, bonus)}

print(result)