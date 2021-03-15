import random
"""71 to 14"""

print('...')

rps = ["rock", "paper", "scissors"]

u_i = input(": ")
c_i = random.choice(rps)

print(f"computer input: {c_i}")
print(f"your input: {u_i}")

if c_i == u_i:
    print('draw')
elif (u_i == 'rock' and c_i == 'scissors') or (u_i == 'paper' and c_i == 'rock') or \
    (u_i == 'scissors' and c_i == 'paper'):
    print('you win')
else:
    print('you lose')
