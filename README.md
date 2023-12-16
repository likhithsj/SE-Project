# SE-Project

This research paper introduces a project designed for the Software Engineering Data Mining Challenge. The objective is to study how an AI model, specifically ChatGPT, responds to various types of queries posed by developers, including bug reports, requests for new features, and theoretical inquiries. The project seeks to address three key research questions as follows below.

1) What types of issues do developers most commonly present to ChatGPT?
2) How does the conversation length vary between different types of issues?
3) How does the length of a question affect ChatGPT’s response length?

DATASET:
---------

  In this research, we made use of the most recent dataset “snapshot_20230831” provided by the MSR 2024 mining challenge. The dataset consists of dialogues between developers and ChatGPT, covering a wide range of topics including bug reports, coding inquiries, requests for documentation, feature utilization, installation procedures, design-related queries, theoretical questions, and reviews.

FILE STRUCTURE:
----------
filtered_data_and_code file has the python code to filter the data from the data set which is available from	https://2024.msrconf.org/track/msr-2024-mining-challenge.

   - To run the code first make sure the json files are in the same file path as the code. By running the filter_data_code it will genarate all the filtered files in separate JSON files.
   - We havent uploaded the unfiltered json files as the soze were too large.

  - Classify_chatGPT_prompts file answers the first research question.
  - Average_Conversation_Length file answers the second research question.
  - Wording influence file answers the third research question.
  
FIRST QUESTION: 
-----------

What types of issues do developers most commonly present to ChatGPT?

**FILE STRUCTURE:**

  Classify_chatGPT_prompts file answers the first research question it has Output file, src file and SE_model.ipynb file
  
    - Output file has the output screenshots of the filtered data and the actual filtered data.
    - src has the main code which is naviebycemodel.py.
    - SE_model.ipynb also has the main code which I used google colab as the dataset is too large.
    
**SOLUTION SETUP:**

  To run the code open SE_model.ipynb file open the colab link. Next get the filtered dataset from filtered_data_and_code file and add these data to the runtime local in the google colab then run the code one by one. It will genarate three files which are coding questions, theoritical questions and feature request questions.
  
  Finally a bar graph will be plotted between all the three types of categories.
  
**RESULT:**
The genearted output files are in Output and the final result as follows below.
![image](https://github.com/likhithsj/SE-Project/assets/53929108/cb0f922d-f052-43da-8333-3fa2cc7e1064)

SECOND QUESTION: 
------------

How does the conversation length vary between different types of issues and among coding prompts what are the common programming languages do developers regularly ask ChatGPT.

**FILE STRUCTURE:**

Average_Conversation_Length file answers the second research question It has five filtered datasets, ToFilterData.py file to filter the datasets, ToFindConversationLength.py file to find the average conversation lenght of the filtered datasets, Wordusagefrequencyfile.py file to find the frequency of programming languages do developers regulalry ask chatGPT, and output screenshots.

**SOLUTION SETUP:**

To run the code open ToFindConversationLenght.py file, mention the name of the dataset in 'json_file_path' to find the average conversation length of the dataset. To filter the datasets, open ToFilterData.py file, mention the name of the dataset to filter in 'json_file_path' and mention the file path in 'path' to store the filtered the data. Open Wordusagefrequency.py file To find the frequency of programming languages do developers ask chatGPT, mention the dataset name in 'json_file_path' to find the most common programming languages that developers ask chatGPT.

**RESULTS:**

![Screenshot 2023-12-06 212034](https://github.com/likhithsj/SE-Project/assets/72007255/5bd3090b-80f3-4aa1-9b1a-cd249ca1288c)

![Screenshot 2023-12-06 212145](https://github.com/likhithsj/SE-Project/assets/72007255/4b980c97-7eb7-4f0a-b8b7-356132dfd621)

![Screenshot 2023-12-06 212221](https://github.com/likhithsj/SE-Project/assets/72007255/511ea788-3fa5-47a7-b138-f86a1622c07b)

![Screenshot 2023-12-15 183402](https://github.com/likhithsj/SE-Project/assets/72007255/2543ee2a-732e-4a7d-9ece-efc7f25bca11)

![Screenshot 2023-12-15 183747](https://github.com/likhithsj/SE-Project/assets/72007255/375fae61-36f9-458d-8767-8d4e9bab9da2)






THIRD QUESTION:
----------

How does the length of a question affect ChatGPT's response length?

**FILE STRUCTURE:**

  Wording influence file answers the third research question it has Output figures, Analysis.txt and length_influence.py file
  
    - Output figures show the experimental results.
    - length_influence.py is the main code.
    - Analysis.txt gives the detailed result explanation.

**SOLUTION SETUP:**

To run the code open Wording influence file, then simply run the python script "length_influence.py" by intalling the proper libraries. (pip install pandas matplotlib seaborn scipy) 

**RESULTS:**

The results are as follows:

![image](https://github.com/likhithsj/SE-Project/assets/125890917/4ffe7b95-6c6c-41b1-ba79-76bffa3059d3)
![image](https://github.com/likhithsj/SE-Project/assets/125890917/1a5c93de-120a-4745-92f8-81d6354f11f2)


