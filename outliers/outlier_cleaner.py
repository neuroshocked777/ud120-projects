#!/usr/bin/python

'''
def outlierCleaner(predictions, ages_train, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = list( (net_worths - predictions)**2 )

    cleaned_data = zip(ages, net_worths, error)
    cleaned_data = sorted(cleaned_data, key = lambda tup: tup[2])
    cleaned_data = cleaned_data[:80]
    
    return cleaned_data
'''    

def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)
        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    temp_data = []

    ### your code goes here
    numPredictions = len(predictions)

    for i in range(numPredictions):
        resError = abs(predictions[i] - net_worths[i])
        tempTuple = (ages[i], net_worths[i], resError)
        temp_data.append(tempTuple)

    temp_data.sort(key=lambda tup: tup[2])
    cleaned_data = temp_data[0:int(len(temp_data)*0.9)]

    return cleaned_data
