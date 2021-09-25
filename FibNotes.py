notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

seq_start = int(input("What value should we start from? "))
seq_length = int(input("How long should the sequence be? "))

fib_seq =  [seq_start, seq_start]
note_list = []

for i in range(seq_length-2):
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

for i in fib_seq:
print(note_list)



'''
def fibonacci(start, length):
    fib_seq =  [seq_start, seq_start]
    for i in range(length-2):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


def note_gen(int_list):
    note_list = []
    for i in int_list:
        note_list.append(i % 12)
    return note_list


def note_conv(int_list):
    note_list = []
    for i in int_list:
        note_list.append(notes[i])
    return note_list


seq_start = int(input("What value should we start from? "))
seq_length = int(input("How long should the sequence be? "))

#Test
print(fibonacci(seq_start,seq_length))
print(note_gen(fibonacci(seq_start,seq_length)))
print(note_conv(note_gen(fibonacci(seq_start,seq_length))))
'''