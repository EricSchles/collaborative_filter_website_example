from pgmpy import inference
from pgmpy.models import BayesianModel
from pgmpy.factors import TabularCPD
from app.models import Jokes

number_of_users = len(set([joke.user_id for joke in Jokes.query.all()]))
# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianModel([('', '')])

# Defining individual CPDs.
cpd_decision = TabularCPD(variable='Decision', variable_card=5, values=[]) #number of times this user has chosen a category
cpd_preference = TabularCPD(variable='Preference', variable_card=10, values=[]) #number of times they've chosen a category given another option
cpd_user_category = TabularCPD(variable='UserCategory', variable_card=5, values=[]) #number of overall users on the site with each category as a preference
cpd_follower = TabularCPD(variable='Follower', variable_card=2, values=[]) #they follow other people or they don't

# The representation of CPD in pgmpy is a bit different than the CPD shown in the above picture. In pgmpy the colums
# are the evidences and rows are the states of the variable. So the grade CPD is represented like this:
#
#    +---------+---------+---------+---------+---------+
#    | diff    | intel_0 | intel_0 | intel_1 | intel_1 |
#    +---------+---------+---------+---------+---------+
#    | intel   | diff_0  | diff_1  | diff_0  | diff_1  |
#    +---------+---------+---------+---------+---------+
#    | grade_0 | 0.3     | 0.05    | 0.9     | 0.5     |
#    +---------+---------+---------+---------+---------+
#    | grade_1 | 0.4     | 0.25    | 0.08    | 0.3     |
#    +---------+---------+---------+---------+---------+
#    | grade_2 | 0.3     | 0.7     | 0.02    | 0.2     |
#    +---------+---------+---------+---------+---------+

cpd_user = TabularCPD(variable='User', variable_card=5, 
                   values=[],
                  evidence=['Decision', 'Preference'],
                  evidence_card=[5, 10])

cpd_choice = TabularCPD(variable='Choice', variable_card=, 
                   values=[],
                   evidence=['Decision', 'Preferences','UserCategory','Follower'],
                   evidence_card=[])


# Associating the CPDs with the network
model.add_cpds() #ToDo

# check_model checks for the network structure and CPDs and verifies that the CPDs are correctly 
# defined and sum to 1.
model.check_model()
