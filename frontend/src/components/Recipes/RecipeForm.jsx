import clsx from "clsx";
import React, { useState } from "react";
import { BiPlus } from "react-icons/bi";

function RecipeForm() {
  const [formData, setFormData] = useState({
    banner_image: "",
    banner_file: null,
    description: "",
    ingredients: [],
    instructions: "",
    title: "",
    user_id: 0,
    other_images: [],
  });

  const [loading, setLoading] = useState(false);
  const [uploadingBanner, setUploadingBanner] = useState(false);
  const [uploadingIngredient, setUploadingIngredient] = useState(null);
  const [uploadingOtherImage, setUploadingOtherImage] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleFileChange = (e) => {
    const { name, files } = e.target;
    const file = files[0];
    if (name === "banner_file") {
      setFormData((prevData) => ({
        ...prevData,
        [name]: file,
      }));
      uploadImage(file, (url) =>
        setFormData((prevData) => ({
          ...prevData,
          banner_image: url,
        }))
      );
    }
  };

  const handleIngredientFileChange = (index, e) => {
    const { files } = e.target;
    const file = files[0];
    setFormData((prevData) => {
      const updatedIngredients = [...prevData.ingredients];
      updatedIngredients[index].image_file = file;
      return { ...prevData, ingredients: updatedIngredients };
    });
    uploadImage(
      file,
      (url) =>
        setFormData((prevData) => {
          const updatedIngredients = [...prevData.ingredients];
          updatedIngredients[index].image = url;
          return { ...prevData, ingredients: updatedIngredients };
        }),
      index
    );
  };

  const handleIngredientChange = (index, e) => {
    const { name, value } = e.target;
    const updatedIngredients = [...formData.ingredients];
    updatedIngredients[index][name] = value;
    setFormData((prevData) => ({
      ...prevData,
      ingredients: updatedIngredients,
    }));
  };

  const handleAddIngredient = () => {
    setFormData((prevData) => ({
      ...prevData,
      ingredients: [
        ...prevData.ingredients,
        { image: "", image_file: null, name: "", quantity: "" },
      ],
    }));
  };

  const handleRemoveIngredient = (index) => {
    const updatedIngredients = formData.ingredients.filter(
      (_, i) => i !== index
    );
    setFormData((prevData) => ({
      ...prevData,
      ingredients: updatedIngredients,
    }));
  };

  const handleOtherImageFileChange = (index, e) => {
    const { files } = e.target;
    const file = files[0];
    setFormData((prevData) => {
      const updatedOtherImages = [...prevData.other_images];
      updatedOtherImages[index].image_file = file;
      return { ...prevData, other_images: updatedOtherImages };
    });
    uploadImage(
      file,
      (url) =>
        setFormData((prevData) => {
          const updatedOtherImages = [...prevData.other_images];
          updatedOtherImages[index].image = url;
          return { ...prevData, other_images: updatedOtherImages };
        }),
      index,
      "other_image"
    );
  };

  const handleOtherImageChange = (index, e) => {
    const { name, value } = e.target;
    const updatedOtherImages = [...formData.other_images];
    updatedOtherImages[index][name] = value;
    setFormData((prevData) => ({
      ...prevData,
      other_images: updatedOtherImages,
    }));
  };

  const handleAddOtherImage = () => {
    setFormData((prevData) => ({
      ...prevData,
      other_images: [
        ...prevData.other_images,
        { image: "", image_file: null, name: "" },
      ],
    }));
  };

  const handleRemoveOtherImage = (index) => {
    const updatedOtherImages = formData.other_images.filter(
      (_, i) => i !== index
    );
    setFormData((prevData) => ({
      ...prevData,
      other_images: updatedOtherImages,
    }));
  };

  const uploadImage = (image, callback, index = null, type = "ingredient") => {
    if (index === null && type === "banner") {
      setUploadingBanner(true);
    } else if (type === "ingredient") {
      setUploadingIngredient(index);
    } else if (type === "other_image") {
      setUploadingOtherImage(index);
    }

    const data = new FormData();
    data.append("file", image);
    data.append("upload_preset", "recipes_app");
    data.append("cloud_name", "dyswmfsw3");
    fetch(`https://api.cloudinary.com/v1_1/dyswmfsw3/image/upload`, {
      method: "post",
      body: data,
    })
      .then((resp) => resp.json())
      .then((data) => {
        console.log("Image URL:", data.url); // Log the image URL
        callback(data.url);
        if (index === null && type === "banner") {
          setUploadingBanner(false);
        } else if (type === "ingredient") {
          setUploadingIngredient(null);
        } else if (type === "other_image") {
          setUploadingOtherImage(null);
        }
      })
      .catch((err) => {
        console.log(err);
        if (index === null && type === "banner") {
          setUploadingBanner(false);
        } else if (type === "ingredient") {
          setUploadingIngredient(null);
        } else if (type === "other_image") {
          setUploadingOtherImage(null);
        }
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    // Submit the form data to the API
    console.log("Form submitted:", formData);
    setLoading(false);
    // Reset form
    setFormData({
      banner_image: "",
      banner_file: null,
      description: "",
      ingredients: [],
      instructions: "",
      title: "",
      user_id: 0,
      other_images: [],
    });
  };

  return (
    <div className="w-full h-full">
      <div className="max-w-3xl mx-auto py-8 px-12 bg-gradient-to-bl shadow-md shadow-slate-500 drop-shadow-lg from-slate-100 to-white rounded-md">
        <form
          onSubmit={handleSubmit}
          className="[&_label]:text-slate-600 [&_label]:text-sm [&_label]:pb-[2px]"
        >
          <div className="mb-1 grid grid-cols-2 gap-3">
            <fieldset>
              <label className="block text-gray-700 font-semibold">
                Banner Image URL
              </label>
              <input
                type="text"
                name="banner_image"
                value={formData.banner_image}
                onChange={handleChange}
                className="w-full px-3 py-2 text-sm border border-slate-300 rounded-md"
                disabled={uploadingBanner}
              />
            </fieldset>
            <fieldset>
              <label className="block text-gray-700 font-semibold">
                Or Upload Image
              </label>
              <input
                type="file"
                name="banner_file"
                onChange={handleFileChange}
                className="w-full px-3 py-[6.5px] text-xs border border-slate-300 rounded-md"
                disabled={uploadingBanner}
              />
            </fieldset>
          </div>
          {uploadingBanner == null && (
            <div className="mb-2 text-center text-gray-700">
              Uploading banner image, please wait...
            </div>
          )}
          <div className="mb-1">
            <label className="block text-gray-700 font-semibold">Title</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              className="w-full px-3 py-2 text-sm border border-slate-300 rounded-md"
              disabled={
                uploadingBanner ||
                uploadingIngredient !== null ||
                uploadingOtherImage !== null
              }
            />
          </div>
          <div className="mb-">
            <label className="block text-gray-700 font-semibold">
              Description
            </label>
            <textarea
              name="description"
              value={formData.description}
              onChange={handleChange}
              className="w-full px-3 py-1.5 text-sm border border-slate-300 rounded-md"
              disabled={
                uploadingBanner ||
                uploadingIngredient !== null ||
                uploadingOtherImage !== null
              }
            />
          </div>
          <div className="mb-">
            <label className="block text-gray-700 font-semibold">
              Instructions
            </label>
            <textarea
              name="instructions"
              value={formData.instructions}
              onChange={handleChange}
              className="w-full px-3 py-1.5 text-sm border border-slate-300 rounded-md"
              disabled={
                uploadingBanner ||
                uploadingIngredient !== null ||
                uploadingOtherImage !== null
              }
            />
          </div>
          <div className="mb- hidden">
            <label className="block text-gray-700 font-semibold">User ID</label>
            <input
              type="number"
              name="user_id"
              value={formData.user_id}
              onChange={handleChange}
              className="w-full px-3 py-1.5 text-sm border border-slate-300 rounded-md"
              disabled={
                uploadingBanner ||
                uploadingIngredient !== null ||
                uploadingOtherImage !== null
              }
            />
          </div>
          <div
            className={clsx(
              formData.ingredients.length === 0 &&
                formData.other_images.length === 0
                ? "flex items-center justify-start space-x-5"
                : "grid"
            )}
          >
            <div className="mb-">
              <label className="block text-gray-700 font-semibold">
                Ingredients
              </label>
              {formData.ingredients.map((ingredient, index) => (
                <div key={index} className="mb-2 flex space-x-2 items-center">
                  <input
                    type="text"
                    name="image"
                    placeholder="Image URL"
                    value={
                      uploadingIngredient == null
                        ? ingredient.image
                        : "Uploading image..."
                    }
                    onChange={(e) => handleIngredientChange(index, e)}
                    className="w-1/4 px-3 py-1.5 text-sm border border-slate-300 rounded-md"
                    disabled={uploadingIngredient === index}
                  />
                  <input
                    type="file"
                    name="image_file"
                    onChange={(e) => handleIngredientFileChange(index, e)}
                    className="w-1/4 px-3 py-[4px] text-sm border border-slate-300 rounded-md"
                    disabled={uploadingIngredient === index}
                  />
                  <input
                    type="text"
                    name="name"
                    placeholder="Name"
                    value={ingredient.name}
                    onChange={(e) => handleIngredientChange(index, e)}
                    className="w-1/4 px-3 py-1.5 text-sm border border-slate-300 rounded-md"
                    disabled={uploadingIngredient === index}
                  />
                  <input
                    type="text"
                    name="quantity"
                    placeholder="Quantity"
                    value={ingredient.quantity}
                    onChange={(e) => handleIngredientChange(index, e)}
                    className="w-1/4 px-3 py-1.5 text-sm border border-slate-300 rounded-md"
                    disabled={uploadingIngredient === index}
                  />
                  <button
                    type="button"
                    onClick={() => handleRemoveIngredient(index)}
                    className="px-2 py-1 bg-red-500 text-white rounded-md"
                    disabled={uploadingIngredient === index}
                  >
                    X
                  </button>
                </div>
              ))}
              <button
                type="button"
                onClick={handleAddIngredient}
                className="mt- text-sm w-48 inline-flex space-x-2 items-center justify-center px-4 py-2 mb-2 font-semibold bg-blue-500 text-white rounded-md"
                disabled={
                  uploadingBanner ||
                  uploadingIngredient !== null ||
                  uploadingOtherImage !== null
                }
              >
                <span>Add Ingredient</span>
                <BiPlus className="text-2xl" />
              </button>
            </div>
            <div className="mb-">
              <label className="block text-gray-700 font-semibold">
                Other Images
              </label>
              {formData.other_images.map((other_image, index) => (
                <div key={index} className="mb-2 flex space-x-2 items-center">
                  <input
                    type="text"
                    name="image"
                    placeholder="Image URL"
                    value={
                      uploadingOtherImage == null
                        ? other_image.image
                        : "Uploading image..."
                    }
                    onChange={(e) => handleOtherImageChange(index, e)}
                    className="w-1/2 px-3 py-1.5 text-sm border border-slate-300 rounded-md"
                    disabled={uploadingOtherImage === index}
                  />
                  <input
                    type="file"
                    name="image_file"
                    onChange={(e) => handleOtherImageFileChange(index, e)}
                    className="w-1/4 px-3 py-[4px] text-sm border border-slate-300 rounded-md"
                    disabled={uploadingOtherImage === index}
                  />
                  <input
                    type="text"
                    name="name"
                    placeholder="Name"
                    value={other_image.name}
                    onChange={(e) => handleOtherImageChange(index, e)}
                    className="w-1/4 px-3 py-1.5 text-sm border border-slate-300 rounded-md"
                    disabled={uploadingOtherImage === index}
                  />
                  <button
                    type="button"
                    onClick={() => handleRemoveOtherImage(index)}
                    className="px-2 py-1 bg-red-500 text-white rounded-md"
                    disabled={uploadingOtherImage === index}
                  >
                    X
                  </button>
                </div>
              ))}
              <button
                type="button"
                onClick={handleAddOtherImage}
                className="mt- w-48 inline-flex space-x-2 items-center justify-center px-4 py-2 mb-2 font-semibold bg-blue-500 text-sm text-white rounded-md"
                disabled={
                  uploadingBanner ||
                  uploadingIngredient !== null ||
                  uploadingOtherImage !== null
                }
              >
                <span>Add Other Image</span>
                <BiPlus className="text-2xl" />
              </button>
            </div>
          </div>
          <button
            type="submit"
            className="w-full mt-2 px-4 py-2 font-semibold bg-green-600 text-white rounded-md"
            disabled={
              loading ||
              uploadingBanner ||
              uploadingIngredient !== null ||
              uploadingOtherImage !== null
            }
          >
            {loading ? "Submitting..." : "Submit Recipe"}
          </button>
        </form>
      </div>
    </div>
  );
}

export default RecipeForm;
