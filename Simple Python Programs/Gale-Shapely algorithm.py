# Description : Gale-Shapely algorithm
# Author: Kevin Richard 

import random
import ast
import timeit
import matplotlib.pyplot as plt

def createPreferenceList_to_txt(n,inputfilename):
    men = []
    women = []
    men_preference =[]
    women_preference=[]

    for i in range(n):
        men.append(f"M{i+1}")
        women.append(f"W{i+1}")

    #generate preference list:
    for i in range(n):
        temp = women.copy()
        random.shuffle(temp)
        men_preference.append(temp)
        temp = men.copy()
        random.shuffle(temp)
        women_preference.append(temp)

    
    with open(inputfilename, 'w') as f:
        f.write(f"{n}")
        for i in range(len(men)):
            f.write(f"\n{men[i]} : {men_preference[i]}")
        for i in range(len(women)):
            f.write(f"\n{women[i]} : {women_preference[i]}")
    
    print("\nPreference list of men")        
    for i in range(len(men)):
        print(f"{men[i]} : {men_preference[i]}")
    print("\nPreference list of women")  
    for i in range(len(women)):
        print(f"{women[i]} : {women_preference[i]}")
    
    print(f"\nThe preference list create and saved to '{inputfilename}'")
        
    return   


def read_txt_preference_input(inputfilename):
    men=[]
    women=[]
    men_preference=[]
    women_preference=[]

    with open(inputfilename) as f:
        lines = f.readlines()
    n = int(lines[0])
    for i in range(n):
        temp = lines[i+1].split(' : ')
        men.append(temp[0])
        men_preference.append(ast.literal_eval(temp[1]))
    for i in range(n):
        temp = lines[i+n+1].split(' : ')
        women.append(temp[0])
        women_preference.append(ast.literal_eval(temp[1]))

    print("\nThe preference list read from the input file:\n")
    for i in range(len(men)):
        print(f"{men[i]} : {men_preference[i]}")
    for i in range(len(women)):
        print(f"{women[i]} : {women_preference[i]}")
        
    return men,women,men_preference,women_preference


def write_txt_stablePair_output(outputfilename,men,men_pair):
    with open(outputfilename, 'w') as f:
        for i in range(len(men)):
            f.write(f"{men[i]},{men_pair[i]}")
            if(i+1 != len(men)):
                f.write("\n")
    return


def gale_shapely_for_input_txt(inputfilename,outputfilename):
    
    men,women,men_preference,women_preference = read_txt_preference_input(inputfilename)
    startTime = timeit.default_timer()
    men_pair = ["None"]*len(men)
    i = 0
    print("\n")
    while(i<len(men)):
        j = 0
        while(j<len(men)):
            man_preference = men_preference[i].copy()
            #print(f"{men[i]} : {man_preference}")
            if men_pair[i] != "None":
                break
            elif man_preference[j] not in men_pair:
                # print(men_preference[j])
                men_pair[i] = man_preference[j]
                break
            else:
                index_man_with_her = men_pair.index(man_preference[j])  # index of current man with woman (pair list)
                index_of_women = women.index(man_preference[j])
                rank_womens_current_man_appeal = women_preference[index_of_women].index(men[index_man_with_her]) # (w_p list)index of current man in her preference
                rank_womens_preference_of_New_man = women_preference[index_of_women].index(men[i]) # (w_p list) index of new man in her preference
                if rank_womens_preference_of_New_man < rank_womens_current_man_appeal:
                    men_pair[index_man_with_her] = "None"
                    men_pair[i] = women[index_of_women]
                    women_index_current_man_list = men_preference[index_man_with_her].index(man_preference[j])
                    i = index_man_with_her
                    j = women_index_current_man_list
                    #print(f"back {i} , {j}")
            j +=1
        i +=1
    
    exec_time = timeit.default_timer() - startTime  
                  
    print("\nThe stable matching output from Gale-Sahpely function: ") 
    for i in range(len(men)):
        print(f"{men[i]},{men_pair[i]}")
        
    write_txt_stablePair_output(outputfilename,men,men_pair)
    return exec_time,outputfilename
    
def read_input_of_Output_file(output_file):
    men_pair =[]
    women_pair =[]
    with open(output_file) as f:
        lines = f.readlines()
    for line in lines:
        temp = line.split(',')
        men_pair.append(temp[0].split())
        women_pair.append(temp[1].split())
    return men_pair,women_pair

def checkUnstablePairs(pair_check_filename,inputfilename):
    _,outputfilename=gale_shapely_for_input_txt(inputfilename,'checkUnstablePairs_output.txt')
    men_input_pair,women_input_pair = read_input_of_Output_file(pair_check_filename)
    men_gs_pair,women_gs_pair = read_input_of_Output_file(outputfilename)
    for i in range(len(men_input_pair)):
       if women_gs_pair[men_gs_pair.index(men_input_pair[i])] != women_input_pair[i] :
            print("This is an Unstable pairing")
            return
    print("This is a Stable pairing")
    return

def change_man_proposing_first(main_filename,no_of_changes):
    men,women,men_preference,women_preference = read_txt_preference_input(main_filename)
    
    for i in range(no_of_changes):
        temp = men[0]
        men[0] = men[i]
        men[i] = temp
        temp = men_preference[0]
        men_preference[0] = men_preference[i]
        men_preference[i] = temp
        with open(f'input_{i+1}_f.txt', 'w') as f:
            f.write(f"{len(men)}")
            for i in range(len(men)):
                f.write(f"\n{men[i]} : {men_preference[i]}")
            for i in range(len(women)):
                f.write(f"\n{women[i]} : {women_preference[i]}")
    return

def plot_exec_time(x_axis,exec_times,x_label,plotImg_filename):
    exec_times_1000 = [i * 1000 for i in exec_times]
    plt.plot(x_axis, exec_times_1000, linewidth=2, color='orange')
    plt.xlabel(f'{x_label}')
    plt.ylabel("(Execution Time * 1000) secs")
    plt.title(f"{x_label} vs Execution Time")
    plt.savefig(plotImg_filename)
    plt.show()
    return

#main function which goes to menu to slect the country          
def main():
    # createPreferenceList_to_txt(10,'input.txt')
    # exec_time,_ = gale_shapely_for_input_txt('input.txt','output.txt')
    # print(exec_time)
    while(True): 
        # Menu loop valid until user selects the Exit option and exitFlag=True.
        selectedOperation= input("\nSelect Homework 1: 1. option:-\na - Function to create preference lists\nb - Check if there are any unstable pairs\nc - Implement Gale-Shapely 5 times for n=10 & diff inputs\nd - Implement Gale-Shapely 5 times for n=10 & same inputs\ne - Implement Gale-Shapely 5 times for n = 10, 15, 20, 50, 100 & same inputs\nf - Implement Gale-Shapely for same preference with different man starting\ng - Exit Program\n:")
        if selectedOperation not in ['a','b','c','d','e','f','g']:
            print("Choose from the given option")  
        if selectedOperation=='a':
            n = int(input("\nPlease enter the number of men (women):"))
            createPreferenceList_to_txt(n,'preference_a.txt')
        elif selectedOperation=='b':
            print("Following Default input files will be used: 'output_pair_check_homework_1_b.txt','input_homework_1_b.txt'")
            input("Press Enter to continue!!")
            checkUnstablePairs('output_pair_check_homework_1_b.txt','input_homework_1_b.txt')
        elif selectedOperation=='c':
            print("n is set to default value: 10")
            n = 10
            exec_times = []
            for i in range(5):
                createPreferenceList_to_txt(n,f'input_{i+1}_c.txt')
            for i in range(5):
                exec_time,_ = gale_shapely_for_input_txt(f'input_{i+1}_c.txt',f'output_{i+1}c.txt')
                exec_times.append(exec_time)
            print(exec_times)
            plot_exec_time(range(1,6),exec_times,"Run number",'homework_1_c.png')
            
        elif selectedOperation=='d':
            print("n is set to default value: 10")
            n = 10
            exec_times = []
            # for i in range(5):
            createPreferenceList_to_txt(n,f'input_d.txt')
            for i in range(5):
                exec_time,_ = gale_shapely_for_input_txt(f'input_d.txt',f'output{i+1}_d.txt')
                exec_times.append(exec_time)
            print(exec_times)
            plot_exec_time(range(1,6),exec_times,"Run number",'homework_1_d.png')
            
        elif selectedOperation=='e':
            n = [10,15,20,50,100]
            avg_time = []
            for no_of_pairs in n:
                createPreferenceList_to_txt(no_of_pairs,f'input_{no_of_pairs}_e.txt')
            for no_of_pairs in n:
                exec_times = []
                for i in range(5):
                    exec_time,_ = gale_shapely_for_input_txt(f'input_{no_of_pairs}_e.txt',f'output_{no_of_pairs}_e.txt')
                    print(f"Output File = output_{i+1}_f.txt")
                    exec_times.append(exec_time)
                avg_time.append(sum(exec_times)/len(exec_times))
            print(avg_time)
            plot_exec_time(n,avg_time,"Number of pairs (n)",'homework_1_e.png')
            
        elif selectedOperation=='f':
            print("n is set to default value: 10")
            n = 10
            exec_times = []
            no_of_changes = 5
            createPreferenceList_to_txt(n,f'input_f_main.txt')
            change_man_proposing_first(f'input_f_main.txt',no_of_changes)
            for i in range(5):
                exec_time,_ = gale_shapely_for_input_txt(f'input_{i+1}_f.txt',f'output_{i+1}_f.txt')
                print(f"Output File = output_{i+1}_f.txt")
                exec_times.append(exec_time)
            print(exec_times)
            plot_exec_time(range(1,6),exec_times,"Run number with diff man starting",'homework_1_f.png')
            
        elif(selectedOperation=='g'):
            exit()
        input("\nPress Enter to continue !!")
       

#main function is called
if __name__=='__main__':
    main()    