#!user/bin/python3

'''
towers of hanoi; nothing special
'''

def move(fro, to):
	''' move disk from `fro` to `to` '''
	print(f'move disk from peg {fro} to peg {to}')

def move_via(fro, via, to):
	''' move disk from `fro` to `to` via `via` '''
	move(fro, via)
	move(via, to)

def hanoi(num, fro, hlp, to):
	'''
	num: number of disks
	fro: `from` position
	hlp: `helper` aka temp position
	to: `to` aka target position
	Position is the pole/peg that the disks are stacked through
	'''
	if num == 0:
		pass
	else:
		hanoi(num - 1, fro, to, hlp)
		move(fro, to)
		hanoi(num - 1, hlp, fro, to)

if __name__ == '__main__':
	print(f'Solution for Towers of Hanoi: 7 disks, 3 pegs')
	hanoi(7,'A','B','C')
