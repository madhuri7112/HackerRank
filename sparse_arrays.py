# https://www.hackerrank.com/challenges/sparse-arrays/submissions/code/64464647
# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
   num_strings = input()
   all_strings_freq = {}
   for i in range(0, num_strings):
       stri = raw_input()
       if stri in all_strings_freq:
           all_strings_freq[stri] = all_strings_freq[stri]+1
       else:
           all_strings_freq[stri] = 1

   num_queries = input()
   for i in range(0, num_queries):
        query = raw_input()
        if query in all_strings_freq:
            print all_strings_freq[query]
        else:
            print "0"

main()
