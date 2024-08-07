import React from "react";
import { AuthContext } from "../../contexts/AuthContext";
import {
  BiLock,
  BiLockOpenAlt,
  BiSearch,
  BiSolidDashboard,
  BiUser,
  BiUserCircle,
  BiWindowClose,
} from "react-icons/bi";
import { NavLink } from "react-router-dom";

import logo from "../../assets/imgs/logo.jpg";
import { useAuth } from "../../contexts/userContext";
import clsx from "clsx";
import Search from "./Search";

const Header = () => {
  const { isLoggedIn, setIsLoggedIn, isSearching, setIsSearching } = useAuth();
  const { logout } = React.useContext(AuthContext);

  const handleLogout = () => {
    logout();
    setIsLoggedIn(false);
  };
  return (
    <header className="bg-white shadow-md h-[4rem] sticky top-0 z-50 grid items-center">
      <div
        className={clsx(
          "container mx-auto py-3 flex justify-between items-center",
          "lg:px-8",
          "xl:px-24",
          isSearching ? "" : "overflow-y-hidden"
        )}
      >
        <div className="flex items-center">
          <NavLink
            onClick={() => setIsSearching(false)}
            to="/"
            className="text-lg xl:text-xl font-bold text-green-600 rounded-lg border-2 border-green-600 px-2.5 py-1 xl:py-1.5"
          >
            {/* <img src={logo} alt="" className="h- w-64" /> */}
            RecipeHaven
          </NavLink>
        </div>
        <div className="relative group flex items-center w-[35%] xl:w-[40%]">
          {/* Alternative search... */}
          <div
            className={clsx(
              "search absolute overflow-x-hidden top-[calc(100%+6px)] rounded-lg w-full bg-red-300 will-change-auto duration-300 ease-out",
              isSearching ? "h-fit" : "h-0"
            )}
          >
            <div className="content w-full h-full flex items-center font-semibold p-4 bg-slate-50">
              Enter search Text...
            </div>
          </div>
          <input
            type="text"
            className={clsx(
              "w-full px-4 py-2 border rounded-lg",
              isSearching &&
                "focus:outline-none focus:ring focus:ring-green-400"
            )}
            placeholder="Search..."
            onClick={() => setIsSearching(true)}
          />
          {!isSearching ? (
            <BiSearch
              onClick={() => setIsSearching(true)}
              className="absolute z-20 right-4 text-xl xl:text-2xl group-hover:text-green-600 cursor-pointer"
            />
          ) : (
            <span
              onClick={() => setIsSearching(false)}
              className="absolute z-20 right-4  text-lg xl:text-xl group-hover:text-red-600 cursor-pointer"
            >
              ❌
            </span>
          )}
        </div>
        <nav className="flex items-center space-x-4 [&_a]:text-sm [&_a]:font-semibold">
          <NavLink
            onClick={() => setIsSearching(false)}
            to="/recipes"
            className={({ isActive }) =>
              isActive ? "nav-link-active" : "nav-link"
            }
          >
            Recipes
          </NavLink>
          <NavLink
            onClick={() => setIsSearching(false)}
            to="/cooking_tips"
            className={({ isActive }) =>
              isActive ? "nav-link-active" : "nav-link"
            }
          >
            Cooking Tips
          </NavLink>
          {isLoggedIn ? (
            <>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/dashboard"
                className={({ isActive }) =>
                  isActive ? "nav-link-active" : "nav-link"
                }
              >
                <BiSolidDashboard className="inline-block mr-1" />
                Dashboard
              </NavLink>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/profile"
                className={({ isActive }) =>
                  isActive
                    ? "nav-link-active flex items-center justify-center"
                    : "nav-link "
                }
              >
                <BiUserCircle className="inline-block mr-1 text-2xl" />
                <span>Profile</span>
              </NavLink>
            </>
          ) : (
            <>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/about_us"
                className={({ isActive }) =>
                  isActive ? "nav-link-active" : "nav-link"
                }
              >
                About Us
              </NavLink>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/contact_us"
                className={({ isActive }) =>
                  isActive ? "nav-link-active" : "nav-link"
                }
              >
                Contact Us
              </NavLink>
            </>
          )}
            {/*to={isLoggedIn ? "/" : "/login"}*/}
          <NavLink
            onClick={() => {
              setIsLoggedIn(!isLoggedIn);
              setIsSearching(false);
              //handleLogout();
            }}
            to={isLoggedIn ? "/" : "/login"}
              className={({ isActive }) =>
              isActive
                ? "flex group items-center justify-center space-x-2 text-gray-800 border border-green-600 px-4 py-1.5 rounded-2xl"
                : "flex group items-center justify-center space-x-2 text-gray-800 hover:text-gray-600 border border-cyan-300 hover:border-green-600 duration-300 ease-in-out px-4 py-1.5 rounded-2xl"
            }
          >
            <span>{isLoggedIn ? "Logout" : "Login"}</span>
            <BiLock className="group-hover:hidden" />
            <BiLockOpenAlt className="hidden group-hover:flex" />
          </NavLink>
        </nav>
      </div>
    </header>
  );
};

export default Header;
