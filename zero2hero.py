from chatgpt_wrapper import ChatGPT
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
import re
import sys


def extract_equations(input_string):
    eq_pattern = r'\\begin\{equation\}(.+?)\\end\{equation\}'
    matches = re.findall(eq_pattern, input_string, re.DOTALL)
    eqs = []
    for match in matches:
        match = re.sub(r'^\\label\{.*\}', '', match)
        match = re.sub(r'\\label\{.*\}$', '', match)
        eqs.append(match.strip())
    return eqs

def remove_dollars(input_string):
    output_string = input_string.replace('$', '').replace('$$', '')
    return output_string

def replace_string(input_string, search_string, replacement_string):
    output_string = input_string.replace(search_string, replacement_string)
    return output_string

def write_text_file(file_path, file_content):
    with open(file_path, 'w') as f:
        f.write(file_content)

def main(tex_file):
    cprint(figlet_format('zero2hero', font='standard'),
       'yellow', 'on_red', attrs=['bold'])
    gpt = ChatGPT()
    tex_doc = open(tex_file + '.tex', 'r').read()
    print('Extracting simple equations from ' + str(tex_file) + '.tex.')
    eqs = extract_equations(tex_doc)
    num_eqs = len(eqs)
    print('Found ' + str(num_eqs) + ' equation(s). Let\'s make it complex!')
    for id, eq in enumerate(eqs):
        eq_cpx = gpt.ask('make this equation look extremly complicated: ' + 
                         eq + '. provide only plain latex code without any explanation.')
        eq_cpx = remove_dollars(eq_cpx)
        tex_doc = replace_string(tex_doc, eq, eq_cpx)
        print('Processed equation ' + str(id + 1) + '/' + str(num_eqs) + '.')
    print('Saving new latex document.')
    write_text_file(tex_file + '_complicate.tex', tex_doc)
    print('Thank you for using\n')
    cprint(figlet_format('zero2hero', font='standard'),
       'yellow', 'on_red', attrs=['bold'])

if __name__ == "__main__":
    init(strip = not sys.stdout.isatty())
    main(sys.argv[1])