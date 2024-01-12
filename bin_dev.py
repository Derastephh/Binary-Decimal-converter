import argparse

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

def main():
    parser = argparse.ArgumentParser(description="Binary to Decimal and Decimal to Binary Converter")

    parser.add_argument("-b", "--binary", help="Convert binary to decimal", type=str)
    parser.add_argument("-d", "--decimal", help="Convert decimal to binary", type=int)

    args = parser.parse_args()

    if args.binary:
        decimal_result = binary_to_decimal(args.binary)
        print(f"Binary {args.binary} to Decimal: {decimal_result}")

    elif args.decimal:
        binary_result = decimal_to_binary(args.decimal)
        print(f"Decimal {args.decimal} to Binary: {binary_result}")

    else:
        print("Invalid arguments. Use '-b' to convert binary to decimal or '-d' to convert decimal to binary.")

if __name__ == "__main__":
    main()
