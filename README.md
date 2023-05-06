# Study of Internet Metrics on Document Collaboration Applications

Author: Katherine Lee (ksl103), Kuhu Halder (kh761) <br/>
Course: [CS 553](https://people.cs.rutgers.edu/~sn624/553-S23/index.html), Design of Internet Services (Graduate Course) <br/>
Professor: Srinivas Narayana <br/>
Semester: Spring 2023

Final Paper can be found [here]()

## Table of Contents
* [Introduction](#introduction)
* [Technologies/Frameworks](#technologies)
* [Folder Contents](#folder-contents)
* [Setup](#setup)

## Introduction
-----------

Document collaboration has become an essential feature in word processors and similar applications. Users expect to be able to share their documents with friends and colleagues in order to be able to view, edit, and collaborate in real-time. While document collaboration is vital to these tools, especially in the post-pandemic era as people continue to work remotely, there is very little research on how well they perform. This study seeks to understand how connectivity and network affect the performance of some of the most popular collaboration tools: Google Docs, Microsoft Word, and Notion, and how performance can be improved by studying a small custom document collaboration app.

## Technologies/ Frameworks

- [React.js](https://reactjs.org/)
- [Node.js](https://nodejs.org/en/)
- [MongoDB](https://www.mongodb.com/)
- [Python](https://www.python.org/)
- [Nodemon](https://www.npmjs.com/package/nodemon)
- [Autocannon](https://www.npmjs.com/package/autocannon)

## Folder Contents

- client folder contains all files for the custom document collaboration app written in Javascript using React.js framework
- experiments folder contains all experiment test data for all individual applications. Experiments are broken down into: 
    * One User Typing
    * Two Users Typing
    * One User Typing With Throttling
    * Two Users Typing With Throttling
    * One User Typing With Network Disconnect
    * Two Users Typing With Network Disconnect
    * Image Upload
- exoeriments/graphs: Graphs folder inside experiments contains all graphs used in paper and is divided between individual application graphs and combined application graphs.  
- server folder contains all files for the server used to run the custom document collaboration app written in Javascript using Node.js and MongoDB

## Setup

To run our server, you will need to install the following dependencies:
- [Node.js](https://nodejs.org/en/download/)
- [Python 3](https://www.python.org/downloads/)
- [MongoDB](https://docs.mongodb.com/manual/installation/)
- [Nodemon](https://www.npmjs.com/package/nodemon)

Make sure npm (Node package manager is installed) and Python3 is intalled.

1. Clone the repository
```
git clone https://github.com/kuhuhalder/document-collaboration-app
```

2. Install dependencies
```
cd client
npm install .
cd ../server
npm install .
```

3. To run the server, run the following commands in the root directory:
```
cd server
nodemon server.js
```

4. To run our custom document collaboration app, run the following commands in the root directory in a new terminal window
```
cd client
npm start
```

The app should open in a new browser window at http://localhost:3000/

5. To run the experiments, run the following commands in the root directory in a new terminal window
```
autocannon -c 100 -d 10 -w 50 -l [link to app]
```










