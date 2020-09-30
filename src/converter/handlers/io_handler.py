def cvt(line):
    if(line[:5] == "show("):
        text = line[5:-2]
        return f"print({text})"
