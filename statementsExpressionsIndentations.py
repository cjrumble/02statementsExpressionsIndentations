# Using Arithmetic expressions
print((10 + 2) * 100 / 5 - 200)
# Output: 40.0
# Using functions in an expression
print(pow(2, 10))
# Output: 1024
# # Using eval in an expression
# >> > eval("2.5+2.5")
# 5.0
# Back
# to
# top
#
# Simple
# Assignment
# Statement
#
# In
# a
# simple
# assignment, we
# create
# new
# variables, assign and change
# values.This
# statement
# provides
# an
# expression and a
# variable
# name as a
# label
# to
# preserve
# the
# value
# of
# the
# expression.
#
# # Syntax
# variable = expression
# # LHS <=> RHS
# Let’s
# now
# take
# a
# close
# look
# at
# three
# types
# of
# assignment
# statements in Python and see
# what’s
# going
# on
# under
# the
# hood.
#
# Case - 1: Right - hand
# side(RHS) is just
# a
# value - based
# expression.
#
# Let’s
# consider
# the
# most
# basic
# form
# of
# assignment in Python.
#
# >> > test = "Learn Python"
# Python
# will
# create
# a
# string “Learn
# Python” in memory and assigns
# the
# name “test” to
# it.You
# can
# confirm
# the
# memory
# address
# with the of a built- in function known as id().
#
# >> > test = "Learn Python"
# >> > id(test)
# 6589040
# The
# number is the
# address
# of
# the
# location
# where
# the
# data
# lives in memory.Now, here
# comes
# a
# few
# interesting
# points
# which
# you
# should
# know.
#
# 1.
# If
# you
# create
# another
# string
# with the same value, Python will create a new object and assign it to a different location in memory.So this rule would apply to most of the cases.
#
# >> > test1 = "Learn Python"
# >> > id(test1)
# 6589104
# >> > test2 = "Learn Python"
# >> > id(test2)
# 6589488
# 2.
# However, Python
# will
# also
# allocate
# the
# same
# memory
# address in the
# following
# two
# scenarios.
#
# The
# strings
# don’t
# have
# whitespaces and contain
# less
# than
# 20
# characters.
# In
# case
# of
# Integers
# ranging
# between - 5
# to + 255.
# This
# concept is known as Interning.Python
# does
# it
# to
# save
# memory.
#
# Back
# to
# top
#
# Case - 2: Right - hand
# side(RHS) is a
# current
# Python
# variable.
#
# Let’s
# take
# up
# the
# next
# type
# of
# assignment
# statement
# where
# the
# RHS is a
# current
# Python
# variable.
#
# >> > another_test = test
# The
# above
# statement
# won’t
# trigger
# any
# new
# allocation in memory.Both
# the
# variables
# would
# point
# to
# the
# same
# memory
# address.It’s
# like
# creating
# an
# alias
# to
# the
# existing
# object.Let’s
# validate
# this
# by
# using
# the
# id()
# function.
#
# >> > test = "Learn Python"
# >> > id(test)
# 6589424
# >> > another_test = test
# >> > id(another_test)
# 6589424
# Case - 3: Right - hand
# side(RHS) is an
# operation.
#
# In
# this
# type
# of
# statement, the
# result
# would
# depend
# on
# the
# outcome
# of
# the
# operation.Let’s
# analyze
# it
# with the following examples.
#
# >> > test = 2 * 5 / 10
# >> > print(test)
# 1.0
# >> > type(test)
# <
#
# class 'float'>
#
#
# In
# the
# above
# example, the
# assignment
# would
# lead
# to
# the
# creation
# of
# a “float” variable.
#
# >> > test = 2 * 5
# >> > print(test)
# 10
# >> > type(test)
# <
#
# class 'int'>
#
#
# In
# this
# example, the
# assignment
# would
# lead
# to
# the
# creation
# of
# an “int” variable.
#
# Back
# to
# top
#
# Augmented
# Assignment
# Statement
#
# You
# can
# combine
# arithmetic
# operators in assignments
# to
# form
# an
# augmented
# assignment
# statement.
#
# Check
# out
# the
# below
# examples
# for augmented assignment statement.
#
# x += y
# The
# above
# statement is a
# shorthand
# for the below simple statement.
#
# x = x + y
# Next
# one is a
# bit
# clearer
# example
# where
# we
# are
# appending
# new
# elements
# to
# the
# tuple.
#
# >> > my_tuple = (10, 20, 30)
# >> > my_tuple += (40, 50,)
# >> > print(my_tuple)
# (10, 20, 30, 40, 50)
# Next
# example is using
# a
# list
# of
# vowels.It is demonstrating
# the
# addition
# of
# missing
# vowels
# to
# the
# list.
#
# >> > list_vowels = ['a', 'e', 'i']
# >> > list_vowels += ['o', 'u', ]
# >> > print(list_vowels)
# ['a', 'e', 'i', 'o', 'u']
# Back
# to
# top
#
# Multi - line
# Statement in Python
#
# Usually, every
# Python
# statement
# ends
# with a newline character.However, we can extend it over to multiple lines using the line continuation character (\).
#
# And
# Python
# gives
# us
# two
# ways
# to
# enable
# multi - line
# statements in a
# program.
#
# Explicit
# line
# continuation
#
# When
# you
# right
# away
# use
# the
# line
# continuation
# character(\) to
# split
# a
# statement
# into
# multiple
# lines.
#
# Example
#
# # Initializing a list using the multi-line statement
# >> > my_list = [1, \
#                 ... 2, 3 \
#                     ..., 4, 5 \
#                     ...]
# >> > print(my_list)
# [1, 2, 3, 4, 5]
# # Evalulate an expression using a multi-line statement
# >> > eval( \
#     ...
# " 2.5 \
# ... + \
# ... 3.5")
# 6.0
# Back
# to
# top
#
# Implicit
# line
# continuation
#
# Implicit
# line
# continuation is when
# you
# split
# a
# statement
# using
# either
# of
# parentheses(), brackets[] and braces
# {}.You
# need
# to
# enclose
# the
# target
# statement
# using
# the
# mentioned
# construct.
#
# Example
#
# >> > result = (10 + 100
#                ... * 5 - 5
#                ... / 100 + 10
#                ...)
# >> > print(result)
# 519.95
# Another
# Example
#
# >> > subjects = [
#     ... 'Maths',
#     ... 'English',
#     ... 'Science'
#         ...]
# >> > print(subjects)
# ['Maths', 'English', 'Science']
# >> > type(subjects)
# <
#
# class 'list'>
#
#
# Back
# to
# top
#
# Python
# Indentation
#
# Many
# of
# the
# high - level
# programming
# languages
# like
# C, C + +, C  # use braces { } to mark a block of code. Python does it via indentation.
#
# A
# code
# block
# which
# represents
# the
# body
# of
# a
# function or a
# loop
# begins
# with the indentation and ends with the first unindented line.
#
# How
# many
# spaces is an
# indent in Python?
#
# Python
# style
# guidelines(PEP
# 8) states
# that
# you
# should
# keep
# indent
# size
# of
# four.However, Google
# has
# its
# unique
# style
# guideline
# which
# limits
# indenting
# up
# to
# two
# spaces.So
# you
# too
# can
# choose
# a
# different
# style, but
# we
# recommend
# to
# follow
# the
# PEP8.
#
# Why is indentation
# so
# crucial in Python?
#
# Most
# of
# the
# programming
# languages
# provide
# indentation
# for better code formatting and don’t enforce to have it.
#
# However, in Python, it is mandatory
# to
# obey
# the
# indentation
# rules.Typically, we
# indent
# each
# line
# by
# four
# spaces( or by
# the
# same
# amount) in a
# block
# of
# code.
#
# In
# the
# examples
# of
# the
# previous
# sections, you
# might
# have
# seen
# us
# writing
# simple
# expression
# statements
# which
# didn’t
# have
# the
# indentation.
#
# However,
# for creating compound statements, the indentation will be utmost necessary.
#
# Example
#
#
# def demo_routine(num):
#     print('I am a demo function')
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# num = int(input('Enter a number:'))
# if demo_routine(num) is True:
#     print(num, 'is an even number')
# else:
#     print(num, 'is an odd number')
# Now, also
# see
# a
# scenario
# when
# undesired
# indentation
# causes
# an
# error.So
# let’s
# try indenting a simple expression statement.
#
# >> > 6 * 5 - 10
# File
# "<stdin>", line
# 1
# 6 * 5 - 10
# ^
# IndentationError: unexpected
# indent