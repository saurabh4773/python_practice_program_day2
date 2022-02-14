# WAP to print escape character and its use

print("Escape Character\tUse\n\t"r'\n''\t\tNewline\n\t'
        r'\t''\t\tSpace/tab\n\t'r'\'''\t\tSingle Quote\n\t'
        r'\"''\t\tDouble Quote')

# OR

print("{} {}".format("Escape Character","\tUse"))
print("{} {}".format('\t'r"\n","\t\tNewline"))
print("{} {}".format('\t'r"\t","\t\tSpace/tab"))
print("{} {}".format('\t'r"\'","\t\tSingle Quote"))
print("{} {}".format('\t'r"\"","\t\tDouble Quote"))
