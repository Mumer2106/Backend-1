def convert_seconds(sec):
    hours= sec // 3600
    minutes= (sec - hours * 3600)// 60
    remaining_seconds= sec - hours * 3600 - minutes * 60
    return hours, minutes, sec

result = convert_seconds(5000)
print(result)