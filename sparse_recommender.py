class SparseMatrix:

    def __init__(self, rows, cols):
        # Initialize the sparse matrix using dictionaries or other suitable data structures
        self.matrix = {}
        self.rows = rows
        self.cols = cols

    def set(self, row, col, value):
        # Sets the value at (row, col) to 'value'
        if row < 0 or col < 0:
            raise ValueError("must be non-negative")
        elif value < 0:
            raise ValueError("Negative values are not allowed")
        elif 0 <= row < self.rows and 0 <= col < self.cols:
            if value!=0:
                self.matrix[(row, col)] = value
            elif (row,col) in self.matrix:
                del self.matrix[(row, col)]
        elif row>self.rows or col>self.cols:
            raise ValueError("Invalid row or column index")
        else:
            raise ValueError("Invalid row or column index")

    def get(self, row, col):
        #check if the row or the column is negative
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative")

        # Returns the value at (row, col)
        elif 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix.get((row, col), 0)
        else:
            raise ValueError("Invalid row or column index")

    def recommend(self, user):

        # Multiplies the sparse matrix with a given user_vector to produce recommendations
        if len(user) != self.cols:
            raise ValueError("the  dimension does not match")
        
        recommendations = [0] * self.rows

        for (row, col), value in self.matrix.items():
            recommendations[row] += value * user[col]
        
        return recommendations

    def add_movie(self, matrix):

        # Adds another sparse matrix, simulating the addition of a new movie
        if matrix.rows != self.rows or matrix.cols != self.cols:
            raise ValueError("the dimensions should match")
        for (row, col), value in matrix.matrix.items():
            if (row, col) in self.matrix:
                self.matrix[(row, col)] += value
            else:
                self.matrix[(row, col)] = value

    def to_dense(self):
        # Converts the sparse matrix to a dense matrix
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        
        for (row, col), value in self.matrix.items():
            dense_matrix[row][col] = value
        
        return dense_matrix

    def recommend_top_n_movies(self, n):
        if n <= 0:
            raise ValueError("n must be a positive integer")

        # Create a list of (movie_index, rating) pairs

        movie_ratings = []
        for col in range(self.cols):
            rating_sum = sum(self.matrix.get((row, col), 0) for row in range(self.rows))
            movie_ratings.append((col, rating_sum))

        # Sort the movie_ratings by rating in descending order (highest rated first)
        movie_ratings.sort(key=lambda x: x[1], reverse=True)
        print(movie_ratings)

        top_movies = []
        for movie, rating in movie_ratings[:n]:
            top_movies.append(movie)
        return top_movies



    