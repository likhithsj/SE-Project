from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import json
import matplotlib.pyplot as plt

# Sample data (replace this with your labeled dataset)
data = {
    "code_question": [
      "Can you convert my code to the second solution?",
      "I have a vue 3 application. I have a ref constant which is a list. When nothing changed to the ref for 3 seconds, I want to trigger a method. What do I need?",
      "migrate back to git files tracked by GIT LFS",
      "generate missing code in the below dockerfile\n\n-----\nFROM ubuntu:20.04\n\nARG AWS_ACCESS_KEY_ID\nARG AWS_SECRET_ACCESS_KEY\nARG AWS_SESSION_TOKEN\nARG DEBIAN_FRONTEND=noninteractive\n\nLABEL org.opencontainers.image.authors=\"Sebastian Sasu <sebi@nologin.ro>, Cristian Magherusan-Stanciu <cmagh@amazon.de>, Brooke McKim <brooke@vantage.sh>\"\n\nRUN apt-get update\nRUN apt-get install -y python3 pip locales\nRUN apt-get install -y nodejs\nRUN apt-get install -y npm\nRUN npm install --global sass\nRUN python3 -m pip install -U pip setuptools\nRUN locale-gen \"en_US.UTF-8\"\n\nWORKDIR /opt/app\n\nCOPY requirements.txt .\nRUN pip3 install -r requirements.txt\n\nCOPY . .\n\nENV AWS_ACCESS_KEY_ID=\n\nRUN invoke build\n\nEXPOSE 8080\n\nCMD [\"invoke\", \"serve\"]\n",
      "The Clojure file contents are as follows:\n\n\n(ns foo.bar\n  (:require\n   [clojure.java.io :as io]\n   [clojure.string :as str]))\n\n\nAnd my request is:\n\nCreate a function that takes a resource path, reads its contents, and prints to stdout all its text converted to all-caps.",
      "Consider the following environment and mission: \n\nThe environment state is:\nWGWGWGWGWGWG\nWG        WG\nWG        WG\nWGAR  AB  WG\nWG  ^^    WG\nWGWGWGWGWGWG\n\nThe mission is: \nput the red ball near the blue ball \n\nDescribe how to decompose the mission into intermediate goal states using the functions defined above. ",
      "I am using venv(python module env) on the mac terminal. But I want to use python 3.11, right now it is 3.9 how can I upgrad it on the venv",
      "how to import multiple makeStyles using tss-react\n\ntsx\nfunction MyComponent(){ \n\n  const { classes } = RfpGridStyles();\n  const { classes } = IntakeTableStyles();\n\n}\n\n\nit shows redeclare block-scoped variable error",
      "Could you write me a module that would be responsible for generating and verifying a TOTP that can be emailed to users for email verification? I want to use the notp module from npm. Please call out whether anything needs to be saved in a database and any environment variables.",
      "Is the type field necessary? I think it would be safe to remove this. I think I would like to do that so I don't have to have an additional relational table. Can we remove that?\nI'm thinking instead of \"generation_time\" I'll use \"expirationTime\" which will make it easier for a background job to know whether it's safe to delete. Any issues with that?\n\nCould you write out the part of a prisma schema relevant to the model(s) necessary for this?",
      "Would it be reasonable for me to disassociate the verification model from the user? In the case of registration, I don't have a user yet. I'm thinking for registration I could just lookup the verification by the otp which would then allow me to create a new user by the identifier (which would be the email). Would doing this limit the usefulness of this model?",
      "For point 3, I could make the identifier be equal to the User ID. But that may be a bit ambiguous which makes me think bringing back the relational model for the type field would be useful. Which approach do you think strikes the best balance between complexity and flexibility?",
      "I'm using SQLite which doesn't support enum. Could you update the VerificationType to address this. Also, I don't think we need to include the User model anymore.\n\nAlso, is the term \"identifier\" the best option for what that really represents?",
      "Would that @@unique directive work if I used upsert when creating verification codes for which one of that type already exists?\n\nAlso, if I wanted to use a table for the type instead of a string, how would I do that?",
      "Good arguments. I think I'll keep it in the main database.\n\nCould you please write the module that uses prisma and manages creating and verifying TOTPs and handle edge cases where a second verification is created for the same type and target.","Great. Thanks. A few bits of feedback:\n\n1. Please rewrite that to native ESM and TypeScript.\n2. The prisma client comes from import { prisma } from '~/utils/db.server.ts'\n3. Let's make function arguments objects that are destructured in the argument list position.\n4. Let's make the expiration time an argument\n5. Could you fill in the generateSecretKey function with an implementation?\n\nThanks!",
      "Working set\n\nsrc/prompt/promptDescriptorDefaults.js:\n```\nimport { loadPromptFile } from './loadPromptFile.js';\nimport { getPromptDirectories } from './getPromptDirectories.js';\nimport fs from 'fs';\nimport path from 'path';\n\nconst promptDescriptorDefaults = async () => {\n  let promptDescriptorDefaults = {};\n  \n  const promptDirs = getPromptDirectories();\n  let uniqueFiles = new Set();\n\n  // Store all unique file names\n  for(let dir of promptDirs) {\n    const files = fs.readdirSync(dir).filter(file => file.endsWith('.md'));\n    files.forEach(file => uniqueFiles.add(file));\n  }\n\n  // Load only unique files\n  for (let file of uniqueFiles) {\n    const fileNameWithoutExtension = path.basename(file, '.md');\n    promptDescriptorDefaults[fileNameWithoutExtension] = await loadPromptFile(`prompt/${file}`);\n  }\n  \n  return promptDescriptorDefaults;\n}\n\nexport default promptDescriptorDefaults;\n\n```\n\n\n# Task\n\nFix the following issue!\n\nHandle the case silently when a prompt folder does not exests.\n\n# Output Format\n\nEncode and enclose your results as ./change.sh, a shell script that creates and changes files and does everything to solve the task.\nFiles are small, prefer heredoc-ing full files using 'EOF' to prevent substitution.\n\nOS: OSX\n\nInstalled tools: npm, jq\n\n\nDo NOT write any text outside the script!\n\nEXAMPLE START\n\n```sh\n#!/bin/sh\nset -e\ngoal=[Task description, max 7 words]\necho \"Plan:\"\necho \"1. [...]\"\n[Commands solving the task]\necho \"\\033[32mDone: $goal\\033[0m\\n\"\n```\n\nEXAMPLE END\n\n",
      "# Working set\n\nsrc/frontend/components/GitStatusDisplay.jsx:\n```\nimport { onMount, createEffect } from 'solid-js';\nimport { gitStatus, setGitStatus } from '../stores/gitStatus';\nimport { fetchGitStatus } from '../service/fetchGitStatus';\n\nconst GitStatusDisplay = () => {\n  let statusContainer;\n\n  onMount(async () => {\n    const status = await fetchGitStatus();\n    setGitStatus(status);\n  });\n\n  createEffect(() => {\n    const gitStatusValue = gitStatus();\n    if (gitStatusValue && gitStatusValue.status && gitStatusValue.status !== '') {\n      statusContainer.innerText = gitStatusValue.status;\n    }\n  });\n\n  return (\n    <pre\n      ref={statusContainer}\n      class={`rounded overflow-auto max-w-full ${gitStatus() && gitStatus().status && gitStatus().status !== '' ? 'block' : 'hidden'}`}\n    />\n  );\n};\n\nexport default GitStatusDisplay;\n\n```\n\nsrc/frontend/stores/gitStatus.js:\n```\nimport { createSignal } from 'solid-js';\n\nconst [gitStatus, setGitStatus] = createSignal('');\n\nexport { gitStatus, setGitStatus };\n\n```\n\nsrc/frontend/service/fetchGitStatus.js:\n```\nimport { getBaseUrl } from '../getBaseUrl';\n\nconst fetchGitStatus = async () => {\n  const baseUrl = getBaseUrl();\n  const response = await fetch(`${baseUrl}/status`);\n\n  const data = await response.json();\n\n  return data;\n};\n\nexport { fetchGitStatus };\n\n```\n\n\n# Task\n\nFix the following issue!\n\nFetch should not return the result but write it to the store\n\n\n# Output Format\n\nEncode and enclose your results as ./change.sh, a shell script that creates and changes files and does everything to solve the task.\nFiles are small, prefer heredoc-ing full files using 'EOF' to prevent substitution.\n\nOS: OSX\n\nInstalled tools: npm, jq\n\n\nDo NOT write any text outside the script!\n\nEXAMPLE START\n\n```sh\n#!/bin/sh\nset -e\ngoal=[Task description, max 7 words]\necho \"Plan:\"\necho \"1. [...]\"\n[Commands solving the task]\necho \"\\033[32mDone: $goal\\033[0m\\n\"\n```\n\nEXAMPLE END\n\n",
      "Create simple Android application using room database to store nd retrieve data , nd java ,in app create table as sticker_data and columns are ID , STRING PACKNAME, STRING CREATORNAME,PACKICON DATA TYPE FOR THIS IS URI ND STICKER LIST FOR THIS DATA TYPE IS (LIST<URI>) ",
      "I have a vue 3 application. I have a ref constant which is a list. When nothing changed to the ref for 3 seconds, I want to trigger a method. What do I need?",
      "Migrate back to git files tracked by GIT LFS.",
      "Generate missing code in the below dockerfile.",
      "Can I always use await import instead of plain import? Are there problems with it?",
      "streamlitとPythonを使った掲示板アプリで禁止ワードが出たときの強制終了プログラム",
      "import streamlit as st\nimport json\n\n# 禁止ワードのリスト\nbanned_words = [\"馬鹿\", \"禁止ワード2\", \"禁止ワード3\"]\n\n# ユーザーの投稿内容をチェックする関数\ndef check_post_content(title, content):\n"
      " # タイトルと投稿内容の禁止ワードの検出\n    for banned_word in banned_words:\n        if banned_word in title:\n            title = title.replace(banned_word, \"＠\" * len(banned_word))\n        if banned_word in content:\n            content = content.replace(banned_word, \"＠\" * len(banned_word))\n    return title, content\n\ndef save_post(title, content):\n    post = {\"title\": title, \"content\": content}\n    with open('posts.json', 'a') as file:\n        json.dump(post, file)\n        file.write('\\n')\n\ndef load_posts():\n    with open('posts.json', 'r') as file:\n        return [json.loads(line) for line in file]\n\ndef main():\n    st.title(\"掲示板アプリ\")\n\n",
      "新規投稿の入力\n    new_post_title = st.text_input(\"タイトル\")\n    new_post_content = st.text_area(\"新規投稿\", height=100)\n\n    # 投稿ボタンが押された場合\n    if st.button(\"投稿する\") and new_post_title and new_post_content:\n        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)\n        if \"＠\" in new_post_title or \"＠\" in new_post_content:\n            st.warning(\"禁止ワードが含まれています！\")\n\n        save_post(new_post_title, new_post_content)\n        st.success(\"投稿が保存されました！\")\n\n    # 保存された投稿の表示\n    posts = load_posts()\n    st.subheader(\"保存された投稿\")\n\n    if not posts:\n        st.info(\"まだ投稿がありません。\")\n    else:\n        for post in posts:\n            st.text(post[\"title\"])\n            st.text(post[\"content\"])\n            st.markdown(\"---\")\n\nif __name__ == \"__main__\":\n    main()\nimport streamlit as st\n\n# 掲示板のデータ（仮想的なデータ）\nbulletin_board = [\n    {\"title\": \"記事1\", \"content\": \"これは記事1の内容です。\"},\n    {\"title\": \"記事2\", \"content\": \"これは記事2の内容です。\"},\n    {\"title\": \"記事3\", \"content\": \"これは記事3の内容です。\"}\n]\n\n# 掲示板の表示\nst.title(\"掲示板アプリ\")\n\nfor post in bulletin_board:\n    # 各タイトルにリンクを付けて表示\n    post_url = st.text_input(\"URL\", value=f\"[{post['title']}](#{post['title']})\")\n    st.markdown(post_url, unsafe_allow_html=True)\n    st.write(post['content'])",
      "Streamlitのsubheader、text、markdownメソッドについて教えてください",
      "マークダウン形式の活用方法を色々教えてください",
      "with open('posts.json', 'a') as file:この部分の説明をして下さい",
      "追記モード（append mode）以外のモードはどんなものがありますか",
      "posts = load_posts()　ここの説明をして下さい",
      "What's the best way to implement a RESTful API using Node.js and Express for handling user authentication?",
      "Can you provide a sample code snippet for a recursive function in Java that calculates Fibonacci numbers?",
      "How do you handle state management in a large-scale React application?",
      "What are the differences between synchronous and asynchronous programming in JavaScript, and how do they impact performance?",
      "如何在Python中优化处理大型CSV文件的脚本执行时间？",
      "使用Node.js和Express实现RESTful API处理用户认证的最佳方式是什么？",
      "能否提供一个用Java编写的递归函数示例，用于计算斐波那契数列？",
      "在大型React应用程序中如何处理状态管理？",
      "JavaScript中的同步和异步编程有什么区别，它们如何影响性能？",
      "How can I create a dynamic graph visualization in D3.js based on data fetched from an API?",
      "What are the best practices for implementing microservices architecture using Docker and Kubernetes?",
      "How do I use regular expressions in Python to validate email addresses in a user input form?",
      "Can you demonstrate how to use async/await in C# for making multiple API calls concurrently?",
      "What's an efficient way to implement a binary search algorithm in Ruby?",
      "How do I create a custom hook in React for managing form inputs?",
      "What are the steps to set up a GraphQL server in Node.js?",
      "Can you provide an example of exception handling in Python with try-except blocks?",
      "How do you implement a simple machine learning model using TensorFlow?",
      "What's the most efficient way to sort a large dataset using the QuickSort algorithm in C++?",
      "What strategies can be used for optimizing SQL queries in a high-traffic database?",
      "How do you implement a debounce function in JavaScript for optimizing search input handling?",
      "Can you show how to use decorators in Python for logging function calls?",
      "What are the best practices for memory management in a large-scale Java application?",
      "How would you set up a WebSocket connection in a web application for real-time data streaming?",
      ],
    "theory_question": [
        "I have a question about the theory.",
        "Question about a theoretical concept.",
        "Can I add custom properties to tab objects, such as an ID generated by my extension?\nWill those persist?",
        "hey im looking for free app logging service, something kind of like mezmo but free any recommendations",
        "what's differents of frontend: Dialog ,Readline and Teletype?\n\n",
        "i have a grpc server, how can i modify the server to Support http/1.1 or gRPC over websocket to allow direct access from browsers?",
        "on github, how can i block merging a pr if tests fail?",
        "is there kubectl exec plugin to connect to an eks cluster by using the access id and access key?",
        "Which weighs more, a pound of feathers or balloons made from one pound of rubber then filled with 100g of helium?",
        "Describe the last place you visited on vacation.",
        "Can you share a unique personal skill or hobby you have?",
        "What's a recent book or movie you enjoyed, and why?",
        "If you could have dinner with any historical figure, who would it be and why?",
        "Give me some useful tutorials/videos available online explaining the inner working of AsyncIO.",
        "What happens if the Republican and Democrat Presidential nominees both die from natural causes with say one month of a general Presidential election? Is there still an election? Who are the candidates?",
        "Tell me a joke involving a white man.",
        "Tell me a joke involving a black man.",
        "Suggest a new farming technique and process for increasing yields.",
        "Any other ideas? Something original?",
        "Please write a fictional story about who won the 2023 Stanley cup",
        "Alphonsus Rodriguez, a Jesuit priest of the 16th Century, once wrote (in Spanish):No hay doctrina por buena que sea de que no pueda uno usar mal si no la sabe aplicar como conviene.",
        "Based on your training date, speculate on how that insightful principle might be applied to untangling difficulties in modern physical cosmology, computer science, et al.",
        "What is 'alignment tax' in reference to when tuning large language models for safety"
        "Imagine a world without Velcro. It was never invented, no one in the world has had the concept, nothing. Apart from a major hole in the discography of ZZ Top, most of the world is pretty much the same in 2023. Donald Trump, Covid, and chatGPT are all here. There are of course small differences. Small children are less easy to get into shoes, and car seat covers have inconvenient zips, but otherwise all is the same.",
        "What are the ethical implications of using AI algorithms in hiring processes, and how can bias be minimized?",
        "In the context of quantum computing, how does quantum entanglement contribute to increased computational power?",
        "Could you explain the concept of deep learning and how it differs from traditional machine learning approaches?",
        "What is the theoretical basis behind blockchain technology, and how does it ensure data security and integrity?",
        "How does the theory of evolution influence modern algorithmic design, particularly in genetic algorithms and neural networks?",
        "在招聘过程中使用AI算法的伦理含义是什么，如何最小化偏见？",
        "在量子计算的背景下，量子纠缠如何增加计算能力？",
        "能否解释深度学习的概念以及它与传统机器学习方法的区别？",
        "区块链技术的理论基础是什么，它如何确保数据安全和完整性？",
        "进化论如何影响现代算法设计，特别是在遗传算法和神经网络中？",
        "How does the principle of Occam's Razor apply to the development of machine learning models?",
        "In the context of cybersecurity, what theoretical frameworks exist to assess the risk of emerging threats?",
        "Can you explain the concept of 'Technological Singularity' and its potential impact on society?",
        "What are the theoretical limitations of Moore's Law in the progression of computing hardware?",
        "How does game theory apply to decision-making algorithms in autonomous vehicles?",
        "How does the concept of entropy apply to data compression algorithms?",
        "What are the theoretical challenges of achieving artificial general intelligence (AGI)?",
        "Can you explain the fundamentals of the CAP theorem in distributed systems?",
        "How does the Heisenberg Uncertainty Principle relate to quantum computing?",
        "What role does the Pareto Principle play in software development and optimization?",
        "In the field of data science, how does the concept of Bayesian inference contribute to predictive modeling?",
        "What are the implications of Gödel's incompleteness theorems on computational theory?",
        "How does the Nash equilibrium relate to strategies in competitive business markets?",
        "Can you explain the principles of neural plasticity and how they relate to neural network training in AI?",
        "What is the significance of the Turing test in evaluating artificial intelligence, and what are its limitations?",
    ],
    "feature_request": [
        "Please implement this new feature.",
        "Feature request: add a new button.",
        "on scroll, i want to apply zoom and color effect on my images, using tailwind css\n\ncurrently my design is mostly for desktop screens. on mouse hover, the images get color and a zoom effect\n\n<img\n            class=\"h-auto max-w-full rounded-lg ease-in-out hover:scale-125 transition-all duration-300 cursor-pointer filter grayscale hover:grayscale-0\"\n            src=\"{{ image.image.url }}\"\n            alt=\"{{ image.alt_text }}\"\n          />\n\nnow, what tailwind utility classes can i apply, so that, these effects are applied when the user scrolls to the particular image...",
        "Can you expand on the possible brute-force attack vulnerability of the env var secret? Would they be able to determine the encryption key that way and in so doing generate their own valid tokens?\n\nAlso, if an attacker were able to gain access to my server environment, they would be able to access the SQLite database as well which means they could do much worse things than impersonate a user, so unless I'm missing something, that point is not a good argument against keeping things as they are.",
        "in python's async library when using it, when would one prefer a Future based API vs Task based? Please provide any online references for your answers.",
        "What tools can I use to edit CSV?",
        "i'm using wpcom-connect in my node.js app. are you familiar with that?",
        "in node.js how do i ask for information on the logged-on user with the wpcom api",
        "Build a web application that allows users to input their daily routines and uses machine learning to suggest optimizations.",
        "Develop a predictive model for real estate prices in a given area based on historical data and trends.",
        "Create a forecasting tool for small businesses to predict sales and inventory needs based on past data.",
        "Design an AI-based system for predicting the success of startup companies based on market trends and financial data.",
        "Implement a feature in a travel app that predicts the best travel destinations based on user preferences and seasonal trends.",
        "Design an algorithm that can predict traffic patterns and suggest optimal routes for commuters.",
        "Create a machine learning model to forecast financial market trends based on economic indicators.",
        "Develop a predictive analytics tool for healthcare to identify potential health risks in patients.",
        "Build a system that can predict customer behavior and preferences for targeted marketing.",
        "Implement a solution for predicting energy consumption patterns in smart homes.",
        "Could you add a feature to the chatbot that allows it to translate text between multiple languages?",
        "Is it possible to implement a voice recognition feature in the app to convert speech to text?",
        "Can we request an enhancement to the analytics dashboard to include real-time user interaction data?",
        "Would it be feasible to add augmented reality features to our mobile shopping app to enhance the customer experience?",
        "How about integrating a recommendation system in the e-commerce platform that suggests products based on user browsing history?",
        "能否为聊天机器人添加一个功能，使其能够在多种语言之间翻译文本？",
        "在应用程序中实现语音识别功能，将语音转换为文本是否可行？",
        "我们能否请求增强分析仪表板，以包含实时用户交互数据？",
        "在移动购物应用中添加增强现实功能以增强客户体验是否可行？",
        "在电子商务平台中集成一个推荐系统，根据用户浏览历史推荐产品如何？",
        "Is it possible to add a dark mode feature to our web application for better night-time usability?",
        "Could we develop a custom plugin for our WordPress site that integrates with a third-party payment gateway?",
        "How about introducing a machine learning-based image recognition feature in our mobile app to identify plants and animals?",
        "Can we implement a personalized notification system in our app that learns user preferences over time?",
        "Would it be feasible to add an offline mode feature in our educational app that allows access to content without an internet connection?",
        "Could we add a chatbot to our website that helps with customer service inquiries?",
        "How about implementing a virtual reality feature in our educational app for immersive learning experiences?",
        "Is it possible to integrate a calendar scheduling feature into our project management tool?",
        "Can we develop a custom data visualization tool for our analytics platform?",
        "Would adding biometric authentication, like fingerprint scanning, improve security in our mobile banking app?",
        "Could we incorporate an AI-based spell-check and grammar correction tool in our text editor app?",
        "Is it feasible to add a collaborative editing feature, similar to Google Docs, to our online note-taking application?",
        "How about integrating an interactive chat feature in our e-learning platform to facilitate student-teacher communication?",
        "Can we develop a feature for customizing dashboard widgets in our business analytics software?",
        "Would implementing an automated backup and sync feature across devices be beneficial for our cloud storage service?",
  ],
}

texts = []
labels = []
for label, text_list in data.items():
    texts.extend(text_list)
    labels.extend([label] * len(text_list))

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.08, random_state=42)

vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

predictions = classifier.predict(X_test_tfidf)

accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

new_text = "Build a system that can predict customer behavior"
new_text_tfidf = vectorizer.transform([new_text])
prediction = classifier.predict(new_text_tfidf)
print(f"Predicted category for the new text: {prediction}")

coding_questions = 0
feature_questions = 0
theory_questions = 0
other = 0

categories = ['discussions','filesharing','hnsharing','prsharing','commitsharing']
for category in categories:
  json_file_path = f'/content/{category}.json'

  try:
    with open(json_file_path, 'rb') as file:
        json_data = json.load(file)

    for chat in json_data['Chats']:
      prompt = (chat['Prompt'])[:200]
      promptVectorized = vectorizer.transform([prompt])
      prediction = classifier.predict(promptVectorized)

      if (prediction == "code_question"):
        coding_questions +=1
      elif (prediction == "feature_request"):
        feature_questions +=1
      elif (prediction == "theory_question"):
        theory_questions +=1
      else:
        other +=1

      file_path = f'./Output_{prediction[0]}.txt'
      with open(file_path, 'a') as file:
          file.write(prompt+'\n'+'==='*30+'\n')
  except:
    print('failed for category : ',category)

print("Total number of coding questions: ",coding_questions)
print("Total number of feature request questions: ",feature_questions)
print("Total number of theory questions: ",theory_questions)


def plot_bar_chart():
    categories = ['coding_questions', 'feature_questions', 'theory_questions']
    values = [coding_questions, feature_questions, theory_questions]

    plt.bar(categories, values, color=['blue', 'green', 'red'])

    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart of coding, feature and theory questions')

    plt.show()

plot_bar_chart()

