#! usr/bin/python3
# test
import operator

class edit_files(object):

   
    def __init__(self,my_file_input):

        self.my_file = my_file_input


    def clean_file(self):

        self.my_data = {}
        i = 0

        with open(self.my_file) as f:
            for line in f:
                try:
                    self.my_data[i] = float(line.rstrip())
                    i += 1

                except ValueError:
                    print("Removed line: "+line)


    def sort_values(self):

        self.my_sorted_keys = [] 
        self.my_sorted_values = []

        self.my_sorted_data = sorted(self.my_data.items(), key = lambda t: t[1])

        for x in self.my_sorted_data:
            self.my_sorted_keys.append(x[0])
            self.my_sorted_values.append(x[1])


    def print_values(self,no_of_values):
        
    # Print out keys and values of dictionary generated in sort_value().
    # The maximum length of the first column (i.e. the keys) is calculated
    # and used as a reference for the second column holding the values.
    # Function takes one argument: number of values to be printed
    
        self.col_width = max(len(str(row)) for row in self.my_sorted_keys) + 2

        for i in range(no_of_values):

            print(str(self.my_sorted_keys[i]).ljust(self.col_width),str(self.my_sorted_values[i]).ljust(self.col_width))

energy_file = edit_files("sampled.pot_energy")
my_energies = energy_file.clean_file()
energy_file.sort_values()
energy_file.print_values(100)


