def split_and_join(line):
    # Split the text when " "

    text = line.split(" ")

    # Joint the text with "-"
    text = "-".join(text)

    return text

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)