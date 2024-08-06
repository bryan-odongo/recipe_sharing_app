import React from "react";
import Layout from "../../components/Layout/Layout";
import loginBanner from "../../assets/imgs/login-Signup.jpg"; 
import { NavLink } from "react-router-dom";

function Login() {

  function handleSubmit(event) {
    event.preventDefault();
    // Handle form submission
  }

   return (
    <Layout>
    <div className="flex h-screen">
      <div className="w-[45%] bg-slate-50 flex items-center justify-center">
        <div className="w-full max-w-md">
          <h2 className="text-2xl font-bold mb-4">My Account</h2>
          <div className="text-gray-500 mb-6">
            Home &gt; My Account
          </div>
          <div className="mb-4 pb-2 flex space-x-5">
            <button
            className="font-bold border-b-2 border-black pb-1">
              Sign In</button>
            <NavLink to='/register'
            className="text-gray-500 active:border-b-2 active:border-black active:font-bold hover:text-green-600">
            Register
            </NavLink>
          </div>
          <form on onSubmit={handleSubmit}>
            <div className="mb-4">
              <label className="block text-gray-700 mb-2" htmlFor="email">
                Username or email address*
              </label>
              <input
                className=" border border-black bg-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="email"
                type="email"
                placeholder="Enter your email"
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700 mb-2" htmlFor="password">
                Password*
              </label>
              <input
                className="border border-black bg-gray-200 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="password"
                type="password"
                placeholder="Enter your password"
              />
            </div>
            <div className="flex items-center justify-between mb-6">
              <label className="flex items-center">
                <input
                  className="form-checkbox h-5 w-5 text-green-600"
                  type="checkbox"
                />
                <span className="ml-2 text-gray-700">Remember me</span>
              </label>
              <a
                className="inline-block align-baseline border-b-2 border-black font-bold text-sm text-gray-600 hover:text-green-800"
                href="#"
              >
                Forgot your Password?
              </a>
            </div>
            <div className=" w-full">
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
      <div className="md:block md:w-[55%]">
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

export default Login;

