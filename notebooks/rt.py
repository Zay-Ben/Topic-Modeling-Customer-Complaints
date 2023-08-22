def remove_tweets(df, condition, column = None, n = 5):
    
    if column is not None:
        print("Tweets to be removed:")
        print()
        for i in df[~condition][column][:n]:
            print(i)
            print()
    else:
        pass
    
    len_before = len(df)
    
    print("Before: {} tweets.".format(len_before))
    
    len_after = len(df[condition])
    
    print("{0} or {1}% of the tweets were removed.".format(len_before - len_after, round((len_before - len_after) / len_before * 100, 2)))
    
    print("After: {} tweets.".format(len_after))
    
    return df[condition].reset_index(drop = True)

def rt(before, after):
    
    print("{0} or {1}% of the tweets were removed.".format(before - after, round((before - after) / before * 100, 2)))