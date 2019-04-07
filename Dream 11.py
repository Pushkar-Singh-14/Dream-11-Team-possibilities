

'''
***RULES***


1 wk
3-5 batsmen
1-3 AR
3-5 Bowler

credit 100
team 
max 7 from 1 team
4 from another
'''

from itertools import combinations 
names=[]
name_players=[]
team=[]
wk=[]
bowl=[]
batsman=[]
ar=[]

##Path of the text file which you found in Git Repo. or you can create your own text file
##just make sure the the pattern.
'''
for example

kock mi 9.5 wk 
parthiv rcb 8.5 wk 
kohli rcb 11.0 batsman 
r_sharma mi 10.5 batsman 
de_villiers rcb 10.0 batsman 
s_yadav mi 9.0 batsman 
Y_singh mi 8.5 batsman 
h_pandya mi 9.5 AR 
M_Ali Rcb 8.5 ar 
bumrah mi 9.5 bowl
chahal rcb 9.0 bowl 
siraj rcb 8.5 bowl 
hetmyer mi 8.5 batsman
shivam_dube mi 8.0 ar
grandhomme mi 8.5 ar
saini mi 8.0 bowl
umesh_yadav mi 9.0 bowl
pollard rcb 8.5 batsman
k_pandya rcb 8.5 ar
mcclenaghan rcb 8.5 bowl
malinga rcb 8.5 bowl
markande rcb 8.0 bowl
'''
f = open("/Users/pushkarsingh/Desktop/Team.txt", "r")

for name in f.readlines():
    name_players.append( [name.lower() for name in (name.split())])
f.close()
try:
    for player_info in name_players:
        team.append(player_info[1])
        if player_info[3]=='wk':
            wk.append(player_info)
        if player_info[3]=='bowl':
            bowl.append(player_info)
        if player_info[3]=='batsman':
            batsman.append(player_info)
        if player_info[3]=='ar':
            ar.append(player_info)
except:
    pass
        
print(list(set(team)))
team_1=list(set(team))[0]
team_2=list(set(team))[1]
print(wk)
print(bowl)
print(batsman)
print(ar)

def comb(n,c):
    comb_num=[i for i in range(n)]
    comb=combinations(comb_num,c)
    return (list(comb))

bowl_list_struct=[]
batsman_list_struct=[]
ar_list_struct=[]
bowl_list=[]
batsman_list=[]
ar_list=[]
bowl_list_player=[]
batsman_list_player=[]
ar_list_player=[]



bowl_list_struct.append([comb(len(bowl),3),comb(len(bowl),4),comb(len(bowl),5)])
for x in bowl_list_struct[0]:
    for y in x:
        bowl_list.append(y)
for seq in bowl_list:
    bowl_list_player.append([bowl[index] for index in seq])
        
batsman_list_struct.append([comb(len(batsman),3),comb(len(batsman),4),comb(len(batsman),5)])
for x in batsman_list_struct[0]:
    for y in x:
        batsman_list.append(y)
for seq in batsman_list:
    batsman_list_player.append([batsman[index] for index in seq])


ar_list_struct.append([comb(len(ar),1),comb(len(ar),2),comb(len(ar),3)])
for x in ar_list_struct[0]:
    for y in x:
        ar_list.append(y)
for seq in ar_list:
    ar_list_player.append([ar[index] for index in seq])

comb_list_1=[]
for wk_player in wk:
    for batsman_player in batsman_list_player:
        for ar_player in ar_list_player:
            for bowl_player in bowl_list_player:
                comb_list_1.append([wk_player,batsman_player,ar_player,bowl_player])

comb_list_2=[]
for comb in comb_list_1:
    comb_list_2_temp=[]
    comb_list_2_temp.append(comb[0])
    for comb_batsman in comb[1]:
        comb_list_2_temp.append(comb_batsman)
    for comb_bowl in comb[3]:
        comb_list_2_temp.append(comb_bowl)
    if len(comb[2])<=3:
        for comb_ar in comb[2]:
            comb_list_2_temp.append(comb_ar)
    if len(comb[2])==4:
        comb_list_2_temp.append(comb[2])
    comb_list_2.append([temp for temp in comb_list_2_temp ])

comb_list_3=[]

for comb in comb_list_2:
    if len(comb)==11:
        score=0
        team_1_counter=0
        team_2_counter=0
        for comb_1 in comb:
            score+=float(comb_1[2])
            if comb_1[1]==team_1:
                team_1_counter+=1
            if comb_1[1]==team_2:
                team_2_counter+=1
        #print(score)
        if score<=100.0:
            
            
            if team_1_counter<=7 and team_2_counter<=7:
                comb_list_3.append(comb)

## All Teams are in comb_list_3 list, you can save it in text file or do whatever you want with it.
                
print(len(comb_list_3))
