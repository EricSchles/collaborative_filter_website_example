from pgmpy import inference
from pgmpy.models import BayesianModel
from app.models import Jokes 
from pgmpy.estimators import ExhaustiveSearch, BdeuScore, K2Score, BicScore
import pandas as pd

# es = ExhaustiveSearch(data, scoring_method=bic)
# best_model = es.estimate()
# print(best_model.edges())

# print("\nAll DAGs by score:")
# for score, dag in reversed(es.all_scores()):
#     print(score, dag.edges())

def train_joke_type_selection():
    #one table
    jokes = Jokes.query.all()
    joke_preferences = []
    for i in range(sum([joke_preference.nerd_joke for joke_preference in jokes])):
        joke_preferences.append("nerd joke")
    for i in range(sum([joke.weird_joke for joke in jokes])):
        joke_preferences.append("weird joke")
    for i in range(sum([joke.cat_meme for joke in jokes])):
        joke_preferences.append("cat meme")
    for i in range(sum([joke.dog_meme for joke in jokes])):
        joke_preferences.append("dog meme")
    for i in range(sum([joke.dad_joke for joke in jokes])):
        joke_preferences.append("dad joke")
    data = pd.DataFrame()
    for joke_preference in joke_preferences:
        data = data.append({"joke_preference":joke_preference},ignore_index=True)
        
    bic = BicScore(data)
    import code
    code.interact(local=locals())
    es = ExhaustiveSearch(data, scoring_method=bic)
    best_model = es.estimate()
    return best_model

def main():
    number_of_users = len(set([joke.user_id for joke in Jokes.query.all()]))
    # Defining the model structure. We can define the network by just passing a list of edges.
    model = BayesianModel([('Decision', 'User')])

    # Defining individual CPDs.

    jokes = Jokes.query.all()
    total_jokes = sum([joke.nerd_joke + joke.weird_joke + joke.cat_meme + joke.dog_meme + joke.dad_joke
                   for joke in jokes])

    prob_nerd_jokes = sum([joke.nerd_joke for joke in jokes])/float(total_jokes)
    prob_weird_jokes = sum([joke.weird_joke for joke in jokes])/float(total_jokes)
    prob_cat_memes = sum([joke.cat_meme for joke in jokes])/float(total_jokes)
    prob_dog_memes = sum([joke.dog_meme for joke in jokes])/float(total_jokes)
    prob_dad_jokes = sum([joke.dad_joke for joke in jokes])/float(total_jokes)
    cpd_decision = TabularCPD(variable='Decision', variable_card=5, values=[prob_nerd_jokes, prob_weird_jokes, prob_cat_memes, prob_dog_memes, prob_dad_jokes])
    #number of times this user has chosen a category

    # num_dad_over_nerd = sum([joke.dad_over_nerd for joke in jokes])/float(total_jokes)
    # num_nerd_over_dad = sum([joke.nerd_over_dad for joke in jokes])/float(total_jokes)
    # num_dad_over_weird = sum([joke.dad_over_weird for joke in jokes])/float(total_jokes)
    # num_weird_over_dad = sum([joke.weird_over_dad for joke in jokes])/float(total_jokes)
    # num_dad_over_cat = sum([joke.dad_over_cat for joke in jokes])/float(total_jokes)
    # num_cat_over_dad = sum([joke.cat_over_dad for joke in jokes])/float(total_jokes)
    # num_dad_over_dog = sum([joke.dad_over_dog for joke in jokes])/float(total_jokes)
    # num_dog_over_dad = sum([joke.dog_over_dad for joke in jokes])/float(total_jokes)
    # num_nerd_over_weird = sum([joke.nerd_over_weird for joke in jokes])/float(total_jokes)
    # num_weird_over_nerd = sum([joke.weird_over_nerd for joke in jokes])/float(total_jokes)

    #cpd_preference = TabularCPD(variable='Preference', variable_card=20, values=[])
    #number of times they've chosen a category given another option


    # The representation of CPD in pgmpy is a bit different than the CPD shown in the above picture. In pgmpy the colums
    # are the evidences and rows are the states of the variable. So the grade CPD is represented like this:
    #
    #    +---------  +---------+---------+---------+---------+
    #    | Decision  | dad     | cat     | dog     | weird   | nerd |
    #    +---------  +---------+---------+---------+---------+
    #    | user_dad | 0.3     | 0.05    | 0.9     | 0.5     |
    #    +---------+---------+---------+---------+---------+
    #    | user_cat | 0.4     | 0.25    | 0.08    | 0.3     |
    #    +---------+---------+---------+---------+---------+
    #    | user_nerd | 0.3     | 0.7     | 0.02    | 0.2     |
    #    +---------+---------+---------+---------+---------+
    #    | user_dog | 0.3     | 0.7     | 0.02    | 0.2     |
    #    +---------+---------+---------+---------+---------+
    #    | user_weird | 0.3     | 0.7     | 0.02    | 0.2     |
    #    +---------+---------+---------+---------+---------+

    #number of overall users on the site with each category as a preference
    # a user prefers a type of joke if the most jokes they clicked on, is of a given type
    total_num_users = Joke.query.count()
    user_type_counts = {"nerd":0,"weird":0,"dad":0,"cat":0,"dog":0}
    user_preference_counts = {
        "nerd":{
            "weird":0,
            "dad": 0,
            "cat": 0,
            "dog": 0,
            "nerd": 0
            },
        "weird":{
            "nerd": 0,
            "dad": 0,
            "cat": 0,
            "dog": 0,
            "weird": 0
        },
        "cat":{
            "nerd":0,
            "dad":0,
            "dog":0,
            "weird":0,
            "cat":0
        },
        "dog":{
            "nerd":0,
            "dog":0,
            "cat":0,
            "weird":0,
            "dad":0
        },
        "dad":{
            "dad":0,
            "nerd":0,
            "weird":0,
            "cat":0,
            "dog":0
        }
    }

    list_of_keys = ["nerd", "weird", "dad", "cat", "dog"]
    for joke in jokes:
        dicter = {
            "nerd":joke.nerd_joke,
            "weird":joke.weird_joke,
            "dad":joke.dad_joke,
            "cat":joke.cat_meme,
            "dog":joke.dog_meme
        }
        for key in list_of_keys:
            user_preference_counts[ user_type_counts[ max(dicter) ] ][key] = dicter[key]/float(total_jokes)
        

    # cpd_user = TabularCPD(variable='User', variable_card=5, 
    #                    values=[ user_table_results ],
    #                   evidence=['Decision'],
    #                   evidence_card=[5])

    # # cpd_follower = TabularCPD(variable='Follower', variable_card=2, values=[]) #they follow other people or they don't

    # # cpd_choice = TabularCPD(variable='Choice', variable_card=, 
    # #                    values=[],
    # #                    evidence=['Decision', 'Preferences','UserCategory','Follower'],
    # #                    evidence_card=[])


    # # Associating the CPDs with the network
    # model.add_cpds(cpd_decision, cpd_user) #ToDo

    # # check_model checks for the network structure and CPDs and verifies that the CPDs are correctly 
    # # defined and sum to 1.
    # print(model.check_model())
