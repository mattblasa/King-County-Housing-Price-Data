

#determine interquartile range 
'''
Q1 = df.quantile(0.001)
Q3 = df.quantile(0.999)
IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
'''

#check if values in a column are a float 
def is_float(x):
    try:
        float(x)
    except:
        return False 
    return True

#convert a range string into numbers. Format: 1112 - 2222
def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None 