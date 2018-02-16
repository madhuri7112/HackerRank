#https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem
from Queue import PriorityQueue

def min_avg_time(time_duration_pairs):

     heap = PriorityQueue()
     time_duration_pairs = sorted(time_duration_pairs, key = lambda x: x[0])
     current_serve = time_duration_pairs[0]
     current_time = current_serve[0]
     current_end_time = current_time + current_serve[1]
     tdpair_index = 1
     current_time = current_end_time
     wait_time = current_time - current_serve[0]
     #print current_end_time, current_serve[0], current_end_time - current_serve[0], "pr1"

     while(1):
        while( tdpair_index<len(time_duration_pairs) and time_duration_pairs[tdpair_index][0] <= current_end_time ):
            td = time_duration_pairs[tdpair_index]
            heap.put((td[1], td))
            tdpair_index = tdpair_index + 1
            
        if(heap.empty()):
           if (tdpair_index<len(time_duration_pairs)):
               td = time_duration_pairs[tdpair_index]
               heap.put((td[1], td))
               tdpair_index = tdpair_index + 1
           else:
                break

        current_serve = heap.get()[1]
        current_time = max(current_time, current_serve[0])
        current_end_time = current_time + current_serve[1]
        #print current_end_time, current_serve[0], current_end_time - current_serve[0], "pr"
        wait_time = wait_time + (current_end_time - current_serve[0])
        current_time = current_end_time
        
     return wait_time/len(time_duration_pairs)
     
def main():
     num_customers = input()
     time_durations = []
     while (num_customers):
          inp = raw_input()
          inp_array = inp.strip().split(" ")
          time_durations.append(( int(inp_array[0]), int(inp_array[1] ))) 
          num_customers = num_customers - 1
     wait_time = min_avg_time(time_durations)

     print wait_time

main()


