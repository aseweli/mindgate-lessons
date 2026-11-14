readings = [21.5, 22.0, 23.4]
with open("log.txt", "w") as f:
    for r in readings:
        pass                      # TODO: write r and a newline (f.write(str(r) + "\n"))

with open("log.txt", "r") as f:
    lines = f.readlines()
values = []                       # TODO: float(line) for each line
print(len(lines), "lines")
print("average:", sum(values) / max(len(values), 1))
