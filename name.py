def name_length(name):
    return len(name)
def upper_case(name):
    return name.upper()
def lower_case(name):
    return name.lower()

if __name__=="__main__":
    name = "Nina"
    length = name_length(name)
    upper_case_letter = upper_case(name)
    print(f" the length is:{length} and the uppercase version is:{upper_case_letter}")