#!/usr/bin/python3

'''
Use binary trees to perform basic maths  ops
Disclaimer: I have not implemented brackets, yet.
'''


class Expr:
	'''
	expressions
	'''
	pass


class Times(Expr):
	'''
	multiplication
	'''
	def __init__(self, l, r):
		''' __init__ method '''
		self.l = l
		self.r = r

	def __str__(self):
		''' __str__ method '''
		ret_val = f'{str(self.l)} * {str(self.r)}'
		return ret_val

	def evaluator(self, env):
		''' evaluator method '''
		return self.l.evaluator(env) * self.r.evaluator(env)


class Plus(Expr):
	'''
	Addition
	'''
	def __init__(self, l, r):
		''' __init__ method '''
		self.l = l
		self.r = r

	def __str__(self):
		''' __str__ method '''
		ret_val = f'{str(self.l)} + {str(self.r)}'
		return ret_val

	def evaluator(self, env):
		''' evaluator method '''
		return self.l.evaluator(env) + self.r.evaluator(env)


class Minus(Expr):
	'''
	Subtraction
	'''
	def __init__(self, l, r):
		''' __init__ method '''
		self.l = l
		self.r = r

	def __str__(self):
		''' __str__ method '''
		ret_val = f'{str(self.l)} - {str(self.r)}'
		return ret_val

	def evaluator(self, env):
		''' evaluator method '''
		return self.l.evaluator(env) - self.r.evaluator(env)


class Divide(Expr):
	'''
	Division
	'''
	def __init__(self, l, r):
		'''__init__ method'''
		self.l = l
		self.r = r

	def __str__(self):
		''' __str__ method '''
		ret_val = f'{str(self.l)} / {str(self.r)}'
		return ret_val

	def evaluator(self, env):
		''' evaluator method '''
		return self.l.evaluator(env) / self.r.evaluator(env)


class Const(Expr):
	'''
	algebraic known
	'''
	def __init__(self, val):
		''' __init__ method '''
		self.val = val

	def __str__(self):
		''' __str__ method '''
		return str(self.val)

	def evaluator(self, env):
		''' evaluator method '''
		return self.val


class Var(Expr):
	'''
	algebraic unknown
	'''
	def __init__(self, name):
		''' __init__ method '''
		self.name = name

	def __str__(self):
		''' __str__ method '''
		return self.name

	def evaluator(self, env):
		''' evaluator method '''
		return env[self.name]


if __name__ == '__main__':
	e1 = Times(Const(3), Plus(Var('y'), Var('x'))) # 3 * (y + x)
	e2 = Plus(Times(Const(3), Var('y')), Var('x')) # 3 * y + x

	env = {'x': 2, 'y': 4}

	print(f'The value of {e1} when x = {env["x"]} and y = {env["y"]} is {e1.evaluator(env)}')
	print(f'The value of {e2} when x = {env["x"]} and y = {env["y"]} is {e2.evaluator(env)}')
