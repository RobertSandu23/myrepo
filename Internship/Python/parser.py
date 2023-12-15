start_timestamp = '17:56:07.996'
end_timestamp = '17:56:08.357'
log = 'logcat_applications.txt'

def word_parser(filename, start_timestamp, end_timestamp):
    last_words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                timestamp = line[6:18]  # take timestamp

                if start_timestamp <= timestamp <= end_timestamp:
                    words = line.split() # make a list of words

                    if words:
                        last_word = words[-1] # take las word from the list 
                        last_words.append(last_word.strip()) # append with removing blank spaces before and after the word

        return last_words
    
    except FileNotFoundError:
        print(f"Couldn't find this file: {log}")         

result = word_parser(log, start_timestamp, end_timestamp)
print(result)