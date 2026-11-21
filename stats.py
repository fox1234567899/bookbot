import sys

def get_words_count(get_book_text):
    
    words = get_book_text(sys.argv[1]).split()
    num_words=len(words)
    the_thing=f"Found {num_words} total words"
    print(the_thing)
    






def count_character(get_book_text):
    new_data={}
    
    words=get_book_text(sys.argv[1]).lower()
    for m in words:
        for n in m:
            if n in new_data:
                new_data[n] +=1
            else:
                new_data[n] =1
    return new_data
        

def sort_on(vehicle:tuple[str,int])->int:
    return vehicle[1]


def chars_dict_to_sorted_list(the_count:dict[str,int])->list[tuple[str,int]]:
    new_list=[]
    
    for m in the_count:
        new_list.append(tuple([m,the_count[m]]))
        sorted_the_list=sorted(new_list,reverse=True,key=sort_on)
    return sorted_the_list

