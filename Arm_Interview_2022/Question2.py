line = input(": ")

binaries = line.split(",")

larger_len = max(len(binaries[0]), len(binaries[1]))
bin1 = binaries[0].zfill(larger_len)
bin2 = binaries[1].zfill(larger_len)

# Initialize the result
result = ""

# Initialize the carry
carry = 0

# Traverse the string
for i in range(larger_len - 1, -1, -1):
    r = carry
    r += 1 if (bin1[i] == "1") else 0
    r += 1 if (bin2[i] == "1") else 0
    result = ("1" if (r % 2 == 1) else "0") + result

    # Compute the carry.
    carry = 0 if r < 2 else 1

if carry != 0:
    result = "1" + result

removed0 = []

for i in range(len(result)):
    removed0.append(result[i])


for i in range(len(removed0)):
    if (removed0[i] != "1"):
        removed0.remove(removed0[i])
    break


result = ""

for i in range(len(removed0)):
    result += removed0[i]

print(result)

