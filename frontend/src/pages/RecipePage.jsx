import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom'; 
import Layout from '../components/Layout/Layout';


const RecipeDetails = () => {
    const { id } = useParams();
    const navigate = useNavigate(); 
    const [recipe, setRecipe] = useState(null);
    
    useEffect(() => {
        // Fetch recipe details by ID
        fetch(`/api/recipes/${id}`)
            .then(response => response.json())
            .then(data => setRecipe(data))
            .catch(error => console.error('Error fetching recipe:', error));
    }, [id]);

    const handlePreviousClick = () => {
        navigate(-1); 
    };

    const handleNextClick = () => {
        const nextRecipeId = parseInt(id) + 1;
        navigate(`/recipes/${nextRecipeId}`); 
    };

    if (!recipe) {
        return <div>Loading...</div>;
    }

    return (
        <Layout>
            <div className="recipe-details">
                <div className="recipe-header">
                    <div className="recipe-image">
                        <img src={recipe.mainImage} alt={recipe.title} />
                    </div>
                    <div className="recipe-info">
                        <h1>{recipe.title}</h1>
                        <p>{recipe.author}</p>
                        <div className="rating">Rating: {recipe.rating} ★</div>
                    </div>
                </div>

                <div className="recipe-content">
                    <div className="ingredients">
                        <h2>Ingredients</h2>
                        {recipe.ingredients.map((ingredient, index) => (
                            <div key={index} className="ingredient">
                                <img src={ingredient.image} alt={ingredient.name} />
                                <p>{ingredient.name}</p>
                            </div>
                        ))}
                    </div>

                    <div className="recipe-body">
                        <div className="summary">
                            <h2>Recipe At A Glance</h2>
                            <p>{recipe.summary}</p>
                        </div>

                        <div className="steps">
                            <h2>Steps</h2>
                            {recipe.steps.map((step, index) => (
                                <div key={index} className="step">
                                    <h3>Step {index + 1}</h3>
                                    <p>{step}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>

                <div className="navigation-buttons">
                    <button onClick={handlePreviousClick} className="previous-button">Previous</button>
                    <button onClick={handleNextClick} className="next-button">Next</button>
                </div>

                <div className="comments-section">
                    <h2>Comments</h2>
                    {recipe.comments.map((comment, index) => (
                        <div key={index} className="comment">
                            <p><strong>{comment.author}:</strong> {comment.text}</p>
                        </div>
                    ))}
                </div>
            </div>
        </Layout>
    );
};

export default RecipeDetails;
