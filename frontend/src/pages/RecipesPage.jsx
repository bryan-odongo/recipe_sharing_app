import React, { useEffect, useState } from "react";
import Layout from "../components/Layout/Layout";
import RecipeForm from "../components/Recipes/RecipeForm";

function Recipes() {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    const fetchRecipes = async () => {
      const response = await fetch("http://127.0.0.1:5000/api/recipes");
      const data = await response.json();
      setRecipes(data);
    };
    fetchRecipes();
  }, []);

  return (
    <Layout>
      <section className="w-full h-full">
        <div className="max-w-4xl xl:max-w-[73rem] w-full mx-auto py-3 flex flex-col justify-between items-center">
          <RecipeForm />
          {/* <ul className="grid">
            {recipes.map((recipe) => (
              <Link key={recipe.id} to={`/recipes/${recipe?.id}`}>
                {recipe.title}
              </Link>
            ))}
          </ul> */}
        </div>
      </section>
    </Layout>
  );
}

export default Recipes;
