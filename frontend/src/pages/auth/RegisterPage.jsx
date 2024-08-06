import React from 'react';
import loginBanner from '../../assets/imgs/login-Signup.jpg';
import { NavLink } from 'react-router-dom';
import Layout from '../../components/Layout/Layout';
const RegisterPage = () => {
  //add register logic and form submission
  // finalize on design
  return (
    <Layout>
    <div className="flex h-screen">
      <div className="w-[45%] bg-gray-100 flex items-center justify-center">
        <div className="w-full max-w-md">
          <h2 className="text-2xl font-bold mb-4">My Account</h2>
          <div className="text-gray-500 mb-6">
            Home &gt; My Account
          </div>
          <div className="border-b mb-4 pb-2 flex justify-between">
            <NavLink to="/login"
              className="text-gray-500">
              Sign In
            </NavLink>
            <button className="font-bold border-b-2 border-black pb-1">Register</button>
          </div>
          <form>
            <div className="mb-4 flex space-x-4">
              <div className="w-1/2">
                <label className="block text-gray-700 mb-2" htmlFor="firstname">
                  Firstname*
                </label>
                <input
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="firstname"
                  type="text"
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
                  placeholder="Lastname"
                />
              </div>
            </div>
            <div className="mb-4">
              <label className="block text-gray-700 mb-2" htmlFor="email">
                Email address*
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="email"
                type="email"
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
                  placeholder="Repeat your password"
                />
              </div>
            </div>
            <div className="mb-4">
              <label className="flex items-center">
                <input
                  className="form-checkbox h-5 w-5 text-green-600"
                  type="checkbox"
                />
                <span className="ml-2 text-gray-700">Agree to Terms & Conditions</span>
              </label>
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
        </div>
      </div>
      <div className=" md:block md:w-[60%]">
        <img
          className="object-cover h-full w-full"
          src={loginBanner}
          alt="Food"
        />
      </div>
    </div>
    </Layout>
  );
};

export default RegisterPage;



