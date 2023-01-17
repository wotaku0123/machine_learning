class Student:
  def __init__(self, name):
    self.name = name

  def calculate_avg(self, data):
    sum = 0

    for num in data:
      sum += num

    avg = sum / len(data)
    return avg

  def judge(self, avg):
      if(avg >= 60):
        result="passed"
      else:
        result="failed"
      return result

a001 = Student("sato")
data = [70, 65, 50, 10, 30]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(avg)
print(a001.name+" " + result)