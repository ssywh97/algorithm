sentence = input()
check_list = ["U", "C", "P", "C"]
check = True

for i in range(len(check_list)):
  if check_list[i] in sentence:
    check = True
    index = sentence.find(check_list[i]) #sentence의 몇번에 check_list의 원소들이 위치해있는지 확인
    sentence = sentence[index + 1:]
  else:
    check = False
    break
if check == True:
  print("I love UCPC")
else:
  print("I hate UCPC")