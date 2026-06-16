file_names = {"app1.log": 0,
              "app2.log": 0,
              "app3.log": 0
              }


def count_error(filename):
    count = 0
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        if "ERROR" in line:
            count += 1

    return count


print("============ MOST PROBLEMATIC APPLICATION ============\n")
for file in file_names:
    file_names[file] = count_error(file)
    print(f"{file}: {file_names[file]}")

max_error_count = 0
max_error_file = max(file_names, key=file_names.get)

for key, value in file_names.items():
    if value > max_error_count:
        max_error_count = value

print(f"\nPROBLEMATIC APP FILE: {max_error_file}")

print(f"\nTOTAL NO OF ERRORS: {max_error_count}")



