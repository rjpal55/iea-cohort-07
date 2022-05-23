
def test_gol_init_blank_grid():
    grid = [
       [False,False],
       [False,False],]

    game = Life(grid)
    assert game.grid == grid

