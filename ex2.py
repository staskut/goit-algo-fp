import turtle


def draw_pifagor_tree(turtle_obj, branch_length_px, recursion_depth):
    """
    Рекурсивна функція для малювання дерева Піфагора за допомогою turtle graphics.
    Args:
        turtle_obj (turtle.Turtle): Об'єкт turtle для малювання.
        branch_length_px (int): Довжина гілок дерева в пікселях.
        recursion_depth (int): Кількість рівнів або глибина рекурсії для дерева.
    Returns:
        None
    """
    if recursion_depth == 0:
        return
    turtle_obj.forward(branch_length_px)
    turtle_obj.left(45)
    draw_pifagor_tree(turtle_obj, int(0.6 * branch_length_px), recursion_depth - 1)
    turtle_obj.right(90)
    draw_pifagor_tree(turtle_obj, int(0.6 * branch_length_px), recursion_depth - 1)
    turtle_obj.left(45)
    turtle_obj.backward(branch_length_px)


def main():
    recursion_depth = int(input(f"Введіть рівень рекурсії (1-10): "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    turtle_obj = turtle.Turtle()
    turtle_obj.speed(5)
    turtle_obj.color("red")
    turtle_obj.left(90)
    turtle_obj.up()
    turtle_obj.backward(200)
    turtle_obj.down()

    draw_pifagor_tree(turtle_obj, 100, recursion_depth)

    screen.exitonclick()


if __name__ == "__main__":
    main()
