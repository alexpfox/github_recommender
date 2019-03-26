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


"""
from textgenrnn import textgenrnn
from keras import backend

def generate(author, seed=''):
    print('Loading model...')
    textgen = textgenrnn(weights_path='wilde_weights_e13_bi.hdf5')
    #frost_weights_e15_bi_e_300.hdf5, eliot_weights_2.hdf5, kaur_weights_3.hdf5, shakespeare_weights_e17_bi.hdf5, wilde_weights_e13_bi.hdf5

    if author == 'Wilde':
        textgen = textgenrnn(weights_path='wilde_weights_e13_bi.hdf5')
        #print('Generating...')
        lines = textgen.generate(n=1, prefix=seed, temperature=0.4, return_as_list=True)
    elif author == 'Frost':
        textgen = textgenrnn(weights_path='frost_weights_e15_bi_e_300.hdf5')
        #print('Generating...')
        lines = textgen.generate(n=3, prefix=seed, temperature=0.4, return_as_list=True)
    elif author == 'Kaur':
        textgen = textgenrnn(weights_path='kaur_weights_6.hdf5')
        #print('Generating...')
        lines = textgen.generate(n=2, prefix=seed, temperature=0.6, return_as_list=True)
    elif author == 'Eliot':
        textgen = textgenrnn(weights_path='eliot_weights_2.hdf5')
        #print('Generating...')
        lines = textgen.generate(n=3, prefix=seed, temperature=0.6, return_as_list=True)
    elif author == 'Shakespeare':
        textgen = textgenrnn(weights_path='shakespeare_weights_e17_bi.hdf5')
        #print('Generating...')
        lines = textgen.generate(n=4, prefix=seed, temperature=0.4, return_as_list=True)

        #lines = #process out extra punctuation at the end of the quote

    # print('Generating...')
    # lines = textgen.generate(n=3, prefix=seed, temperature=0.4, return_as_list=True)

    # flask is running multiple thread, tf doesn't like having the model initialized across threads
    # we use keras to clear the tf session after generating a result.
    backend.clear_session()
    return lines

# test code for running this file on its own
# python3 generate.py
if __name__== "__main__":
    print('Testing...\n', generate('wilde', 'Tears'))




# from textgenrnn import textgenrnn
# from keras import backend

# def generate(author, seed=''):
#     print('Loading model...')
#     textgen = textgenrnn(weights_path='frost_weights.hdf5') 
#     #frost_weights_e15_bi_e_300.hdf5, eliot_weights_2.hdf5, kaur_weights_3.hdf5, shakespeare_weights_e17_bi.hdf5, wilde_weights_e13_bi.hdf5

#     print('Generating...')
#     lines = textgen.generate(n=3, prefix=seed, temperature=0.4, return_as_list=True)

#     # flask is running multiple thread, tf doesn't like having the model initialized across threads
#     # we use keras to clear the tf session after generating a result.
#     backend.clear_session()
#     return lines

# # test code for running this file on its own
# # python3 generate.py
# if __name__== "__main__":
#     print('Testing...\n', generate('wilde', 'Tears'))        

"""