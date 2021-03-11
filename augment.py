##Determine whether the section is metro or rural
def rurality(data, RA, road_no, SLK = "SLK") :
    import numpy as np
    regionType = np.where((data[RA] == 7 & data[road_no].isin(['M045','H006','M026','M010']))| 
                    ((data[SLK].astype(int) >= 48.5) & data[road_no] == 'H005')|
    ((data[SLK].astype(int) >= 48.5) & data[road_no] == 'H005')|
    ((data[SLK].astype(int) >= 12.22) & data[road_no] == 'H052')|
    ((data[SLK].astype(int) >= 35.5) & data[road_no] == 'H001')|
    ((data[SLK].astype(int) >= 18.54) & data[road_no] == 'H009'), 'Rural', 'Metro')
    return regionType

##Assign a natural key based on key variables
def natural_key(data, SLK = None, ID_name = "NATURAL_KEY", true_SLK = None, key_vars = []):

    #Create a natural key based on SLK and ID variables
    new_data = data.copy()
    new_data.insert(0, ID_name, "")
    for var in key_vars +[SLK, true_SLK]:
        if var is not None:
            new_data[ID_name] += new_data[var].astype(str) + '-'

    return new_data

##Function that allows one to add columns to a dataset from one with a shared natural key.  
def concat_cols(left, right, key = "NATURAL_KEY", new_cols = []):
    new_cols.append(key)
    concat_data = left.copy().merge(right[new_cols], how = 'left', on = key, suffixes = ('','_right'))
    return concat_data

###Find points of equation and add the information to the dataset
# def pointOfEquation(data, SLK, locationVars)
# #Find the Points of Equations by searching for duplicate SLKs for the same location variables
