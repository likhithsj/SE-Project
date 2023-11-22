# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Sample data (replace this with your labeled dataset)
data = {
    "bug": [
      "Can you convert my code to the second solution?",
      "I have a vue 3 application. I have a ref constant which is a list. When nothing changed to the ref for 3 seconds, I want to trigger a method. What do I need?",
      "migrate back to git files tracked by GIT LFS",
      "generate missing code in the below dockerfile\n\n-----\nFROM ubuntu:20.04\n\nARG AWS_ACCESS_KEY_ID\nARG AWS_SECRET_ACCESS_KEY\nARG AWS_SESSION_TOKEN\nARG DEBIAN_FRONTEND=noninteractive\n\nLABEL org.opencontainers.image.authors=\"Sebastian Sasu <sebi@nologin.ro>, Cristian Magherusan-Stanciu <cmagh@amazon.de>, Brooke McKim <brooke@vantage.sh>\"\n\nRUN apt-get update\nRUN apt-get install -y python3 pip locales\nRUN apt-get install -y nodejs\nRUN apt-get install -y npm\nRUN npm install --global sass\nRUN python3 -m pip install -U pip setuptools\nRUN locale-gen \"en_US.UTF-8\"\n\nWORKDIR /opt/app\n\nCOPY requirements.txt .\nRUN pip3 install -r requirements.txt\n\nCOPY . .\n\nENV AWS_ACCESS_KEY_ID=\n\nRUN invoke build\n\nEXPOSE 8080\n\nCMD [\"invoke\", \"serve\"]\n",
      "The Clojure file contents are as follows:\n\n\n(ns foo.bar\n  (:require\n   [clojure.java.io :as io]\n   [clojure.string :as str]))\n\n\nAnd my request is:\n\nCreate a function that takes a resource path, reads its contents, and prints to stdout all its text converted to all-caps.",
      "how can i do it with nginx",
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
      "Create simple Android application using room database to store nd retrieve data , nd java ,in app create table as sticker_data and columns are ID , STRING PACKNAME, STRING CREATORNAME,PACKICON DATA TYPE FOR THIS IS URI ND STICKER LIST FOR THIS DATA TYPE IS (LIST<URI>) "
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
        "Please write a fictional story about who won the 2023 Stanley cup"
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
        "Implement a solution for predicting energy consumption patterns in smart homes."
  ],
}

# Combine texts and labels
texts = []
labels = []
for label, text_list in data.items():
    texts.extend(text_list)
    labels.extend([label] * len(text_list))
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Convert text data to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test_tfidf)

# Evaluate the performance of the model
accuracy = metrics.accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Example usage: classify a new text
new_text = "Create a forecasting tool for small businesses to predict sales and inventory needs based on past data."
new_text_tfidf = vectorizer.transform([new_text])
prediction = classifier.predict(new_text_tfidf)
print(f"Predicted category for the new text: {prediction}")