pool_volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

pipe_1_work = pipe_1 * hours
pipe_2_work = pipe_2 * hours

overall_work = pipe_1_work + pipe_2_work

percent_full = overall_work / pool_volume * 100
percent_pipe_1 = pipe_1_work / overall_work * 100
percent_pipe_2 = pipe_2_work / overall_work * 100

if overall_work <= pool_volume:
    print(f'The pool is {percent_full:.2f}% full. Pipe 1: {percent_pipe_1:.2f}%. Pipe 2: {percent_pipe_2:.2f}%.')

else:
    diff = overall_work - pool_volume
    print(f'For {hours} hours the pool overflows with {diff:.2f} liters.')
