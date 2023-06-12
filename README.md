# PLAYER PERFORMANCE ANALYSIS IN CRICKET: WITH THE FUSION OF MACHINE LEARNING

1. INTRODUCTION

Cricket is a sport played by two teams with each side having eleven players. Each team is a right
blend of batsmen, bowlers and all-rounders. The batsmen’s role is to score maximum runs possible and the bowlers have to take maximum wickets and restrict the other team from scoring runs at the same time. All-rounders are the players who can both bat and bowl and they contribute by scoring runs and taking wickets. Each player contributes towards the overall performance of the team by giving his best performance in each match. Each player’s performance varies with factors like the team he is playing against and the ground at which the match is being played. It is important to select the right players that can perform the best in each match. The performance of a player also depends on several factors like his current form, his performance against a particular team, his performance at a particular venue etc. The team management, the coach and the captain analyze each player’s characteristics, abilities and past stats to select the best playing XI for a given match. In other words, they try to predict the players’ performance for each match. In this paper, we predict the players’ performance in One Day International (ODI) matches by analyzing their characteristics and stats using supervised machine learning techniques. For this, we predict batsmen’s and bowlers’ performance separately as how many runs will a batsman score and how many wickets will a bowler take in a particular match.

2. IMPLEMENTATION

Our project deals with a machine learning prediction model that is developed to get better accuracy in predicting team players in the game of cricket. As we know any model requires training in order to get results for new input / testing data. In our model, as shown below.


Coach has the ability to update with the training dataset that we use to train our model. Coach uses attributes like score, strike rate, wickets, matches, average scores and many more attributes that depend on the type of player we need to train. Both batsman and bowler datasets are used as training datasets. Now captain can view the dataset uploaded by coach. Captain selects players (assume new players) as part of their team depending upon the model suggestion that gives ranking of player’s given by the captain as testing dataset as shown in Fig:6. This process is implemented by four machine learning algorithms such as naïve bayes, decision tree, SVM, random forest. As we trained on all the models and compared them based on accuracy, precision and recall, we can say that random forest is better than other three classifiers. We have implemented the idea with better GUI that makes very easy for the users to use our model. The rank is shown in sorted order and accuracy is shown as a bar chart plot that can be easily distinguished by a user visually as in the following figure.


NAIVE BAYES

In this method we are mainly using Bayesian learning method; here the values are independent to each other. The input is taken from the set of values and different attributes are combined then f(x) will be taken. In the training set of attributes will be taken then P () and P () learning steps are estimated, by this process normal and intrusion will be detected. Totally there are three algorithms those are Gaussian, Bernoulli, and multinomial naïve bayes algorithm. We discussed about continuous and discrete data values, in Gaussian model continuous values are distributed, Bernoulli is used for binary feature and multinomial is used for discrete values. This is the easiest and speed detection algorithm compared to the algorithms compared to all the algorithms mathematical calculations are different in this method, but it this method features are independent relation.
DECISION TREE

Branching method is use to get the output result, for this we can use discrete value attributes or else continuous value attributes depending upon the input. The trained trees will be given in the form of ifthen rules. Mainly there are three basic parts are there in decision tree algorithm those are decision node, branch node and leaf node. These three will be used for testing the attribute, in the decision mode test of the attribute will be done, in the branch mode values will be taken and in leaf node class can be defined.

SUPPORT VECTOR MACHINE

In this method a hyper plane is drawn in between the classifiers, this plane will separate the two classifiers. The error can be identified by increasing the distance between hyper planes in both sides. The points which show on the line are known as supporting vector points, a linear line is drawn in between the data points, but when there is a non-linear point then SVM can’t detect those points, to solve this problem we are using a high dimensional space it is known as feature space. In this kernel function is used for the new classification. Based on this kernel function SVM will be divided into two types those are Non-linear SVM and linear SVM. By using the linear kernel hyper plane is separated in the training set if the separation is not possible by linear then we apply the non-linear kernel function. A visual image of how SVM works is in Fig. 2.
Originally SVM was used for the binary classification. However, it has also developed many multiclass SVM algorithms.

RANDOM FOREST

Random Forests is a classification and regression ensembles method. Random forests are set of decision trees where each tree depends on a random vector that is independently checked and the same distribution of the forest trees. The algorithm creates a series of decision trees that create a forest. Generation of each tree is achieved by selecting random attributes to decide the split at each node. Using random subspace method Tim Kam Ho gave the 1st random forest method After Breiman Leo continued the algorithm in his paper and it was officially called Random Forests. The later method of Classification and Regression Trees (CART) is used in growth trees. The trees grow to their maximum size and are not being cropped. It is a technique of non-parametric induction, used to generate trees for classification and regression

3. CONCLUSION:

Four multiclass classification algorithms were used and compared. Wherein, The Random Forest Classifier turned out to be the most accurate classifier for both the datasets with an accuracy of 90.74% for predicting runs scored by a batsman and 92.25% for predicting wickets taken by a bowler. Results of SVM were surprising as it achieved an accuracy of just 51.45% for predicting runs and 68.78% for predicting wickets. Similar studies can be carried out for other formats of the game i.e. test cricket and T20 matches. The models for these formats can be shaped to reflect required characteristics of the players; e.g. batsmen need to have patience and ability to play longer innings in test matches whereas score more runs in less overs in T20 matches. Similarly, bowlers need to have stronger wicket taking abilities in test matches and better economy rate i.e. conceding less runs in T20 matches.
