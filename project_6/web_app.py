import streamlit as st
from sklearn.preprocessing import MinMaxScaler 
import pandas as pd
import numpy as np
from scipy.stats import poisson
import os

st.title('FIFA World Cup Qatar 2022™ A.I.')

# here comes all the code that we just did!
cwd = os.getcwd()
st.title(cwd)
# teams = pd.read_excel('data/DadosCopaDoMundoQatar2022.xlsx',
#                         sheet_name ='selecoes',
#                         names = ['Teams_BR',
#                                  'Group',
#                                  'GroupNumber',
#                                  'Team',
#                                  'FIFAsRankPosition',
#                                  'MarketValue',
#                                  'FIFAsRankingPoints',
#                                  'Confederation',
#                                  'WorldCups',
#                                  'SpotlightPlayer',
#                                  'PictureOfPlayer',
#                                  'FlagsLinkSmall',
#                                  'FlagsLinksBig'],
#                         index_col = 0)

# fifa = pd.DataFrame(teams['FIFAsRankingPoints'])
# minmax = MinMaxScaler(feature_range=(0.15,1))                  
# fifa_norm = minmax.fit_transform(fifa.values.reshape(-1,1))
# fifa.insert(1,"FIFAsRankingPointsNorm", fifa_norm.flatten(), True)
# weights = fifa['FIFAsRankingPointsNorm']

# def Result(gols1, gols2):                               # returns game results for team1 
#     if gols1 > gols2:
#         res = 'V'                                       # victory
#     if gols1 < gols2:                           
#         res = 'D'                                       # defeat
#     if gols1 == gols2:
#         res = 'T'                                       # tie
#     return res

# def PoissonMean(team1, team2):                          # calculates Poisson mean based on weight series
#     weight1 = weights[team1]
#     weight2 = weights[team2] 
#     mgols = 2.75
#     l1      = mgols*weight1/(weight1 + weight2)              # calculating lambda_n
#     l2      = mgols*weight2/(weight1 + weight2)
#     return [l1, l2]
    
# def Dist(mean):                                         # returns the prob of certain number of goals
#     probs = []
#     for i in range(7):                                  # remember Brazil x Germany (0x7)
#         probs.append(poisson.pmf(i,mean))
#     probs.append(1-sum(probs))
#     return pd.Series(probs, index = ['0', '1', '2', '3', '4', '5', '6', '7+'])

# def Prob(team1, team2):                                 # propability matrix
#     l1, l2 = PoissonMean(team1, team2)
#     d1, d2 = Dist(l1), Dist(l2)  
#     matrix = np.outer(d1, d2)                           

#     victory = np.tril(matrix).sum()-np.trace(matrix)    # triangular lower
#     defeat  = np.triu(matrix).sum()-np.trace(matrix)     # triangular upper
#     probs   = np.around([victory, 1-(victory+defeat), defeat], 3)     # 1-vic+def is tie!
#     probsp  = [f'{100*i:.1f}%' for i in probs]

#     names           = ['0', '1', '2', '3', '4', '5', '6', '7+']
#     matrix          = pd.DataFrame(matrix, columns = names, index = names)
#     matrix.index    = pd.MultiIndex.from_product([[team1], matrix.index])      # to give us team1 and number of goals
#     matrix.columns  = pd.MultiIndex.from_product([[team2], matrix.columns]) 
#     output          = {'team1': team1, 'team2': team2, 
#                     'W1': weights[team1], 'w2': weights[team2], 
#                     'lambda1': l1, 'lambda2': l2, 
#                     'probabilities': probsp, 'matrix': matrix}
#     return output

# def Points(gols1, gols2):                               # gives the score for each team after the game
#     rst = Result(gols1, gols2)
#     if rst == 'V':
#         points1, points2 = 3, 0
#     if rst == 'E':
#         points1, points2 = 1, 1
#     if rst == 'T':
#         points1, points2 = 0, 3
#     return points1, points2, rst


# def Game(team1, team2):                                 
#     l1, l2  = PoissonMean(team1, team2)
#     gols1   = int(np.random.poisson(lam = l1, size = 1))
#     gols2   = int(np.random.poisson(lam = l2, size = 1))
#     saldo1  = gols1 - gols2
#     saldo2  = -saldo1
#     points1, points2, result = Points(gols1, gols2)
#     score   = '{}x{}'.format(gols1, gols2)
#     return [gols1, gols2, saldo1, saldo2, points1, points2, result, score]

# # stream lit part

# teamlist = teams.index.tolist()
# teamlist.sort()
# teamlist2 = teamlist.copy()

# j1, j2 = st.columns(2)
# team1 = j1.selectbox('Choose team 1', teamlist)
# teamlist2.remove(team1)
# team2 = j2.selectbox('Choose team 2', teamlist2, index = 1)
# st.markdown('---')

# game = Prob(team1,team2)
# prob = game['probabilities']
# matrix = game['matrix']

# col1, col2, col3, col4, col5 = st.columns(5)
# col1.image(teams.loc[team1, 'FlagsLinksBig'])
# col2.metric(team1, prob[0])
# col3.metric('Tie', prob[1])
# col4.metric(team2, prob[2])
# col5.image(teams.loc[team2, 'FlagsLinksBig'])

# st.markdown('---')
# st.markdown('## Scores probabilities matrix')

# def roundprob(x):
#     return f'{str(round(100*x,1))}%'

# st.table(matrix.applymap(roundprob))

# st.markdown('---')
# st.markdown('## Cup games probabilities')

# cupgames = pd.read_excel('data/outputEstimativasJogosCopa.xlsx', index_col = 0)

# st.table(cupgames[['grupo','seleção1','seleção2', 'Victory', 'Tie', 'Defeat']])


