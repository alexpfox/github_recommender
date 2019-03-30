# ugh

user_dict = {
        'vassim': ['jmitchel3', 'fantasylc', 'ShawnYangYang'],
        'andrew': ['didrocks', 'alittleceline', 'rauchg'],
        'dmd': ['brosner', 'wycats', 'schacon'],
        'laincode': ['JacksonTian', 'munificent', 'davecheney'],
        'aphyr': ['dhh','jinzhu','ask'],
        'jacobian': ['benoitc','tmm1','mattt'],
        'robbyrussell': ['coleifer','bitprophet','jezdez'],
        'sebhtml': ['Newozz', 'gokhanmoral','chanezon'],
        'chriscz': ['meatballhat','robincurry','Psycho7'],
        'mitchellh': ['mislav','sstephenson','andrew'],
        'alexpfox': ['felixge','CamDavidsonPilon','cloudwu']
        }

def get_preds(username):
    prediction = user_dict.get(username)
    return prediction

# test code for running this file on its own
# python3 generate.py
if __name__== "__main__":
    print('Testing...\n', get_preds('vassim'))