def convert_date(epoch):
    import datetime
    epoch_time = epoch
    converted_time = datetime.datetime.fromtimestamp(epoch_time)
    print(converted_time)

user_input = int(input("Enter epoch time:"))
convert_date(user_input)