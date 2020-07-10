
class Model:
    def __init__(self, model):
        self.model = model

    def predict(self, user_id, user_movie_list= [], top_n=20, ):
        """The user_movie_list is the list of movies the user has not seen"""

        movie_rating_predictions = []
        for movie in user_movie_list:
            predicted_rating = self.model.predictions(user_id, movie)
            movie_rating_predictions.append(movie, predicted_rating)

        movie_ranking = movie_rating_predictions.sort(key=lambda movie_rating_tuple: movie_rating_tuple[1],reverse=True)
        return [movie_rating_tuple[0] for movie_rating_tuple in movie_ranking[:20]]

