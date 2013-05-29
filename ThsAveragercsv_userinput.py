import ThsAveragercsv

input_file = raw_input("Enter the name of input csv file\n")
output_file = raw_input("Enter the name of the output csv file\n")
ndata = input("Enter the number of samples\n")
init_temp = input("Enter the initial temperature (usually 20)\n")
final_temp = input("Enter the final temperature (usually 100)\n")

o = ThsAveragercsv.ThsAverager(input_file, output_file, ndata, init_temp, final_temp)
o.Average_Calculate()
