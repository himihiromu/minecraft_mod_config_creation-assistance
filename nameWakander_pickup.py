def word_pickup(target_string_list, pickup_word, exclusion_word=""):
    discovery = False
    ans_list = ""
    for s in target_string_list:
        if pickup_word in s and not(exclusion_word in s):
            discovery = True
        elif s[0] != " ":
            discovery = False
        if discovery:
            ans_list.append(s)
    return ans_list

def _file_line_pickup(file_path, pickup_word, exclusion_word=""):
    discovery = False
    for s in target_string_list:
        if pickup_word in s and not(exclusion_word in s):
            discovery = True
        elif s[0] != " ":
            discovery = False
        if discovery:
            yield s.rstlip("\n")
    return None

def write_pickup_file(nameWakander_file_path, pickup_file_path, pickup_word, exclusion_word=""):
    discovery = False
    with open(pickup_file_path, mode="W") as wf:
        for s in _file_line_pickup(nameWakander_file_path, pickup_file_path, pickup_word, exclusion_word):
            wf.write(s)
    

def cutall_block_pickup_file(nameWakander_file_path, pickup_file_path):
    write_pickup_file(nameWakander_file_path, pickup_file_path, "log"):