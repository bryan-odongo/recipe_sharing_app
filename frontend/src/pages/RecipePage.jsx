import { useParams } from "react-router-dom";
import React, { useEffect, useState } from "react";
import Layout from "../components/Layout/Layout";

function Recipe() {
  const { recipe } = useParams();

  const [singleRecipe, setRecipe] = useState(null);

  useEffect(() => {
    const fetchRecipe = async () => {
      const response = await fetch(
        `http://127.0.0.1:5000/api/recipes/${recipe}`
      );
      const data = await response.json();
      setRecipe(data);
      console.log("RECIPE: ", singleRecipe);
    };
    fetchRecipe();
  }, []);

  console.log(recipe);
  return <Layout>Recipe: {singleRecipe?.title}</Layout>;
}

export default Recipe;
