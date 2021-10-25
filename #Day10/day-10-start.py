#Functions with output

def format_name(f_name, l_name):
    case_1 = f_name.title()
    case_2 = l_name.title()
    return f"{case_1} {case_2}"

a = format_name("AVa", "KhaN")
print(a)