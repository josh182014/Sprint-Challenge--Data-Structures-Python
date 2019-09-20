import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)

# with open('names_1.txt', 'r') as n1:
#     duplicates.append(part in words for line in file for part in line.split())


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
