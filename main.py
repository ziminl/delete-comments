import re

def remove_comments_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

cleaned_lines = []
    inside_multiline_comment = False

    for line in lines:
        #starting with ''' or """
        if inside_multiline_comment:
            if "'''" in line or '"""' in line:
                inside_multiline_comment = False
            continue
        
        if "'''" in line or '"""' in line:
            inside_multiline_comment = True
            continue

        #starting with '#'
        cleaned_line = line.split('#')[0].strip()

        if cleaned_line:  #passover empty lines
            cleaned_lines.append(cleaned_line)
    
    with open(file_path, 'w') as file:
        file.write("\n".join(cleaned_lines))

remove_comments_from_file('1.py')
#remove_comments_from_file('<filename>')

