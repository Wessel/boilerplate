import os
import yaml
import re
import datetime

file_types = ['LICENSE', 'CODEOWNERS', '.md', '.yml']
script_name = os.path.basename(__file__)

def replace_placeholders(file_path, replacements):
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

    for placeholder, replacement in replacements.items():
      content = re.sub(re.escape(placeholder), replacement, content)

    with open(file_path, 'w', encoding='utf-8') as file:
      file.write(content)

def initialize_repository(directory, replacements):
  for root, _, files in os.walk(directory):
    for file in files:
      if file == script_name:
        continue
      if any(file.endswith(file_type) for file_type in file_types):
        file_path = os.path.join(root, file)
        replace_placeholders(file_path, replacements)

def parse_input(prompt):
  return [item.strip() for item in input(prompt).split(',')]

def parse_contact(prompt):
  contacts = []
  while True:
    print(prompt)
    name = input(f"\tName\t\t").strip()
    if not name:
      break
    url = input(f"\tURL\t\t").strip()
    about = input(f"\tAbout\t\t").strip()
    contacts.append({'name': name, 'url': url, 'about': about})
  return {'contact_links': contacts}

def parse_funding(prompt):
  funding = {}
  while True:
    print(prompt)
    key = input(f"\tKey\t\t").strip()
    if not key:
      break
    value = input(f"\tValue\t\t").strip()
    funding[key] = value

  return funding

def main():
  current_year = str(datetime.datetime.now().year)

  replacements = {
    "{{project.name}}": input("Project name\t\t"),
    "{{info.desc}}": input("Project Description\t"),
    "{{project.master}}": input("Master of the repo\t"),
    "{{project.license}}": f"{current_year} " + input('License holder\t\t'),

    "{{tree.parts}}": yaml.dump(parse_input("Parts of the repo\t"), default_flow_style=True),
    "{{project.lang}}": input("Language used\t\t"),
    "{{project.linter}}": input("Linter used\t\t"),

    "{{setup.prerequisites}}": input("Prerequisites\t\t"),
    "{{setup.install}}": input("Install command\t\t"),
    "{{setup.test}}": input("Test command\t\t"),

    "{{project.logo}}": input("Project logo URL\t"),
    "{{project.funding}}": yaml.dump(parse_funding("Funding methods\t\t"), default_flow_style=True),
    "{{project.contact}}": yaml.dump(parse_contact("Contact information\t"), default_flow_style=False),
    "{{project.reviewers}}": yaml.dump(parse_input("Auto-assign users (x,y)\t"), default_flow_style=True)
  }

  directory = input("Initialize directory\t") or '.'
  initialize_repository(directory, replacements)

  delete = input("Delete this script? (Y/n)\t") or "y"
  if delete.lower() == "y":
    os.remove(__file__)

if __name__ == "__main__":
  main()
