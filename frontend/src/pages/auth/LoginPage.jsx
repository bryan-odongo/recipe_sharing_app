import React from "react";
import Layout from "../../components/Layout/Layout";
import loginBanner from "../../assets/imgs/singup-login.jpg"; 
import { NavLink } from "react-router-dom";
import { AuthContext } from "../../contexts/AuthContext";
import { useNavigate } from "react-router-dom";

function Login() {
  const { login } = React.useContext(AuthContext);
  const [userDetails, setUserDetails] = React.useState({
    email: "",
    password: "",
  })
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();
    //login(userDetails);
    //navigate("/recipes");
  }

   return (
    <Layout>
    <div className="flex h-screen max-w-screen justify-center items-center bg-cover  bg-no-repeat"
     style={{backgroundImage: `url(${loginBanner})`}}>
      <div className="w-[45%]  bg-black bg-opacity-60 rounded-xl shadow-xl max-h-screen flex items-center justify-center">
        <div className="w-full mt-2 mb-5 text-white max-w-md">
          <h2 className="text-2xl text-white font-bold mb-4">My Account</h2>
          <div className=" mb-6">
            Home &gt; My Account
          </div>
          <div className="mb-4 pb-2 border-b-2 border-gray-300 flex justify-between">
            <button
            className="font-bold border-b-4 border-white pb-1 p-1 rounded-lg hover:bg-green-500">
              Sign In</button>
            <NavLink to='/register'
            className=" hover:bg-green-500 p-1 rounded-lg font-bold">
            Register
            </NavLink>
          </div>
          <form on onSubmit={handleSubmit}>
            <div className="mb-4">
              <label className="block  mb-2" htmlFor="email">
                Username or email address*
              </label>
              <input
                className=" border border-black bg-gray-200 rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                id="email"
                type="email"
                name="email"
                placeholder="Enter your email"
              />
            </div>
            <div className="mb-4">
              <label className="block  mb-2" htmlFor="password">
                Password*
              </label>
              <input
                className="border border-black bg-gray-200 rounded w-full py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline"
                id="password"
                type="password"
                name="password"
                placeholder="Enter your password"
              />
            </div>
            <div className="flex items-center justify-between mb-6">
              <label className="flex items-center">
                <input
                  className="form-checkbox h-5 w-5 text-green-600"
                  type="checkbox"
                />
                <span className="ml-2 ">Remember me</span>
              </label>
              <a
                className="inline-block align-baseline border-b-2 border-white font-bold text-sm  hover:text-green-500"
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
    </div>
    </Layout>
  );
};

export default Login;

