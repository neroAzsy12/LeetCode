import os

directories_to_access = [  # List of Directories that need to be accessed
  '../C++', 
  '../Go', 
  '../Java', 
  '../Python', 
  '../SQL'
]
language_map = {            # Mapping of respective language solution
  'py' : 'Python', 
  'cpp' : "C++", 
  'java' : 'Java', 
  'sql': 'SQL', 
  'go' : 'Go'
}
problems_solved = {}              # Key: Problem Id, Value: { name: Problem Name, code: [Language(s)] }
previous_data_map = None          # Key: Problem Id, Value: { difficulty: (Easy || Medium || hard), time: TC, space: SC, approach: subsection }

def getReadMeFileContent():
  file = open('../README.md', 'r')
  content_lines = file.read().splitlines()
  startIndex = 4 # 2
  result = {}

  for index in range(startIndex, len(content_lines)):
    currentLine = content_lines[index].split('|')
    
    result[int(currentLine[0])] = {
      'difficulty' : currentLine[2],
      'time' : currentLine[3],
      'space' : currentLine[4],
      'approach' : currentLine[6]
    }

  file.close()
  return result

# solved_map refers to problems_solved
# data_map refers to previous_data_map
def writeContentToFiles(solved_map, data_map):
  solution_link = 'https://github.com/neroAzsy12/LeetCode/blob/main/Go/1-Two-Sum.go'
  problem_link = 'https://leetcode.com/problems/two-sum/'

  readme_file = open('../README.md', 'w')
  readme_file.write('# LeetCode Solutions\n\n')
  readme_file.write('#|Title|Difficulty|Time|Space|Solution|Approach\n---|---|---|---|---|---|---\n')

  solution_file = open('../CodingSolutions.md', 'w')
  solution_file.write('#|Title|Difficulty|Time|Space|Solution|Approach\n---|---|---|---|---|---|---\n')

  for key in solved_map:
    id = str(key)

    title_tmp = problems_solved[key]['title'].replace(' ', '-').lower()
    title = '[' + solved_map[key]['title'] + '](https://leetcode.com/problems/' + title_tmp +')' #[Add Two Numbers](https://open.kattis.com/problems/addtwonumbers)<a name="Add Two Numbers"></a>

    difficulty = data_map[key]['difficulty'] if key in data_map else 'TBD'
    time = data_map[key]['time'] if key in data_map else 'TBD'
    space = data_map[key]['space'] if key in data_map else 'TBD'
    approach = data_map[key]['approach'] if key in data_map else 'TBD'

    solution_path = id + ' ' + solved_map[key]['title']
    solution_path = solution_path.replace(' ', '-')

    lang_readme = ''
    lang_solution = ''

    for index in range(len(solved_map[key]['code']) - 1):
      # https://github.com/neroAzsy12/LeetCode/blob/main/C%2B%2B/1-Two-Sum.cpp
      lang_readme += '[' + language_map[solved_map[key]['code'][index]] + '](https://github.com/neroAzsy12/LeetCode/blob/main/' + language_map[solved_map[key]['code'][index]] + '/' + solution_path + '.' + solved_map[key]['code'][index] + ')'
      lang_readme += ', '

      lang_solution += language_map[solved_map[key]['code'][index]]
      lang_solution += ','

    lang_readme += '[' + language_map[solved_map[key]['code'][-1]] + '](https://github.com/neroAzsy12/LeetCode/blob/main/' + language_map[solved_map[key]['code'][-1]] + '/' + title + '.' + solved_map[key]['code'][-1] + ')'
    lang_solution += language_map[solved_map[key]['code'][-1]]

    readme_file.write(id + '|' + title + '|' + difficulty + '|' + time + '|' + space + '|' + lang_readme + '|' + approach + '\n')
    solution_file.write(id + '|' + solved_map[key]['title'] + '|' + difficulty + '|' + time + '|' + space + '|' + lang_solution + '|' + approach + '\n')
  
  solution_file.close()
  readme_file.close()

# Prepare data based from directories that are being accessed
for directory in directories_to_access:
  file_contents = os.listdir(directory)

  for file in file_contents:
    separator = file.split('-')
    problemNum = int(separator[0])

    problemName = ''
    for i in range(1, len(separator) - 1):
      problemName += separator[i] + ' '
    
    separator_tmp = separator[-1].split('.')
    problemName = problemName + separator_tmp[0]


    if problemNum not in problems_solved:
      problems_solved[problemNum] = {
        'title' : problemName,
        'code' : [separator_tmp[-1]]
      }
    else:
      problems_solved[problemNum]['code'].append(separator_tmp[-1])

problems_solved = dict(sorted(problems_solved.items())) # sort dict by key

# we could open the readme file to save the difficult rating before rewriting to avoid retyping
previous_data_map = getReadMeFileContent()

print(previous_data_map)


writeContentToFiles(problems_solved, previous_data_map)