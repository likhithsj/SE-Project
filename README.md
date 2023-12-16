# SE-Project

This research paper introduces a project designed for the Software Engineering Data Mining Challenge. The objective is to study how an AI model, specifically ChatGPT, responds to various types of queries posed by developers, including bug reports, requests for new features, and theoretical inquiries. The project seeks to address three key research questions as follows below.

1) What types of issues do developers most commonly present to ChatGPT?
2) How does the conversation length vary between different types of issues?
3) How does the length of a question affect ChatGPT’s response length?

DATASET:

  In this research, we made use of the most recent dataset “snapshot_20230831” provided by the MSR 2024 mining challenge. The dataset consists of dialogues between developers and ChatGPT, covering a wide range of topics including bug reports, coding inquiries, requests for documentation, feature utilization, installation procedures, design-related queries, theoretical questions, and reviews.

FILE STRUCTURE:
 filtered_data_and_code file has the python code to filter the data from the data set which is available from	https://2024.msrconf.org/track/msr-2024-mining-challenge.
   -To run the code first make sure the json files are in the same file path as the code. By running the filter_data_code it will genarate all the filtered files in separate JSON files.
   -We havent uploaded the unfiltered json files as the soze were too large.

  Classify_chatGPT_prompts file answers the first research question.
  Average_Conversation_Length file answers the second research question.
  Wording influence file answers the third research question.
  
FIRST QUESTION: 

What types of issues do developers most commonly present to ChatGPT?

FILE STRUCTURE:

  Classify_chatGPT_prompts file answers the first research question it has Output file, src file and SE_model.ipynb file
    Output file has the output screenshots of the filtered data and the actual filtered data.
    src has the main code which is naviebycemodel.py.
    SE_model.ipynb also has the main code which I used google colab as the dataset is too large.
    
SOLUTION SETUP:

  To run the code open SE_model.ipynb file open the colab link. Next get the filtered dataset from filtered_data_and_code file and add these data to the runtime local in the google colab then run the code one by one. It will genarate three files which are coding questions, theoritical questions and feature request questions.
  Finally a bar graph will be plotted between all the three types of categories.
  
RESULT:
The genearted output files are in Output and the final result as follows below.
![image](https://github.com/likhithsj/SE-Project/assets/53929108/cb0f922d-f052-43da-8333-3fa2cc7e1064)


  
