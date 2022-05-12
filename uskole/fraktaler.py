#https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
import turtle


gren_lengde = 50
forkort_med = 5
vinkel = 30
start_vinkel = 90
farge = 'green'


def build_tree(t, branch_length, shorten_by, angle):
  MINIMUM_BRANCH_LENGTH = 5
  if branch_length > MINIMUM_BRANCH_LENGTH:
    t.forward(branch_length)
    new_length = branch_length - shorten_by
    t.left(angle)
    build_tree(t, new_length, shorten_by, angle)
    t.right(angle * 2)
    build_tree(t, new_length, shorten_by, angle)
    t.left(angle)
    t.backward(branch_length)

tree = turtle.Turtle()
tree.setheading(start_vinkel)
tree.color(farge)
build_tree(tree, gren_lengde, forkort_med, vinkel)
turtle.mainloop()
