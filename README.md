# BuddyBot
Buddy Bot is a useful chatbot which enables the desktop users to have a conversation, ask questions, entertain themselves through games, jokes,quotes etc .From serving a specific purpose, answering business related questions, acting as a personal assistant to being a 24/7 available chatting friend.

The coding part of Buddy Bot is fully worked with python. This includes many library functions like NLTK, TensorFlow, NumPy and a few others. Json is a python package that helps the query data set to get parsed by the Python code. This json file has the query with different tags. Each tag has a set of patterns and responses. The GUI is also developed using a Python package called tkinter. Tkinter is the standard interface for GUI creations.
Here the proposed system works on a manually developed Chatbot querying dataset and it produces relevant responses based on the pre-defined repository. Basically Keras is a minimalist Python library that we use for deep learning. Here a Deep Learning model from keras called Sequential is used for implementing the model. Data is considered as the basic key to a chatbot system. At a particular interval of time, the data set is to be updated again and again and should retrain the model to improve accuracy. Otherwise the data gets outdated. After dataset creation, various preprocessing tasks are carried out for cleaning the data to remove any content that does not have any useful information in them. Task of preprocessing is done here in the complete dataset which contains various user input queries and responses and also the same preprocessing tasks are carried out when a particular input is given by the user. After cleaning the data, It should be converted into such a way a machine can understand. For that purpose we use this feature generation technique. Here the concept of Bag Of Words(BOW) is considered for generating features from the input text. In this model, a text such as a sentence or even a document is represented as the bag (multiset) of its corresponding words, without considering the grammar and even word order but keeping multiplicity. The output from this feature generator will be given as the input to the deep learning Model to predict the response.

The five steps used to create the chatbot:
1.	Import and load the data file
2.	Preprocess data
3.	Create training and testing data
4.	Build the model
5.	Predict the response

Screenshots of Buddybot:



![Screenshot 2023-12-16 194707](https://github.com/sakshiisinghh/BuddyBot/assets/87891878/05aa7e10-cf61-4b0b-993c-2961c05510d1)





![Screenshot 2023-12-16 194731](https://github.com/sakshiisinghh/BuddyBot/assets/87891878/27a58a3e-966f-4e8a-875d-954004d6386a)




![Screenshot 2023-12-16 194759](https://github.com/sakshiisinghh/BuddyBot/assets/87891878/30952dd2-ff25-4641-ba98-b5b9d8447ea1)




![Screenshot 2023-12-16 194817](https://github.com/sakshiisinghh/BuddyBot/assets/87891878/874f1ff7-f958-4bfc-97e0-c6d136d8c233)




![Screenshot 2023-12-16 194844](https://github.com/sakshiisinghh/BuddyBot/assets/87891878/fc94a39a-d35a-4936-a9b5-658b61c7936a)




![Screenshot 2023-12-16 194919](https://github.com/sakshiisinghh/BuddyBot/assets/87891878/f2cbf3bf-8ad5-46b4-ab43-2cd9f1140c14)
