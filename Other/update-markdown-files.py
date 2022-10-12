import os

directories_to_access = [         # List of Directories that need to be accessed
  '../C++', 
  '../Go', 
  '../Java', 
  '../Python', 
  '../SQL'
]
extension_map = {                 # Mapping of respective file extensions
  'Python': 'py', 
  'C++': 'cpp', 
  'Java': 'java', 
  'SQL': 'sql', 
  'Go': 'go'
}
language_map = {                  # Mapping of respective language solution
  'py' : 'Python', 
  'cpp' : "C++", 
  'java' : 'Java', 
  'sql': 'SQL', 
  'go' : 'Go'
}
problem_data_map = None           # Key: Problem Id, Value: { name, difficulty: (Easy || Medium || hard), time: TC, solutions: [], space: SC, approach: subsection }

def getCodingSolutionsContent():
  """
  Opens the Coding Solutions file, and obtains the following info for each problem:\n
   {\n
    approach: ex) Two Pointer, Math\n 
    difficulty: (Easy, Medium, Hard),\n
    name: ex) Two Sum,\n
    solutions: [],\n
    space: Space Complexity,\n 
    time: Time Complexity\n 
  }\n
  """
  
  file = open('../CodingSolutions.md', 'r')
  content_lines = file.read().splitlines()
  startIndex = 2
  result = {}

  for index in range(startIndex, len(content_lines)):
    currentLine = content_lines[index].split('|')
    
    result[int(currentLine[0])] = {
      'name' : currentLine[1],                # name of the problem
      'difficulty' : currentLine[2],          # should only be (Easy, Medium or Hard)
      'time' : currentLine[3],                # ex) O(n)
      'space' : currentLine[4],               # ex) O(1)
      'solutions' : currentLine[5].split(','),# ex) [C++, Go, Java, JavaScript, Python]
      'approach' : currentLine[6]             # ex) Hashing or LinkedList or Math
    }

  file.close()
  return result

def getDataFromDirectories(directories, data_map, file_extension_map):
  """
  directories: problem_data_map\n
  data_map: problem_data_map\n
  file_extension_map: language_map\n
  """

  for directory in directories:
    files = os.listdir(directory)

    for file in files:
      separator = file.split('-')
      problemId = int(separator[0])

      problemName = ''
      file_extension = ''

      for i in range(1, len(separator)):

        if i != len(separator) - 1:
          problemName += separator[i] + ' '
        else:
          separator_tmp = separator[-1].split('.')
          problemName += separator_tmp[0]
          file_extension = separator_tmp[1]

      file_extension = file_extension_map[file_extension]

      if problemId not in data_map:
        data_map[problemId] = {
          'name' : problemName,
          'difficulty' : 'TBD',
          'time' : 'TBD',
          'space' : 'TBD',
          'solutions' : [file_extension],
          'approach' : 'TBD'
        }
      elif problemId in data_map and file_extension not in data_map[problemId]['solutions']:
        data_map[problemId]['solutions'].append(file_extension)
        data_map[problemId]['solutions'].sort()

def writeContentToFiles(data_map, lang_map):
  """
  data_map: sorted_problem_data_map\n
  lang_map: extension_map\n
  """
  
  readme_file = open('../README.md', 'w')
  readme_file.write('# LeetCode Solutions\n\n#|Title|Difficulty|Time|Space|Solution|Approach\n---|---|---|---|---|---|---\n')

  solution_file = open('../CodingSolutions.md', 'w')
  solution_file.write('#|Title|Difficulty|Time|Space|Solution|Approach\n---|---|---|---|---|---|---\n')
  
  for key in data_map:
    problemId = str(key)

    problemNameReadMe = "[{name}]({link}/{link_id})".format(
      name = data_map[key]['name'],
      link = 'https://leetcode.com/problems',
      link_id = data_map[key]['name'].replace(' ', '-').lower()
    )

    difficulty = data_map[key]['difficulty']
    time = data_map[key]['time']
    space = data_map[key]['space']
    approach = data_map[key]['approach']

    solution_path = '{id}-{name}'.format(
      id = problemId, 
      name = data_map[key]['name'].replace(' ', '-')
    )

    readme_solutions = ''
    solution_solutions = ''

    for index in range(len(data_map[key]['solutions'])):
      current_lang_solution = '[{lang}]({link}/{dir}/{file_name}.{extension})'.format(
        lang = data_map[key]['solutions'][index],
        link = 'https://github.com/neroAzsy12/LeetCode/blob/main',
        dir = data_map[key]['solutions'][index],
        file_name = solution_path,
        extension = lang_map[data_map[key]['solutions'][index]]
      )

      readme_solutions += current_lang_solution
      solution_solutions += data_map[key]['solutions'][index]

      if index != len(data_map[key]['solutions']) - 1:
        readme_solutions += ','
        solution_solutions += ','
    
    readme_file.write(problemId + '|' + problemNameReadMe + '|' + difficulty + '|' + time + '|' + space + '|' + readme_solutions + '|' + approach + '\n')
    solution_file.write(problemId + '|' + data_map[key]['name'] + '|' + difficulty + '|' + time + '|' + space + '|' + solution_solutions + '|' + approach + '\n')

  solution_file.close()
  readme_file.close()

# First collect data from CodingSolutions.md, and directories
problem_data_map = getCodingSolutionsContent()
getDataFromDirectories(directories_to_access, problem_data_map, language_map)

# update both README and CodingSolutions.md
sorted_problem_data_map = dict(sorted(problem_data_map.items()))
writeContentToFiles(sorted_problem_data_map, extension_map)