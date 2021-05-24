from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
	negative = False

	if num_as_string[0] == "-":
		num_as_string = num_as_string[1:]
		negative = True
	rslt = ""

	valB10 = 0
	multiple = 1

	reverse = num_as_string[::-1]

	for l in reverse:
		curr = convertStrToNumb(l)
		valB10 += curr*multiple
		multiple *= b1

	while valB10 >= b2:
		rslt = convertNumbToString(valB10 % b2) + rslt
		valB10 = int(valB10/b2)

	valB10 = convertNumbToString(valB10) + rslt

	if negative:
		return "-" + valB10
	return valB10

def convertNumbToString(s):
	if s == 0:
		return "0"
	elif s == 1:
		return "1"
	elif s == 2:
		return "2"
	elif s == 3:
		return "3"
	elif s == 4:
		return "4"
	elif s == 5:
		return "5"
	elif s == 6:
		return "6"
	elif s == 7:
		return "7"
	elif s == 8:
		return "8"
	elif s == 9:
		return "9"
	elif s == 10:
		return "A"
	elif s == 11:
		return "B"
	elif s == 12:
		return "C"
	elif s == 13:
		return "D"
	elif s == 14:
		return "E"
	elif s == 15:
		return "F"
	else:
		print("unknown: "+s)
		return 1/0

def convertStrToNumb(s):
	if s == "0":
		return 0
	elif s == "1":
		return 1
	elif s == "2":
		return 2
	elif s == "3":
		return 3
	elif s == "4":
		return 4
	elif s == "5":
		return 5
	elif s == "6":
		return 6
	elif s == "7":
		return 7
	elif s == "8":
		return 8
	elif s == "9":
		return 9
	elif s == "A":
		return 10
	elif s == "B":
		return 11
	elif s == "C":
		return 12
	elif s == "D":
		return 13
	elif s == "E":
		return 14
	elif s == "F":
		return 15
	else:
		print("unknown: "+s)
		return 1/0


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
									   convert_base))
