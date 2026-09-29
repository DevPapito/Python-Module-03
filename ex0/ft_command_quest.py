import sys

def main():
	print("=== Command Quest ===")
	print("Program name: ft_command_quest.py")
	if (len(sys.argv) == 1):
		print("No arguments provided!")
	else:
		args_received = len(sys.argv) - 1
		print(f"Arguments received: {args_received}")
		i = 1
		while (i < len(sys.argv)):
			print(f"Argument: {i}: {sys.argv[i]}")
			i += 1
	print(f"Total arguments: {len(sys.argv)}")
	print("\n")

if __name__ == '__main__':
	main()
