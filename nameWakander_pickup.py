def write_pickup_file(nameWakander_file_path, pickup_file_path, pickup_word):
    nameWakander_file_path
    discovery = False
    with open(pickup_file_path, mode="W") as wf:
        with open(nameWakander_file_path) as f:
            s = f.readline()
            if s in pickup_word:
                discovery = True
            elif s[0] != " ":
                discovery = False
            if discovery:
                wf.write(s.split(",")[0])

