def cvt(line):
    if(line[:5] == "show("):
        text = line[5:-2]
        return f"print({text})"
    if(line[:5] == "read("):
        inside_brackets = line[5:-2]
        var = inside_brackets.split(',')[0]
        dtype = inside_brackets.split(',')[1]
        return f"{var} = {dtype}(input())"
