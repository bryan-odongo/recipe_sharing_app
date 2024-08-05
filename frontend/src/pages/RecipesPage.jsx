import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Layout from "../components/Layout/Layout";

function Recipes() {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    const fetchRecipes = async () => {
      const response = await fetch("http://127.0.0.1:5000/api/recipes");
      const data = await response.json();
      setRecipes(data);
      console.log(recipes);
    };
    fetchRecipes();
  }, []);

  return (
    <Layout>
      <h1>Recipes</h1>
      <ul className="grid">
        {recipes.map((recipe) => (
          <Link key={recipe.id} to={`/recipes/${recipe?.id}`}>
            {recipe.title}
          </Link>
        ))}
      </ul>
    </Layout>
  );
}

export default Recipes;
