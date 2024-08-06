import Select from 'react-select';
import { countries } from 'countries-list';
import React, { useState, useContext } from 'react'
import FileUpload from './FileUpload';
import { AuthContext } from '../contexts/AuthContext';


const countryOptions = Object.keys(countries).map((code) => ({
    value: code,
    label: countries[code].name,
}));


function ProfileForm() {
    const preset_key = 'anonymous'
    const cloud_name = 'dbqwzrkvg'
    const {user, patchUser} = useContext(AuthContext)
    const [file, setFile] = useState(null);
    const [image, setImage] = useState(localStorage.getItem('profilepic') ||null);

    const [userData, setUserData] = useState({
        firstname: '',
        lastname: '',
        email: '',
        country: '',
        phone: '',
        address: '',
    })

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await patchUser(userData);
        } catch (error) {
            console.log('Failed to update profile',error);
        }
    }
    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
      };
    const handleImageChange = (e) => {
    setFile(e.target.files[0]);

    if (!file) {
        console.error('No file selected.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', preset_key);

    console.log('Uploading file to Cloudinary:', file.name);

    axios.post(`https://api.cloudinary.com/v1_1/${cloud_name}/image/upload`, formData, {
        headers: {
        'Content-Type': 'multipart/form-data'
        },
        responseType: 'text' 
    })
        .then(res => {
        console.log('Upload response:', res);
        const data = JSON.parse(res.data);  
        console.log('Image URL:', data.url);
        setUserData({ ...userData, image: data.url });
        setImage(data.url);
        localStorage.setItem('profilepic', data.url);
        })
        .catch(err => {
        console.error('Error uploading image:', err);
        });
    };

  return (
    <>
     <h2 className="text-xl text-gray-500 font-medium mb-4">My Account</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4 flex space-x-4">
            <div className="w-1/2">
              <label className="block text-gray-700 mb-2" htmlFor="firstname">
                Firstname*
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="firstname"
                type="text"
                name="firstname"
                value={userData.firstname}
                onChange={handleChange}
                placeholder="Firstname"
              />
            </div>
            <div className="w-1/2">
              <label className="block text-gray-700 mb-2" htmlFor="lastname">
                Lastname*
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="lastname"
                type="text"
                name="lastname"
                value={userData.lastname}
                onChange={handleChange}
                placeholder="Lastname"
              />
            </div>
          </div>
          <div className="mb-4 flex space-x-4">
            <div className="w-1/2">
              <label className="block text-gray-700 mb-2" htmlFor="country">
                Contry*
              </label>
              <Select
                className="shadow appearance-none rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="country"
                options={countryOptions}
                placeholder="Select your country"
                name="country"
                value={userData.country}
                onChange={handleChange}
              />
            </div>
            <div className="w-1/2">
              <label className="block text-gray-700 mb-2" htmlFor="gender">
                Gender*
              </label>
              <select
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="gender"
                type="text"
                placeholder="Select your gender"
                name="gender"
                value={userData.gender}
                onChange={handleChange}
              >
                <option value="">Select your gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="prefer not to say">Prefer not to say</option>
              </select> 
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="username">
              Username*
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="username"
              type="text"
              name="username"
              value={userData.username}
              onChange={handleChange}
              placeholder="Enter your preferred username"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="email">
              Email address*
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="email"
              type="email"
              name="email"
              value={userData.email}
              onChange={handleChange}
              placeholder="Enter your email"
            />
          </div>
          <div className="mb-4 flex space-x-4">
            <div className="w-1/2">
              <label className="block text-gray-700 mb-2" htmlFor="password">
                Password*
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="password"
                type="password"
                name="password"
                onChange={handleChange}
                placeholder="Enter your password"
              />
            </div>
            <div className="w-1/2">
              <label className="block text-gray-700 mb-2" htmlFor="repeat-password">
                Repeat Password*
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="repeat-password"
                type="password"
                name="repeat-password"
                onChange={handleChange}
                placeholder="Repeat your password"
              />
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="bio">
              Bio*
            </label>
            <textarea
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="bio"
              placeholder="Enter your Bio Information"
              rows="3"
              name="bio"
              value={userData.bio}
              onChange={handleChange}
            />
          </div>
          <div className="mb-4">
            <FileUpload 
              onFileChange={handleImageChange}
            />
            </div>

          <div className="flex items-center justify-center">
            <button
              className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit"
            >
              Submit
            </button>
          </div>
        </form>
    </>
  )
}
export default ProfileForm