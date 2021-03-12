

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

#remove outliers beyond 1 standard deviation
def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key, subdf in df.groupby('location'):
        #mean
        m = np.mean(subdf['price_per_sqft'])
        #standard div of price per sq ft
        st = np.std(subdf['price_per_sqft'])
        #keep data points that are above -1 std and below 1 std
        reduced_df = subdf[(subdf.price_per_sqft>(m-st)) & (subdf.price_per_sqft <= (m+st))]
        df_out = pd.concat([df_out, reduced_df], ignore_index =True)
    return df_out

def plot_scatter_chart(df,location):
    '''This method creates a scatterplot of 2 and 3 bedrooms in a location, and their total area and price per square foot in IND Rupees'''
    #creates two different dataframes: one for 2 bedrooms and 3 bedrooms
    bhk2 = df[(df.location == location) & (df.bhk ==2)]
    bhk3 = df[(df.location == location) & (df.bhk ==3)]
    matplotlib.rcParams['figure.figsize'] = (15,10)
    #create scatterplot
    plt.scatter(bhk2.total_sqft, bhk2.price_per_sqft, color = 'blue', label='2 BHK', s = 50)
    plt.scatter(bhk3.total_sqft, bhk3.price_per_sqft, marker = '+', color = 'green', label='3 BHK', s=50)
    plt.xlabel('Total Square Feet Area')
    plt.ylabel('Price Per Square Feet')
    plt.title(location)
    plt.legend()

