######################################################################
# Mikko Majamaa 3rd of August 2018
#
# Make smaller files of original txt, csv etc. files.
#
# See README.txt for more info.

def main():
    while True:
        file_name = input("Filename: ")
        try:
            file_read = open(file_name, "r")
            while True:
                try:
                    proportion = int(input("Proportion size (for half 2, for quarter 4,  etc.): "))
                    if (proportion <= 0):
                        print("Incorrect value. Enter a positive integer greater than 0.")
                        continue
                    file_write = open("1of" + str(proportion) + "_" + file_name, "w")
                    break
                except ValueError:
                    print("Incorrect value. Enter an integer.")
                    continue
            row_count = 0
            orig_row_count = 0
            new_row_count = 0
            line = file_read.readline()
            for line in file_read:
                orig_row_count += 1
                row_count += 1
                if (row_count == proportion):
                   print(line, file = file_write)
                   new_row_count += 1
                   row_count = 0
            print("Wrote a new file '1of" + str(proportion) + "_" + file_name + "' with " + str(new_row_count) + " lines (original file has " + str(orig_row_count) + " lines).")
            break
        except FileNotFoundError:
            print("File not found.")

main()

######################################################################
# eof
