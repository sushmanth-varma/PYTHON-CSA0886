text='''Bt Brer. ...
Better is Better. ...
Better. ...'''
sentences=text.split("...")
count_b_sen=0
for sentence in sentences:
    if sentence.strip().startswith('B'):
        count_b_sen+=1
print(count_b_sen)
