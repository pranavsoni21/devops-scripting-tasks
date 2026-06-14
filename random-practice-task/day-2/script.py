with open("app.log", "r") as file:
	lines = file.readlines()

total_no_of_errors = 0
total_no_of_warnings = 0
error = []

for l in lines:
	if "WARNING" in l:
		total_no_of_warnings += 1

	elif "ERROR" in l:
		total_no_of_errors += 1
		error.append(l)


print("================== LOG REPORT ==================\n")
print(f"ERROR COUNT: {total_no_of_errors}\n")
print(f"WARNING COUNT: {total_no_of_warnings}\n")
print(f"ERROR DETAILS:\n")
for l in error:
	print(l.strip())

if total_no_of_errors > 2:
	print("\nALERT: APPLICATION UNSTABLE")


