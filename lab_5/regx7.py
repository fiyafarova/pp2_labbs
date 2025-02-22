import re

def replace_match(match):
    return match.group(1).upper()

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', replace_match, snake_str)

snake_string = "hello_world_this_is_python"
camel_case_string = snake_to_camel(snake_string)

print(camel_case_string)
