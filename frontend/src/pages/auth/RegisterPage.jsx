import React from 'react';
import loginBanner from '../../assets/imgs/singup-login.jpg';
import { NavLink } from 'react-router-dom';
import Layout from '../../components/Layout/Layout';
import { AuthContext } from '../../contexts/AuthContext';
const RegisterPage = () => {
  //add register logic and form submission
  // finalize on design

  const { register } = React.useContext(AuthContext);
  const [userDetails, setUserDetails] = React.useState({
    email: "",
    password: "",
    first_name: "",
    last_name: ""
  })

  const handleSubmit = async (event) => {
    event.preventDefault();
    try  {
      await register(userDetails);
    } catch(error){
      if (error.response) {
        return error.response
      } else {
        throw error;
      }
    }
  }

  return (
    <Layout>
    <div className="flex h-screen max-w-screen justify-center items-center bg-cover  bg-no-repeat"
     style={{backgroundImage: `url(${loginBanner})`}}>
      <div className="w-[45%]  bg-black bg-opacity-60 rounded-xl pb-4 pt-4 shadow-xl max-h-screen flex items-center justify-center">
        <div className="w-full text-white max-w-md">
          <h2 className="text-2xl  font-bold mb-4">My Account</h2>
          <div className=" mb-6">
            Home &gt; My Account
          </div>
          <div className="border-b border-slate-200 mb-4 pb-2 flex justify-between ">
            <NavLink to="/login"
              className="hover:bg-green-400 p-2 rounded-lg">
              Sign In
            </NavLink>
            <button className="font-bold border-b-4 border-white pb-1 hover:bg-green-400 p-1 rounded-lg">Register</button>
          </div>
          <form >
            <div className="mb-4 flex space-x-4">
              <div className="w-1/2">
                <label className="block  mb-2" htmlFor="firstname">
                  Firstname*
                </label>
                <input
                  className="shadow appearance-none border bg-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="firstname"
                  type="text"
                  placeholder="Firstname"
                />
              </div>
              <div className="w-1/2">
                <label className="block  mb-2" htmlFor="lastname">
                  Lastname*
                </label>
                <input
                  className="shadow appearance-none border bg-gray-200 text-gray-700 rounded w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="lastname"
                  type="text"
                  placeholder="Lastname"
                />
              </div>
            </div>
            <div className="mb-4">
              <label className="block t mb-2" htmlFor="email">
                Email address*
              </label>
              <input
                className="shadow appearance-none border bg-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="email"
                type="email"
                placeholder="Enter your email"
              />
            </div>
            <div className="mb-4 flex space-x-4">
              <div className="w-1/2">
                <label className="block  mb-2" htmlFor="password">
                  Password*
                </label>
                <input
                  className="shadow appearance-none border bg-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="password"
                  type="password"
                  placeholder="Enter your password"
                />
              </div>
              <div className="w-1/2">
                <label className="block mb-2" htmlFor="repeat-password">
                  Repeat Password*
                </label>
                <input
                  className="shadow appearance-none border bg-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="repeat-password"
                  type="password"
                  placeholder="Repeat your password"
                />
              </div>
            </div>
            <div className="mb-4">
              <label className="flex items-center">
                <input
                  className="form-checkbox bg-gray-200 h-5 w-5 text-green-600"
                  type="checkbox"
                />
                <span className="ml-2 ">Agree to Terms & Conditions</span>
              </label>
            </div>
            <div className="flex items-center justify-center">
              <button
                className="bg-green-500 w-full hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit"
              >
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>
      {/* <div className=" md:block md:w-[60%]">
        <img
          className="object-cover h-full w-full"
          src={loginBanner}
          alt="Food"
        />
      </div> */}
    </div>
    </Layout>
  );
};

export default RegisterPage;



