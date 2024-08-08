import React, { useState, useEffect } from 'react';
import Layout from './Layout';


const RecipeDetails = ({ match }) => {
    const [recipe, setRecipe] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [rating, setRating] = useState(0);
    const [review, setReview] = useState('');
    const [bookmarked, setBookmarked] = useState(false);

    // Fetch recipe from API
    useEffect(() => {
        const fetchRecipe = async () => {
            try {
                const response = await fetch(`https://the-backend-api.com/recipes/${match.params.id}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch recipe');
                }
                const data = await response.json();
                setRecipe(data);
                setLoading(false);
            } catch (error) {
                setError(error.message);
                setLoading(false);
            }
        };

        fetchRecipe();
    }, [match.params.id]);

    const handleRating = (rate) => {
        setRating(rate);
    };

    const handleReviewChange = (e) => {
        setReview(e.target.value);
    };

    const handleBookmark = () => {
        setBookmarked(!bookmarked);
    };

    if (loading) {
        return (
            <Layout>
                <div className="loading">Loading...</div>
            </Layout>
        );
    }

    if (error) {
        return (
            <Layout>
                <div className="error">{error}</div>
            </Layout>
        );
    }

    return (
        <Layout>
            <div className="recipe-details">
                <h1 className="recipe-title">{recipe.title}</h1>
                <img src={recipe.image} alt={recipe.title} className="recipe-image" />
                
                <div className="recipe-info">
                    <p><strong>Preparation Time:</strong> {recipe.prepTime}</p>
                    <p><strong>Cooking Time:</strong> {recipe.cookTime}</p>
                </div>

                <div className="recipe-ingredients">
                    <h2>Ingredients</h2>
                    <ul>
                        {recipe.ingredients.map((ingredient, index) => (
                            <li key={index}>{ingredient}</li>
                        ))}
                    </ul>
                </div>

                <div className="recipe-instructions">
                    <h2>Instructions</h2>
                    <ol>
                        {recipe.instructions.map((instruction, index) => (
                            <li key={index}>{instruction}</li>
                        ))}
                    </ol>
                </div>

                <div className="chef-notes">
                    <h3>Chef's Notes</h3>
                    <p>{recipe.chefNotes}</p>
                </div>

                <div className="recipe-actions">
                    <button onClick={handleBookmark} className="bookmark-button">
                        {bookmarked ? 'Remove Bookmark' : 'Bookmark'}
                    </button>
                    <button className="share-button">Share</button>
                </div>

                <div className="user-interaction">
                    <h3>Your Rating</h3>
                    <div className="rating">
                        {[1, 2, 3, 4, 5].map((star) => (
                            <span
                                key={star}
                                className={star <= rating ? 'star filled' : 'star'}
                                onClick={() => handleRating(star)}
                            >
                                ☆
                            </span>
                        ))}
                    </div>

                    <h3>Your Review</h3>
                    <textarea
                        value={review}
                        onChange={handleReviewChange}
                        placeholder="What did you think about this recipe?"
                        className="review-textarea"
                    />
                </div>
            </div>
        </Layout>
    );
};

export default RecipeDetails;
