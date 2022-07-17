class BoardWrapper():
    def __init__(self, size, tiles):
        self.size = size
        self.tiles = tiles
        self.tile_distance = 182
        self.distance_to_move = 0

    def move(self, number_of_moves):
        self.distance_to_move = 182 * number_of_moves