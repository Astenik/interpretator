'''this project python makes interpretator for my new language. My language contain only variables, print and if-else structures.'''
my_language = open('my_language.txt', 'r')
lines = my_language.readlines()
my_dict = {}
# collect all variables in dictionary
for line in lines:
        if 'var' in line:
              i = line.find('r')
              variable_name = ''
              k = line.find('=')
              for j in range(i + 1, k):
                     if line[j] != ' ':
                           variable_name += line[j]
              variable_value = ''
              for ii in range(k + 1, len(line)):
                    if (line[ii] != ' ') and (line[ii] != ';') and (line[ii] != '/n'):
                          variable_value += line[ii]
              my_dict[variable_name] = variable_value
      # read all lines and done
def foo(num):
     ind = num.find('t')
     li = num[ind + 1:]
     if  (not '"' in li) and (not "'" in li): 
          output1 = ''
          ii = 0
          while li[ii] != ';':
             if (li[ii] != ' ') and (li[ii] != ';'):
                    output1 += li[ii]
             ii += 1
          for key in my_dict.keys():
                 if key == output1:
                        print(my_dict[key])
                        break 
          else:
                raise Exception('you dont have such variable')
     else:
             print(li)
line = 0
while line < len(lines):
     if 'whether_true' in lines[line]:
         ind = lines[line].find('ue')
         ind2 = lines[line].find(':')
         lin = lines[line][ind + 2:ind2]
         if '==' in lin:
             ind1 = lin.find('==')
             name1 = ''
             for kk in range(ind1):
                 if lin[kk] != ' ':
                     name1 += lin[kk]
             name2 = ''
             for gg in range(ind1 + 2, len(lin)):
                 if (lin[gg] != ' ') and (lin[gg] != '/n'):
                     name2 += lin[gg]
             line += 1
             if my_dict[name1] == my_dict[name2]:
                while lines[line][0] == ' ':
                  if 'out' in lines[line]: 
                    foo(lines[line])
                  line += 1 
             if 'otherwise' in lines[line]: 
                line += 1
                if not my_dict[name1] == my_dict[name2]:
                      while lines[line][0] == ' ':
                         if 'out' in lines[line]: 
                             foo(lines[line])
                         line += 1     
         if '>' in lin:
             ind1 = lin.find('>')
             name1 = ''
             for kk in range(ind1):
                 if lin[kk] != ' ':
                     name1 += lin[kk]
             name2 = ''
             for gg in range(ind1 + 1, len(lin)):
                 if (lin[gg] != ' ') and (lin[gg] != '/n'):
                     name2 += lin[gg]
             line += 1
             if my_dict[name1] > my_dict[name2]:
                while lines[line][0] == ' ':
                 if 'out' in lines[line]: 
                    foo(lines[line])
                 line += 1 
             if 'otherwise' in lines[line]: 
                line += 1
                if not my_dict[name1] > my_dict[name2]:
                      while lines[line][0] == ' ':
                         if 'out' in lines[line]: 
                            foo(lines[line])
                         line += 1     
         if '<' in lin:
             ind1 = lin.find('<')
             name1 = ''
             for kk in range(ind1):
                 if lin[kk] != ' ':
                     name1 += lin[kk]
             name2 = ''
             for gg in range(ind1 + 1, len(lin)):
                 if (lin[gg] != ' ') and (lin[gg] != '/n'):
                     name2 += lin[gg]
             line += 1
             if my_dict[name1] < my_dict[name2]:
                while lines[line][0] == ' ':
                 if 'out' in lines[line]: 
                     foo(lines[line])
                 line += 1 
             if 'otherwise' in lines[line]: 
                line += 1
                if not my_dict[name1] < my_dict[name2]:
                      while lines[line][0] == ' ':
                         if 'out' in lines[line]: 
                            foo(lines[line])
                         line += 1     
         if '!=' in lin:
             ind1 = lin.find('!=')
             name1 = ''
             for kk in range(ind1):
                 if lin[kk] != ' ':
                     name1 += lin[kk]
             name2 = ''
             for gg in range(ind1 + 2, len(lin)):
                 if (lin[gg] != ' ') and (lin[gg] != '/n'):
                     name2 += lin[gg]
             line += 1
             if my_dict[name1] != my_dict[name2]:
                while lines[line][0] == ' ':
                 if 'out' in lines[line]: 
                   foo(lines[line])
                 line += 1 
             if 'otherwise' in lines[line]: 
                line += 1
                if not my_dict[name1] != my_dict[name2]:
                      while lines[line][0] == ' ':
                         if 'out' in lines[line]: 
                            foo(lines[line])
                         line += 1     
         if '<=' in lin:
             ind1 = lin.find('<=')
             name1 = ''
             for kk in range(ind1):
                 if lin[kk] != ' ':
                     name1 += lin[kk]
             name2 = ''
             for gg in range(ind1 + 2, len(lin)):
                 if (lin[gg] != ' ') and (lin[gg] != '/n'):
                     name2 += lin[gg]
             line += 1
             if my_dict[name1] <= my_dict[name2]:
                while lines[line][0] == ' ':
                 if 'out' in lines[line]: 
                   foo(lines[line])
                 line += 1 
             if 'otherwise' in lines[line]: 
                line += 1
                if not my_dict[name1] <= my_dict[name2]:
                      while lines[line][0] == ' ':
                         if 'out' in lines[line]: 
                            foo(lines[line])
                         line += 1     
         if '>=' in lin:
             ind1 = lin.find('>=')
             name1 = ''
             for kk in range(ind1):
                 if lin[kk] != ' ':
                     name1 += lin[kk]
             name2 = ''
             for gg in range(ind1 + 2, len(lin)):
                 if (lin[gg] != ' ') and (lin[gg] != '/n'):
                     name2 += lin[gg]
             line += 1
             if my_dict[name1] >= my_dict[name2]:
                while lines[line][0] == ' ':
                 if 'out' in lines[line]: 
                   foo(lines[line])
                 line += 1 
             if 'otherwise' in lines[line]: 
                line += 1
                if not my_dict[name1] >= my_dict[name2]:
                      while lines[line][0] == ' ':
                         if 'out' in lines[line]: 
                            foo(lines[line])
                         line += 1     
     elif 'out' in lines[line]: 
          foo(lines[line])
     line += 1 
