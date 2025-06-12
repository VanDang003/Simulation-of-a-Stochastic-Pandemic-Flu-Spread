import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random
from scipy.optimize import minimize

random.seed(1337) #Set seed for reproducibility

def pandemic(days=3, trials=10000, immunization_prob = 0):
    
    trial_data = np.zeros((trials, days))
    sick_prob = 0.02
    tommy_offspring = np.zeros((trials, days))
       
    for trial in range(trials):
        infected_count = 1
        healthy = np.zeros(31) #healthy = 0
        healthy[0] = 1 #Set Tommy as a sick boi
        
        #Code block changes students to immune based on percentage chance
        if immunization_prob !=0:
            immune_prob_numgen = np.random.rand(1,31)
            immune_index_attempt = np.where(immune_prob_numgen <= immunization_prob)[1]
            for j in immune_index_attempt:
                if j !=0: #Skip Tommy
                    healthy[j] = 4 #4 is essentially immune for the context of our code            
        
        for day in range(days): #For each day
            for infect_person in range(infected_count): #cycle through each sich student
                n = np.random.rand(1,31) #Generate new random numbers
                sick_index_attempt = np.where(n <= sick_prob)[1] #Attempt infection based on the number of sick ppl and find their index
                for i in sick_index_attempt:
                    if healthy[i] == 0:
                        healthy[i] = 1
                        infected_count +=1
                        
                        if infect_person == 0:  # If Tommy is the infecting person
                            tommy_offspring[trial, day] += 1
                            
            trial_data[trial, day] = infected_count
            
            #Prepare data for the next day
            
            #Increment the infection period of each student by 1
            nonzero_mask = np.where(healthy != 0)
            healthy[nonzero_mask] += 1
            
            #Update the infected count to those who are still infectious
            infected_count = len(healthy[(healthy > 0) & (healthy <= 3)])
            
            
    trial_data = trial_data-1 #Remove Tommy

    #Question 3a - What is the distribution of the number of kids that Tommy infects on Day 1?
    counts, bins, patches = plt.hist(trial_data[:,0], bins=np.arange(-0.5, max(trial_data[:,0])+1.5), edgecolor='black')
    plt.xlabel('Number of Students Infected by Tommy on Day 1')
    plt.ylabel('Frequency from Trials')
    plt.title('Distribution of Students Infected by Tommy on Day 1')
    
    print("Bar heights counts:", counts)
    #for count, bin in zip(counts, bins):
    #    plt.text(bin, count, str(int(count)), va='bottom', ha='center')
    plt.show()
    
    #Question 3b - What is the expected number of kids that Tommy infects on Day 1?
    day_1_expected = 30*0.02
    expected_sim_day_1 = np.mean(trial_data[:,0])
    print("Day 1 Expected Value:", day_1_expected)
    print("Day 1 Simulated Value:", expected_sim_day_1)
    
    #Question 3c - What is the expected number of kids that are infected by Day 2 (you can count Tommy if you want)?
    day_2_expected = day_1_expected*0.02*(30-day_1_expected) + 0.6 + 0.6 #Add Tommy's infections on Day 1 and Day2
    expected_sim_day_2 = np.mean(trial_data[:,1])
    print("Day 2 Expected Value:", day_2_expected)
    print("Day 2 Simulated Value:", expected_sim_day_2)
    
    #Question 3d - Simulate the number of kids that are infected on Days 1,2,. . . . Do this many times. What are the (estimated) expected numbers of kids that are infected by Day i, i = 1,2,...? Produce a histogram detailing how long the “epidemic” will last
    expected_totals = np.mean(trial_data, axis=0)
    expected_totals[np.where(expected_totals < 0)] = 0
    days_list = np.arange(1,days+1)
    
    plt.bar(days_list, expected_totals, edgecolor='black')
    plt.xlabel('Day')
    plt.ylabel('Estimated Infected')
    plt.title('Expected Infected Students Over Each Day')
    plt.show()    

    #for i, v in enumerate(expected_totals):
    #    print(f'Day {i+1}: {v:.2f}')
    
    #Question 3e - What if each kid has a 50–50 chance of already being immunized?
    #set immunization_prob = .5
    
    expected_tommy_offpsring = np.mean(tommy_offspring, axis=0)
    expected_tommy_offpsring[np.where(expected_tommy_offpsring < 0)] = 0
    plt.bar(days_list, expected_tommy_offpsring, edgecolor='black')
    plt.xlabel('Number of Days After Initial Infection')
    plt.ylabel('Frequency of Students Infected by Tommy')
    plt.title('Offspring Distribution of Tommy Over All Days')
    plt.show()
    
    for i, v in enumerate(expected_tommy_offpsring):
        print(f'Day {i+1}: {v:.2f}')
    print(sum(expected_tommy_offpsring))
    
    return trial_data

pandemic(days=15, trials=100000, immunization_prob = 0)
