#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import pandas as pd
import os
import matplotlib.pyplot as plt

class CleansingDialogue():
    """
    A class to cleanse dialogue.
    ...
    Attribute
    ----------
    input_file(str): The string to save the input file's name
    work_path(str): The string to save the current working path
    
    Methods
    -------
    extract_dialogue():
        Extract the dialogue and save in file.
    pre_separating_dialogue():
        Separating the dialogues of different roles and store them in a list of dictionary.
    clean_dialogue(dialogue_extract):
        Build a dictionary that different roles have their own dialogue.
        Output the dialogue of different roles in their corresponding files.     
    unique_words(file_name):
        Return a list that each dialogue has unique words.
    """
    def __init__(self, input_script):
        """
        Constructs all the necessary attributes for the SwimGame object.
        Args:
            input_script(str):name of script which will be processed
        """
        self.input_file = input_script
        self.work_path = os.getcwd()

    def extract_dialogue(self):
        """
        Extract the dialogue and save in file.
        Returns:
            list: The pre-processed script in a list of tuple
        """
        # 1. Read the txt with read() and creat a list started with the first Scene
        with open(self.input_file, 'r', encoding='utf-8') as f:
            input_txt = f.read()
            index_number = re.search('\[',input_txt).span()  # Using re.search to find the first '[' appeared index number
            txt_lines = input_txt[index_number[0]:].split('\n')  # Slice the input_script's content from index_number[0], then split it with '\n'
        # 2. Extract dialogue by looking for content starting with the name of the role and ';' , eg. Ross:....
        txt_list = []
        for i in txt_lines:
            dialogue_lines = re.findall('^[A-Z].*:.*',i)  # Find all format start with '^[A-Z].*:.*' from each item in txt_list
            txt_list.extend(dialogue_lines)  # Add all lists in txt_list and the txt_line only has dialogue with '()'
        # 3. Remove the brackets and content in brackets
        clean_list = []
        for i in txt_list:
            clean_item = re.sub('\(.*?\)', '', i)
            clean_list.append(clean_item)
        pre_processed_list = [tuple(i.split(":")) for i in clean_list]  # Creat the pre-processed script in a list of tuple
        # 4. Save the pre_processed_list to a '32807961_clean_dialogue.txt' file
        with open('32807961_clean_dialogue.txt', 'w', encoding='utf-8') as f_save:
            for i in pre_processed_list[:len(pre_processed_list) - 1]:     
                f_save.write(':'.join(i) + '\n')
            f_save.write(':'.join(pre_processed_list[-1]))          #Write the last line without newline  
        return pre_processed_list  

    # Separating the dialogues of different roles and store them in a list of dictionary
    def pre_separating_dialogue(self):
        """
        Separating the dialogues of different roles and store them in a list of dictionary.
        Returns:
            list: The list contain each one-line dialogue in dictionary type
        """    
        # 1. Open the task1 txt and creat a list by split with '\n'
        with open('32807961_clean_dialogue.txt', 'r', encoding='utf-8') as f:
            dialogue_list = f.read().split('\n')            # Each dialogue is an item in the list
            f.close()
        # 2. Modify the dialogue_list's items to dictionary
        dialogue_extract_list = []
        for i in dialogue_list:
            dialogue_dict = {}
            item_dict = str(i).split(':')           
            dialogue_dict[item_dict[0]] = item_dict[1]   # Creat dictionary that item is role and one line dialogue
            dialogue_extract_list.append(dialogue_dict)
        return dialogue_extract_list

    def clean_dialogue(self, dialogue_extract_list):
        """
        Build a dictionary that different roles have their own dialogue eg. {'ross':all his dialogue}.
        Then output the dialogue of different roles in their corresponding files.
        Args:
            dialogue_extract_list(list): contain dictionary with role and one-line dialogue 
        """
        key_list = []
        value_list = []
        # 1. Combine multiple dictionaries, the values of the same key are append with newline
        for i in dialogue_extract_list:    # Traverse the list and i is dictionary
            for key, value in i.items():
                if key in key_list:   #if key exists, append the value to the same key
                    index_number = key_list.index(key)   
                    value_list[index_number] = value_list[index_number] + '\n' + value   # Add value to value_list
                else:
                    key_list.append(key)
                    value_list.append(value)
        clean_dict = dict(zip(key_list, value_list)) 
        # 2. Creat a directory to save each role text
        if not os.path.isdir('./32807961_dialogue'):  # check whether the dir exists
            os.mkdir('./32807961_dialogue')
        os.chdir('./32807961_dialogue')         # Modify the work path to new directory
        # 3. Save different roles' dialogue to corresponding files
        for i in clean_dict:
            with open('32807961_%s' % (i.lower()), 'w', encoding='utf-8') as f:
                f.write(clean_dict[i])
                f.close()
        os.chdir(self.work_path)
        
    def unique_words(self, file_name):
        """
        Return a list that each dialogue has unique words.
        Args:
            file_name(str): file's name
        Returns:
            list: each dialogue has unique words
        """
        # 1.Wash the dialogue by lower the character and split them by '\n' into a list
        with open(file_name, 'r', encoding='utf-8') as f:
            dialogue = f.read().lower().split('\n')
            f.close()
        # 2.Use set to get each line which has unique words
        unique_words_list = []
        for i in dialogue:
            line_list = i.split(' ')    # Separate one dialogue line with ' ' and save in a list
            line_set = set(line_list)   # Use set() to get unique words in a line
            line_set = [j for j in line_set if j != '']   # Remove the empty set
            unique_words_list.append(list(line_set))  # Creat a list contains each line that have unique words
        return unique_words_list
        
class Analyze_Data():
    """
    A class to analyze dialogue.
    ...
    Attribute
    ----------
    cd(CleansingDialogue): The CleansingDialogue class to instantiate
    pathway(str): The string to save the current working path
    
    Methods
    -------
    creat_DataFrame():
        creat DataFrame by input list and file's name.
    unique100(file_name):
        Return the Dataframe who's unique words are more than 100
    generate_total_dataframe():
        Contact Dataframe that unique words more than 100 to one Dataframe and return it, 
        export Dataframe created as csv.           
    visualise_dataframe():
        Visualise the return Dataframe with bar graph
    """
    def __init__(self,file_name):
        """
        Constructs all the necessary attributes for the SwimGame object.
        Args:
            input_script(str):name of script which will be processed
        """
        self.cd = CleansingDialogue(file_name)
        self.pathway = os.getcwd()

    def creat_DataFrame(self, unique_words_list, file_name):
        """
        creat DataFrame by input list and file's name.
        Args:
            1. unique_words_list(list): each dialogue has unique word
            2. file_name(str): file's name
        Returns:
            Dataframe: record top 5 words and its line frequencies
        """
        role_name = re.sub('[^A-Za-z]', '', file_name)     # Extract the role's name by file's name
        dataframe_dict = {'role': [i for j in unique_words_list for i in j],
                          'word': [i for j in unique_words_list for i in j]}
        pre_df = pd.DataFrame(dataframe_dict)
        line_frequency_df = pre_df.value_counts().to_frame().reset_index()   # Count the line frequencies 
        top5_df = line_frequency_df[:5].drop(columns='role')
        role_name_df = pd.DataFrame({'role': [role_name for i in range(5)]})  # Creat a five-role's name Dataframe
        top5_df.insert(0, 'role', role_name_df['role'])   # Insert the role-name Dataframe in
        top5_df.columns = ['role', 'word', 'freq']
        return top5_df

    def unique100(self, file_name):
        """
        Return the Dataframe who's unique words are more than 100.
        Args:
            file_name(str): file's name
        Returns:
            Dataframe: record top 5 words and its line frequencies
        """
        # 1.Obtain the list of unique words that one role has spoken
        unique_word_list = self.cd.unique_words(file_name)
        unique_list = set([i for j in unique_word_list for i in j])  # Use set() to get unique words that has spoken
        # 2. Judge whether the count of unique words is more than 100
        if len(unique_list) > 100:   # If more than 100, creat Dataframe for the role
            unique_words_list = self.cd.unique_words(file_name)
            top5_df = self.creat_DataFrame(unique_words_list, file_name)
            return top5_df

    def generate_total_dataframe(self):
        """
        Contact Dataframe that unique words more than 100 to one Dataframe and return it, export Dataframe created as csv
        Returns:
            Dataframe: record each role's top 5 words and its line frequencies
        """
        # 1. Change the current working directory to 32807961_dialogue which includes different dialogue files
        os.chdir("./32807961_dialogue")
        txt_lists = os.listdir("./")
        # 2. Call the unique100 method for each file and concat the returned Dataframe
        top5_df_list = []
        for title in txt_lists:
            if title.startswith("32807961"):  # Make sure get correct file's name
                top5_df = self.unique100(title)
                top5_df_list.append(top5_df)  # Create list include Dataframe generated by unique100()
        total_dataframe = pd.concat(top5_df_list).reset_index(drop=True)  # Concat dataframes in the list
        # 3. Export the Dataframe created as csv file
        os.chdir(self.pathway)
        total_dataframe.to_csv('32807961_data.csv', sep=',', index=False, header=True)
        return total_dataframe

    def visualise_dataframe(self):
        """Visualise the return Dataframe  with bar graph."""
        # 1. Obtain the returned total_dataframe and set the figure
        data_frame = self.generate_total_dataframe()     
        role_number = int(len(data_frame) / 5)  # Count the number of role and store in role_number
        fig = plt.figure(num=1, figsize=(14, 20), dpi=80)     # Creat a figure space first
        fig.suptitle('Top 5 Frequent Words For Each Role', fontsize=18)
        # 2. Determine the number of rows to prepare different role number
        if role_number % 2 == 0:
            row_number = role_number/2
        else:
            row_number = role_number//2 + 1
        # 3. Draw subplot for each role
        for j in range(role_number):
            num = 5 * j
            name = data_frame['role'][num]                        # Obtain the name of role
            x = [i for i in data_frame['word'][0 + num:5 + num]]  # Extract each role's data and store in list
            y = [i for i in data_frame['freq'][0 + num:5 + num]]
            ax = plt.subplot(int(row_number), 2, j + 1)
            plt.bar(x, y, width=0.6, color='y')
            ax.set_title(name, fontsize=16, color='r')
            ax.set_xlabel('word', fontsize=14, color='b')
            ax.set_ylabel('frequency', fontsize=14, color='b')
            for a,b in zip(x,y):                                   # Add line frequency on the bar
                ax.text(a,b,b,ha='center',va='bottom',fontsize = '8'  )
            fig.tight_layout()
        plt.show()


# In[ ]:


# Task1
test_task1 = CleansingDialogue('input_script.txt')   # Enter the file's name
test_task1.extract_dialogue()


# In[ ]:


# Task2
test_task1.clean_dialogue(test_task1.pre_separating_dialogue())


# In[ ]:


# Task3
test_task3 = Analyze_Data('input_script.txt')  # Enter the input_script
test_task3.generate_total_dataframe()


# In[ ]:


# Task4
test_task3.visualise_dataframe()


# In[ ]:


#Task 4.2,4.3
'''
There are many different characters, each character contains two-dimensional data with frequceny, and the data size is small.
So drawing sub-pictures by bar can easily show each role and observe the frequencies of each word to compare words.
As we can see, chandler, rachel, ross and monica have big difference in their own line frequency, joey and phoebe have smaller difference.
Chandler's highest word is 'i' in 19, lowest is 'have' in 9, and most roles have 'a','i','to' in their top 5 line frequencies' graph.
'''

