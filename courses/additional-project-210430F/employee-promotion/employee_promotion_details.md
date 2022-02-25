# Background & Context

Employee Promotion means the ascension of an employee to higher ranks, this aspect of the job is what drives employees the most.
The ultimate reward for dedication and loyalty towards an organization and HR team plays an important role in handling all these promotion tasks based on ratings and other attributes available.

The HR team in JMD company stored data of promotion cycle last year, which consists of details of all the employees in the company working last year and also
if they got promoted or not, but every time this process gets delayed due to so many details available for each employee - it gets difficult to compare and decide.

So this time HR team wants to utilize the stored data to make a model, that will predict if a person is eligible for promotion or not.

You as a data scientist at JMD company, need to come up with a model that will help the HR team to predict if a person is eligible for promotion or not.

# Objective

Explore and visualize the dataset.
Build a classification model to predict if the customer has a higher probability of getting a promotion
Optimize the model using appropriate techniques
Generate a set of insights and recommendations that will help the company

# Data Dictionary

employee_id: Unique ID for employee
department: Department of employee
region: Region of employment (unordered)
education: Education Level
gender: Gender of Employee
recruitment_channel: Channel of recruitment for employee
no_ of_ trainings: no of other trainings completed in previous year on soft skills, technical skills etc.
age: Age of Employee
previous_ year_ rating: Employee Rating for the previous year
length_ of_ service: Length of service in years
awards_ won: if awards won during previous year then 1 else 0
avg_ training_ score: Average score in current training evaluations
is_promoted: (Target) Recommended for promotion
Submission Guidelines :

There are two parts to the submission: 
A well commented Jupyter notebook [format - .ipynb]
A submission in html format
Any assignment found copied/ plagiarized with other groups will not be graded and awarded zero marks
Please ensure timely submission as any submission post-deadline will not be accepted for evaluation
Submission will not be evaluated if,
it is submitted post-deadline, or,
more than 2 files are submitted
Happy Learning!!

 --

 Scoring guide (Rubric) - Employee Promotion Prediction
Criteria	Points
Perform an Exploratory Data Analysis on the data
- Univariate analysis - Bivariate analysis - Use appropriate visualizations to identify the patterns and insights - Any other exploratory deep dive
6
Illustrate the insights based on EDA
Key meaningful observations on the relationship between variables
5
Data Pre-processing
Prepare the data for analysis - Missing value Treatment, Outlier Detection(treat, if needed- why or why not ), Feature Engineering, Prepare data for modeling
6
Model building - Logistic Regression
- Make a logistic regression model - Improve model performance by up and downsampling the data - Regularize above models, if required
6
Model building - Bagging and Boosting
- Build Decision tree, random forest, bagging classifier models - Build Xgboost, AdaBoost, and gradient boosting models
9
Hyperparameter tuning using grid search
- Tune all the models using grid search - Use pipelines in hyperparameter tuning
9
Hyperparameter tuning using random search
- Tune all the models using ramdonized search - Use pipelines in hyperparameter tuning
9
Model Performances
- Compare the model performance of all the models - Comment on the time taken by the grid and randomized search in optimization
5
Actionable Insights & Recommendations
- Business recommendations and insights
5
Points	60