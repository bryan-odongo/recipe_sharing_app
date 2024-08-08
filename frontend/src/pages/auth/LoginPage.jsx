import React, { useState } from "react";
import Layout from "../../components/Layout/Layout";
import { SignIn, SignUp } from "@clerk/clerk-react";
import clsx from "clsx";

import bg from "../../assets/imgs/login_bg.png";

function Login() {
  const [isSignIn, setIsSignIn] = useState(false);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    firstname: "",
    lastname: "",
    username: "",
    password_confirmation: "",
  });

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [id]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isSignIn) {
      // Handle login submission

      console.log("Login data:", formData.email, formData.password);
      setFormData({
        email: "",
        password: "",
        firstname: "",
        lastname: "",
        username: "",
        password_confirmation: "",
      });
    } else {
      // Handle registration submission
      if (formData.password !== formData.password_confirmation) {
        setError({
          email: "",
          password: "Password did not match",
          firstname: "",
          lastname: "",
          username: "",
        });
        return;
      }

      if (formData.password.length < 8) {
        setError({
          email: "",
          password: "Passwords MUST be atleast 8 character",
          firstname: "",
          lastname: "",
          username: "",
        });
        return;
      }
      setError(null);
      console.log("Registration data:", formData);
      setFormData({
        email: "",
        password: "",
        firstname: "",
        lastname: "",
        username: "",
        password_confirmation: "",
      });
    }
  };

  return (
    <Layout>
      <section className="w-full min-h-[calc(100vh-8rem)] flex justify-start items-center relative">
        <img
          src={bg}
          alt="bg-image"
          className="absolute inset-0 w-full h-full"
        />
        <div className="h-full relative z-20 max-w-4xl xl:max-w-[73rem] w-full mx-auto py-3 flex justify-between items-center">
          <div className="w-fit h-full flex space-y-7 flex-col items-center justify-center">
            <div className="w-full mb-1 space-y-3">
              <div className="header space-y-2 border-b-2 border-slate-400 pb-2">
                <h3 className="text-3xl font-bold">
                  {isSignIn ? "My Account" : "Create an Account"}
                </h3>
              </div>
              <div className="flex items-center gap-2 font-bold">
                <span
                  className="relative flex w-fit cursor-pointer"
                  onClick={() => setIsSignIn(true)}
                >
                  <span>Login</span>
                  <span
                    className={clsx(
                      "absolute -bottom-1 left-0 h-[3px] bg-slate-800 rounded-full ease-out duration-300",
                      isSignIn ? "w-full" : "w-0"
                    )}
                  ></span>
                </span>
                <span
                  className="relative flex w-fit cursor-pointer"
                  onClick={() => setIsSignIn(false)}
                >
                  <span>Register</span>
                  <span
                    className={clsx(
                      "absolute -bottom-1 left-0 h-[3px] bg-slate-800 rounded-full ease-out duration-300",
                      !isSignIn ? "w-full" : "w-0"
                    )}
                  ></span>
                </span>
              </div>
            </div>

            {isSignIn ? (
              <form
                onSubmit={handleSubmit}
                className="space-y-7 [&_input]:text-sm [&_input]:text-gray-800 [&_input]:py-2 [&_input]:pl-2 [&_input]:placeholder:text-sm [&_label]:font-bold [&_label]:text-gray-700 [&_label]:text-sm [&_label]:pb-[2px]"
              >
                <div className="body space-y-2">
                  <fieldset className="input-group w-full flex flex-col">
                    <label htmlFor="email">Email or Username*</label>
                    <input
                      className="outline-none border border-slate-400 py-1 rounded-lg"
                      type="email"
                      id="email"
                      placeholder="Enter your email or username"
                      value={formData.email}
                      onChange={handleChange}
                    />
                  </fieldset>
                  <fieldset className="input-group w-full flex flex-col">
                    <label htmlFor="password">Password*</label>
                    <input
                      className="outline-none border border-slate-400 py-1 rounded-lg"
                      type="password"
                      id="password"
                      placeholder="Enter your password"
                      value={formData.password}
                      onChange={handleChange}
                    />
                  </fieldset>
                  <fieldset className="flex items-center justify-start font-semibold space-x-2 mt-2">
                    <input type="checkbox" name="" id="" />{" "}
                    <span className="text-xs">Remember me</span>
                  </fieldset>
                  <button
                    type="submit"
                    className="py-2 w-full flex items-center justify-center font-bold text-lg bg-green-600 rounded-lg text-white mt-5"
                  >
                    Login
                  </button>
                </div>
                <div className="divider flex space-x-2 items-center justify-between font-bold text-xs">
                  <span className="flex h-[2px] w-full bg-slate-400"></span>
                  <span>OR</span>
                  <span className="flex h-[2px] w-full bg-slate-400"></span>
                </div>
                <div className="socials relative w-full">
                  <SignIn
                    signInFallbackRedirectUrl={"/recipes"}
                    appearance={{
                      elements: {
                        card: "p-0 h-fit w-full bg-transparent border-none shadow-none",
                        header: "hidden",
                        socialButtons: "gap-4 bg-gray-100",
                        socialButtonsIconButton: "border border-slate-400",
                        socialButtonsProviderIcon: "h-6 w-6",
                        footer: "hidden",
                      },
                    }}
                  />
                </div>
              </form>
            ) : (
              <form
                onSubmit={handleSubmit}
                className="space-y-3 [&_input]:text-sm [&_input]:text-gray-800 [&_input]:py-2 [&_input]:pl-2 [&_input]:placeholder:text-sm [&_label]:font-bold [&_label]:text-slate-600 [&_label]:text-sm [&_label]:pb-[2px]"
              >
                <div className="body space-y-">
                  <div className="grid grid-cols-2 gap-3">
                    <fieldset className="input-group w-full flex flex-col">
                      <label htmlFor="firstname">Firstname*</label>
                      <input
                        className="outline-none border border-slate-400 py-1 rounded-lg"
                        type="text"
                        id="firstname"
                        placeholder="Enter your firstname"
                        value={formData.firstname}
                        onChange={handleChange}
                      />
                    </fieldset>
                    <fieldset className="input-group w-full flex flex-col">
                      <label htmlFor="lastname">Lastname*</label>
                      <input
                        className="outline-none border border-slate-400 py-1 rounded-lg"
                        type="text"
                        id="lastname"
                        placeholder="Enter your lastname"
                        value={formData.lastname}
                        onChange={handleChange}
                      />
                    </fieldset>
                  </div>
                  <fieldset className="input-group w-full flex flex-col">
                    <label htmlFor="username">Username*</label>
                    <input
                      className="outline-none border border-slate-400 py-1 rounded-lg"
                      type="text"
                      id="username"
                      placeholder="Enter your username"
                      value={formData.username}
                      onChange={handleChange}
                    />
                  </fieldset>
                  <fieldset className="input-group w-full flex flex-col">
                    <label htmlFor="email">Email*</label>
                    <input
                      className="outline-none border border-slate-400 py-1 rounded-lg"
                      type="email"
                      id="email"
                      placeholder="Enter your email"
                      value={formData.email}
                      onChange={handleChange}
                    />
                  </fieldset>
                  <div className="grid grid-cols-2 gap-3">
                    <fieldset className="input-group w-full flex flex-col">
                      <label htmlFor="password">Password*</label>
                      <input
                        className={clsx(
                          "outline-none border py-1 rounded-lg",
                          error?.password
                            ? "border-red-600"
                            : "border-slate-400"
                        )}
                        type="password"
                        id="password"
                        placeholder="Enter your password"
                        value={formData.password}
                        onChange={handleChange}
                      />
                    </fieldset>
                    <fieldset className="input-group w-full flex flex-col">
                      <label htmlFor="password_confirmation">
                        Confirm Password*
                      </label>
                      <input
                        className={clsx(
                          "outline-none border py-1 rounded-lg",
                          error?.password
                            ? "border-red-600"
                            : "border-slate-400"
                        )}
                        type="password"
                        id="password_confirmation"
                        placeholder="Confirm your password"
                        value={formData.password_confirmation}
                        onChange={handleChange}
                      />
                    </fieldset>
                  </div>
                  <fieldset className="flex pb-2 items-center justify-start font-semibold space-x-2 mt-2">
                    <input type="checkbox" name="" id="" />{" "}
                    <span className="text-xs">
                      I agree to the terms and conditions
                    </span>
                  </fieldset>
                  {error && (
                    <ul
                      className={clsx(
                        error && "border-t border-slate-400 py-2"
                      )}
                    >
                      {Object.values(error).map((err, i) => (
                        <li
                          key={i}
                          className="text-red-600 font-semibold text-xs"
                        >
                          {err}
                        </li>
                      ))}
                    </ul>
                  )}
                  <button
                    type="submit"
                    className="py-2 w-full flex items-center justify-center font-bold text-lg bg-green-600 rounded-lg text-white mt-5"
                  >
                    Register
                  </button>
                </div>
                <div className="divider flex space-x-2 items-center justify-between font-bold text-xs">
                  <span className="flex h-[2px] w-full bg-slate-400"></span>
                  <span>OR</span>
                  <span className="flex h-[2px] w-full bg-slate-400"></span>
                </div>
                <div className="socials relative w-full">
                  <SignUp
                    signInFallbackRedirectUrl={"/recipes"}
                    appearance={{
                      elements: {
                        card: "p-0 h-fit w-full bg-transparent border-none shadow-none",
                        header: "hidden",
                        main: "bg-transparent border-none outline-none shadow-none",
                        socialButtons: "gap-4 bg-gray-100",
                        socialButtonsIconButton: "border border-slate-400",
                        socialButtonsProviderIcon: "h-6 w-6",
                        footer: "hidden",
                      },
                    }}
                  />
                </div>
              </form>
            )}
          </div>
        </div>
      </section>
    </Layout>
  );
}

export default Login;
