abbr_list = {'co': 'company', 
                   'ltd': 'limited',
                   'pvt': 'private'}

stop_words = set(stopwords.words('english')) - set(['i', 'a', 's', 't', 'd', 'm', 'o', 'y'])

def get_value_from_abbr_list(key):
    if key in abbr_list.keys():
        return abbr_list[key]
    else:
        return "na"
        
def remove_stop_words(name):
    name = name.lower()
    name = name.split()
    name = [word for word in name if not word in stop_words]
    return ' '.join(name)
    
 def remove_special_chars(name):
    name = name.lower()
    # remove special characters
    name = re.sub('[^a-z0-9 ]+', ' ', name)
    # remove multiple spaces
    name = re.sub(' +', ' ', name)
    return name
    
 def replace_abbriviations(name):
    name = name.lower()
    name = name.split()
    replaced_name = ''
    
    for word in name:
        value = get_value_from_abbr_expn_list(word)
        if value != 'na':
            if value not in replaced_name:
                replaced_name = replaced_name + ' ' + value
        else:
            if word not in replaced_name:
                replaced_name = replaced_name + ' ' + word
    replaced_name = re.sub(' +', ' ', replaced_name)
    
    # remove repeated words which might happen after replacing abbriviations
    replaced_name = re.sub(r'\b(\w+)( \1\b)+', r'\1', replaced_name)
    return replaced_name
  
#sort words in the name to handle out of order names
def sort_words(name):
    name = name.split(" ")
    name.sort()
    name = " ".join(name)
    return name
    
 def process(name):
    name = name.lower()
    name = remove_stop_words(name)
    name = remove_special_chars(name)
    name = replace_abbriviations(name)
    name = sort_words(name)
    name = name.strip()
    return name
