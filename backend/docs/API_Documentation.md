# API Documentation

## Overview
This API allows users to manage recipes, ingredients, cooking hacks, cooking tips, images, and replies.

## Endpoints

### Recipes

#### GET /recipes
- **Description**: Retrieve a list of all recipes.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "title": "Pilau",
            "description": "A classic Kenyan dish made with rice.",
            "prep_time": 15,
            "cook_time": 20,
            "servings": 4,
            "skill_level": "Medium",
            "country": "Kenya",
            "diet": "Vegetarian",
            "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
            "image_url": "http://example.com/spaghetti.jpg",
            "user_id": 1,
            "created_at": "2024-08-07T00:00:00"
        }
    ]
    ```

#### POST /recipes
- **Description**: Create a new recipe.
- **Request**:
    ```json
    {
        "title": "Pilau",
        "description": "A classic Kenyan dish made with rice.",
        "prep_time": 15,
        "cook_time": 20,
        "servings": 4,
        "skill_level": "Medium",
        "country": "Kenya",
        "diet": "Vegetarian",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "image_url": "http://example.com/spaghetti.jpg",
        "user_id": 1
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Pilau",
        "description": "A classic Kenyan dish made with rice.",
        "prep_time": 15,
        "cook_time": 20,
        "servings": 4,
        "skill_level": "Medium",
        "country": "Kenya",
        "diet": "Vegetarian",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "image_url": "http://example.com/spaghetti.jpg",
        "user_id": 1,
        "created_at": "2024-08-07T00:00:00"
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create recipe.


#### GET /recipes/{id}
- **Description**: Get an existing recipe.
- **Response**:
    ```json
    {
        "cook_time": 20,
        "country": "Kenya",
        "created_at": "2024-08-07T00:00:00",
        "description": "A classic Kenyan dish made with rice.",
        "diet": "Vegetarian",
        "id": 1,
        "image_url": "http://example.com/spaghetti.jpg",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Pilau",
        "user_id": 1
    }
    ```

#### PATCH /recipes/{id}
- **Description**: Update an existing recipe.
- **Request**:
    ```json
    {
        "cook_time": 25,
        "description": "An updated description of the recipe."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Pilau",
        "description": "An updated description of the recipe.",
        "prep_time": 15,
        "cook_time": 25,
        "servings": 4,
        "skill_level": "Medium",
        "country": "Kenya",
        "diet": "Vegetarian",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "image_url": "http://example.com/spaghetti.jpg",
        "user_id": 1,
        "created_at": "2024-08-07T00:00:00"
    }
    ```
- **Errors**:
    - `404 Not Found`: Recipe not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update recipe.

#### DELETE /recipes/{id}
- **Description**: Delete an existing recipe.
- **Response**:
    ```json
    {
        "message": "Recipe successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Recipe not found.
    - `500 Internal Server Error`: Unable to delete recipe due to database constraints.

### Ingredients

#### GET /ingredients
- **Description**: Retrieve a list of all ingredients.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "name": "Spaghetti",
            "image": "http://example.com/spaghetti.jpg",
            "recipe": {
                "id": 1,
                "title": "Spaghetti Bolognese",
                "description": "A delicious Italian dish.",
                "cook_time": 30,
                "prep_time": 15,
                "country": "Italy",
                "diet": "Non-Vegetarian",
                "instructions": "1. Cook spaghetti. 2. Prepare sauce. 3. Mix together.",
                "image_url": "http://example.com/spaghetti.jpg",
                "servings": 4,
                "skill_level": "Medium",
                "created_at": "2024-08-07T00:00:00"
            }
        }
    ]
    ```

#### POST /ingredients
- **Description**: Create a new ingredient.
- **Request**:
    ```json
    {
        "recipe_id": 1,
        "name": "Spaghetti",
        "image": "http://example.com/spaghetti.jpg"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Spaghetti",
        "image": "http://example.com/spaghetti.jpg",
        "recipe": {
            "id": 1,
            "title": "Spaghetti Bolognese",
            "description": "A delicious Italian dish.",
            "cook_time": 30,
            "prep_time": 15,
            "country": "Italy",
            "diet": "Non-Vegetarian",
            "instructions": "1. Cook spaghetti. 2. Prepare sauce. 3. Mix together.",
            "image_url": "http://example.com/spaghetti.jpg",
            "servings": 4,
            "skill_level": "Medium",
            "created_at": "2024-08-07T00:00:00"
        }
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `404 Not Found`: Recipe not found.
    - `500 Internal Server Error`: Unable to create ingredient.

#### GET /ingredients/{id}
- **Description**: Get an existing ingredient.
- **Response**:
    ```json
    {
    "id": 1,
    "image": "http://example.com/spaghetti.jpg",
    "name": "Spaghetti",
    "recipe": {
        "cook_time": 20,
        "country": "Kenya",
        "created_at": "2024-08-07T00:00:00",
        "description": "A classic Kenyan dish made with rice.",
        "diet": "Vegetarian",
        "id": 1,
        "image_url": "http://example.com/spaghetti.jpg",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Pilau",
        "user_id": 1
        }
    }
    ```

#### PATCH /ingredients/{id}
- **Description**: Update an existing ingredient.
- **Request**:
    ```json
    {
        "name": "Updated Ingredient Name",
        "image": "http://example.com/updated_image.jpg"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Updated Ingredient Name",
        "image": "http://example.com/updated_image.jpg",
        "recipe": {
            "id": 1,
            "title": "Spaghetti Bolognese",
            "description": "A delicious Italian dish.",
            "cook_time": 30,
            "prep_time": 15,
            "country": "Italy",
            "diet": "Non-Vegetarian",
            "instructions": "1. Cook spaghetti. 2. Prepare sauce. 3. Mix together.",
            "image_url": "http://example.com/spaghetti.jpg",
            "servings": 4,
            "skill_level": "Medium",
            "created_at": "2024-08-07T00:00:00"
        }
    }
    ```
- **Errors**:
    - `404 Not Found`: Ingredient not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update ingredient.

#### DELETE /ingredients/{id}
- **Description**: Delete an existing ingredient.
- **Response**:
    ```json
    {
        "message": "Ingredient successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Ingredient not found.
    - `500 Internal Server Error`: Unable to delete ingredient due to database constraints.

### Cooking Hacks

#### GET /cookinghacks
- **Description**: Retrieve a list of all cooking hacks.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "content": "Use a spoon to peel ginger.",
            "created_at": "2024-08-07T00:00:00"
        }
    ]
    ```

#### POST /cookinghacks
- **Description**: Create a new cooking hack.
- **Request**:
    ```json
    {
        "content": "Use a spoon to peel ginger."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "content": "Use a spoon to peel ginger."
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create cooking hack.

#### GET /cookinghacks/{id}
- **Description**: Get an existing cooking hack.
- **Response**:
    ```json
    {
        "content": "To prevent pasta from sticking, add a little oil to the water.",
        "id": 1
    }
    ```

#### PATCH /cookinghacks/{id}
- **Description**: Update an existing cooking hack.
- **Request**:
    ```json
    {
        "content": "Updated cooking hack content."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "content": "Updated cooking hack content."
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking hack not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update cooking hack.

#### DELETE /cookinghacks/{id}
- **Description**: Delete an existing cooking hack.
- **Response**:
    ```json
    {
        "message": "Cooking hack successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking hack not found.
    - `500 Internal Server Error`: Unable to delete cooking hack due to database constraints.

### Cooking Tips

#### GET /cookingtips
- **Description**: Retrieve a list of all cooking tips.
- **Response**:
    ```json
    [
        {
            "content": "Rinse rice before cooking. Use a 1:2 rice-to-water ratio.",
            "created_at": "Wed, 07 Aug 2024 00:00:00 GMT",
            "id": 1,
            "title": "How to cook perfect rice",
            "updated_at": "Wed, 07 Aug 2024 00:00:00 GMT"
        }
    ]
    ```

#### POST /cookingtips
- **Description**: Create a new cooking tip.
- **Request**:
    ```json
    {
        "content": "Add a pinch of salt to enhance sweetness.",
        "title": "How to cook perfect chapatis",
        "created_at": "2024-06-07T00:00:00",
        "updated_at": "2024-07-07T00:00:00"
    }
    ```
- **Response**:
    ```json
    {
        "content": "Add a pinch of salt to enhance sweetness",
        "created_at": "Fri, 07 Jun 2024 00:00:00 GMT",
        "id": 3,
        "title": "How to cook perfect chapatis",
        "updated_at": "Sun, 07 Jul 2024 00:00:00 GMT"
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create cooking tip.

#### GET /cookingtips/{id}
- **Description**: Get an existing cooking tip.
- **Request**:
    ```json
    {
        "content": "Rinse rice before cooking. Use a 1:2 rice-to-water ratio.",
        "created_at": "Wed, 07 Aug 2024 00:00:00 GMT",
        "id": 1,
        "title": "How to cook perfect rice",
        "updated_at": "Wed, 07 Aug 2024 00:00:00 GMT"
    }
    ```
#### PATCH /cookingtips/{id}
- **Description**: Update an existing cooking tip.
- **Request**:
    ```json
    
    {
        "content": "Add my salt to enhance sweetness",
        "created_at": "2024-07-07T00:00:00",
        "id": 1,
        "title": "How to cook perfect chapatis",
        "updated_at": "2024-07-07T00:00:00"
    }
    ```
- **Response**:
    ```json
    {
        "content": "Add my salt to enhance sweetness",
        "created_at": "Sun, 07 Jul 2024 00:00:00 GMT",
        "id": 1,
        "title": "How to cook perfect chapatis",
        "updated_at": "Sun, 07 Jul 2024 00:00:00 GMT"
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking tip not found.
    - `400 Bad Request`: Invalid data format.
    - `400 Bad Request`: Invalid date format.
    - `500 Internal Server Error`: Unable to update cooking tip.

#### DELETE /cookingtips/{id}
- **Description**: Delete an existing cooking tip.
- **Response**:
    ```json
    {
        "message": "Cooking tip successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking tip not found.
    - `500 Internal Server Error`: Unable to delete cooking tip due to database constraints.

### Images

#### GET /images
- **Description**: Retrieve a list of all images.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "image_url": "http://example.com/spaghetti1.jpg",
            "recipe": {
                "cook_time": 20,
                "country": "Kenya",
                "created_at": "2024-08-07T00:00:00",
                "description": "A classic Kenyan dish made with rice.",
                "diet": "Vegetarian",
                "id": 1,
                "image_url": "http://example.com/spaghetti.jpg",
                "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
                "prep_time": 15,
                "servings": 4,
                "skill_level": "Medium",
                "title": "Pilau",
                "user_id": 1
            }
        },
        {
            "id": 2,
            "image_url": "http://example.com/spaghetti2.jpg",
            "recipe": {
                "cook_time": 20,
                "country": "Kenya",
                "created_at": "2024-08-07T00:00:00",
                "description": "A classic Kenyan dish made with rice.",
                "diet": "Vegetarian",
                "id": 1,
                "image_url": "http://example.com/spaghetti.jpg",
                "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
                "prep_time": 15,
                "servings": 4,
                "skill_level": "Medium",
                "title": "Pilau",
                "user_id": 1
            }
        },
        {
            "id": 3,
            "image_url": "http://example.com/curry1.jpg",
            "recipe": {
                "cook_time": 40,
                "country": "India",
                "created_at": "2024-08-07T00:00:00",
                "description": "A spicy and flavorful chicken curry with coconut milk and aromatic spices.",
                "diet": "Non-Vegetarian",
                "id": 2,
                "image_url": "http://example.com/curry.jpg",
                "instructions": "1. Cook chicken with spices. 2. Add coconut milk and simmer. 3. Serve with rice.",
                "prep_time": 20,
                "servings": 4,
                "skill_level": "Hard",
                "title": "Chicken Curry",
                "user_id": 2
            }
        },
        {
            "id": 4,
            "image_url": "http://example.com/curry2.jpg",
            "recipe": {
                "cook_time": 40,
                "country": "India",
                "created_at": "2024-08-07T00:00:00",
                "description": "A spicy and flavorful chicken curry with coconut milk and aromatic spices.",
                "diet": "Non-Vegetarian",
                "id": 2,
                "image_url": "http://example.com/curry.jpg",
                "instructions": "1. Cook chicken with spices. 2. Add coconut milk and simmer. 3. Serve with rice.",
                "prep_time": 20,
                "servings": 4,
                "skill_level": "Hard",
                "title": "Chicken Curry",
                "user_id": 2
            }
        }
    ]
    ```

#### POST /images
- **Description**: Create a new image.
- **Request**:
    ```json
    {
        "url": "http://example.com/image.jpg",
        "recipe_id": "1."
    }
    ```
- **Response**:
    ```json
    {
        "id": 5,
        "image_url": "http://example.com/image.jpg",
        "recipe": {
            "cook_time": 20,
            "country": "Kenya",
            "created_at": "2024-08-07T00:00:00",
            "description": "A classic Kenyan dish made with rice.",
            "diet": "Vegetarian",
            "id": 1,
            "image_url": "http://example.com/spaghetti.jpg",
            "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
            "prep_time": 15,
            "servings": 4,
            "skill_level": "Medium",
            "title": "Pilau",
            "user_id": 1
        }
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create image.


#### GET /images/{id}
- **Description**: Get an existing image.
- **Response**:
    ```json
    {
        "id": 1,
        "image_url": "http://example.com/updated_image.jpg",
        "recipe": {
            "cook_time": 20,
            "country": "Kenya",
            "created_at": "2024-08-07T00:00:00",
            "description": "A classic Kenyan dish made with rice.",
            "diet": "Vegetarian",
            "id": 1,
            "image_url": "http://example.com/spaghetti.jpg",
            "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
            "prep_time": 15,
            "servings": 4,
            "skill_level": "Medium",
            "title": "Pilau",
            "user_id": 1
            }
    }
    ```

#### PATCH /images/{id}
- **Description**: Update an existing image.
- **Request**:
    ```json
    {
        "image_url": "http://example.com/updated_image.jpg",
        "recipe_id": "1."
    }
    ```
- **Response**:
    ```json
    {
    "id": 1,
    "image_url": "http://example.com/updated_image.jpg",
    "recipe": {
        "cook_time": 20,
        "country": "Kenya",
        "created_at": "2024-08-07T00:00:00",
        "description": "A classic Kenyan dish made with rice.",
        "diet": "Vegetarian",
        "id": 1,
        "image_url": "http://example.com/spaghetti.jpg",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Pilau",
        "user_id": 1
        }
    }
    ```
- **Errors**:
    - `404 Not Found`: Image not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update image.

#### DELETE /images/{id}
- **Description**: Delete an existing image.
- **Response**:
    ```json
    {
        "message": "Image successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Image not found.
    - `500 Internal Server Error`: Unable to delete image due to database constraints.

### Replies

#### GET /replies
- **Description**: Retrieve a list of all replies.
- **Response**:
    ```json
    [
        {
            "id": 2,
            "reply": "We're sorry to hear that. We will work on improving it.",
            "review_id": 2
        }
    ]
    ```

#### POST /replies
- **Description**: Create a new reply.
- **Request**:
    ```json
    {
        "review_id": "1.",
        "reply": "Your recipe is a life saver",
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "reply": "Your recipe is a life saver",
        "review": {
            "id": 2,
            "user_id": 3,
            "recipe_id": 4,
            "review": "Great recipe!",
            "created_at": "2024-08-08T00:00:00",
            "updated_at": "2024-08-08T00:00:00"
        }
    }

    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `404 Not Found`: Comment or user not found.
    - `500 Internal Server Error`: Unable to create reply.

#### GET /replies/{id}
- **Description**: Get an existing reply.
- **Request**:
    ```json
    {
        "id": 2,
        "reply": "We're sorry to hear that. We will work on improving it.",
        "review": {
            "id": 2,
            "user_id": 3,
            "recipe_id": 4,
            "review": "The recipe was a bit too salty.",
            "created_at": "2024-08-08T00:00:00",
            "updated_at": "2024-08-08T00:00:00"
        }
    }

    ```
#### PATCH /replies/{id}
- **Description**: Update an existing reply.
- **Response**:
    ```json
     {
        "review_id": "3",
        "reply": "Your recipe is a life saver"
    }
    ```
- **Response**:
    ```json
    {
        "id": 3,
        "reply": "Your recipe is a life saver",
        "review": {
            "id": 3,
            "user_id": 2,
            "recipe_id": 5,
            "review": "This recipe was great, but I had to adjust the seasoning.",
            "created_at": "2024-08-07T00:00:00",
            "updated_at": "2024-08-07T00:00:00"
        }
    }

    ```
- **Errors**:
    - `404 Not Found`: Reply not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update reply.

#### DELETE /replies/{id}
- **Description**: Delete an existing reply.
- **Response**:
    ```json
    {
        "message": "Reply successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Reply not found.
    - `500 Internal Server Error`: Unable to delete reply due to database constraints.
