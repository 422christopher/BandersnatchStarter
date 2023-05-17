I trained 3 different models: a random forest classifier, 
a gradient boosting classifier, and a stochastic descent classifier. 
They achieved validation accuracy scores of 92.5%, 88.5%, and 23.5%, respectively. 
The random forest classifier was significantly higher than the other two models, 
so I pursued tuning the random forest model.

I help a few parameters constant such as n_jobs=-1 and random_state=42, 
but I wanted to vary the max_depth parameter because I saw in my notes 
that we toggled this parameter to see if the maximum depth of the tree 
influenced the model's accuracy. Naturally, we would assume that more 
depth would increase accuracy, but I wanted to make sure the model would 
not be slowed down, and at what point the depth would be sufficient. 
A depth of 50 levels was sufficient according to my testing.

Lastly, I tuned the number of n_estimators. I saw on the random forest 
documentation that the default n_estimators changed from 10 to 100, and 
I wanted to see if this change in trees has a significant impact, enough 
for the developers to change the default for all use cases. To my surprise, 
the n_estimators with 10 trees achieved a validation accuracy of 90% and 
the n_estimators with 100 trees achieved a validation accuracy of 92.5%. 
I suppose the jump from 10 to 100 was significant enough at creating a 
better default random forest model for all use cases.