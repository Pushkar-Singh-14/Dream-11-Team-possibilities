Dream 11 / MyTeam 11 total team combination considering the points and other rules. 
===================


This is a fun project which create a list of all the team combinations. It absolutely take care of all the rules that they have. I created it considering the rules of Dream 11 app only and assuming that MyTeam 11 has the same rules too.

----------


Rules
-------------

***RULES***

> - Total usable credit is 100, As soon as you have enough credit you can select players.

> - Only one WK is allowed
> - Batsman: Min 3 , Max 5
> - All Rounder (AR): Min 1 , Max 3
> - Bowler: Min 3, Max 5
> - Maximum 7 player from 1 team is allowed


How to input Players
-------------

You can refer to the team.txt file and write path here. f = open("/path/to/text/file.txt", "r")

**You can create your own text file just make sure the pattern of writing about players**

Here is the sample pattern

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

How to view the teams
-------------

All the teams are stored in "comb_list_3" list.

Total combinations for above team is: 179798

Sample Output
-------------

[['kock', 'mi', '9.5', 'wk'], ['kohli', 'rcb', '11.0', 'batsman'], ['r_sharma', 'mi', '10.5', 'batsman'], ['de_villiers', 'rcb', '10.0', 'batsman'], ['siraj', 'rcb', '8.5', 'bowl'], ['saini', 'mi', '8.0', 'bowl'], ['mcclenaghan', 'rcb', '8.5', 'bowl'], ['malinga', 'rcb', '8.5', 'bowl'], ['markande', 'rcb', '8.0', 'bowl'], ['h_pandya', 'mi', '9.5', 'ar'], ['shivam_dube', 'mi', '8.0', 'ar']]
