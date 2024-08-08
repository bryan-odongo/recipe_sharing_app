import { useClerk, useUser } from "@clerk/clerk-react";
import React, { createContext, useContext, useEffect, useState } from "react";

const UserContext = createContext();

export const useAuth = () => useContext(UserContext);

export const UserProvider = ({ children }) => {
  const { isSignedIn, user, isLoaded } = useUser();

  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [dbLogin, setDbLogin] = useState(false);
  const [isSearching, setIsSearching] = useState(false);

  const { signOut } = useClerk();

  const getDbUser = async () => {
    const user_email =
      user?.emailAddresses[0]?.emailAddress || localStorage.getItem("user");

    if (!user_email) return null;

    try {
      const res = await fetch(`http://localhost:5000/api/users/${user_email}`);
      if (!res.ok) {
        throw new Error("User not found in DB");
      }
      const data = await res.json();
      return data;
    } catch (error) {
      console.error("Error fetching user from DB:", error);
      return null;
    }
  };

  const logout = () => {
    setIsLoggedIn(false);
    setDbLogin(false);

    localStorage.clear();

    signOut(() => {
      localStorage.clear();
    });
  };

  useEffect(() => {
    const checkUser = async () => {
      if (isLoaded) {
        const dbUser = await getDbUser();

        console.log("DB_USER: ", dbUser);

        if (isSignedIn && dbUser) {
          setIsLoggedIn(true);
          setDbLogin(false); // Logged in using Clerk
        } else if (!isSignedIn && dbUser) {
          setIsLoggedIn(true);
          setDbLogin(true); // Logged in using your database
        } else {
          setIsLoggedIn(false);
          setDbLogin(false);
          signOut(() => {
            localStorage.clear();
          });
        }

        console.log("USER: ", dbUser || user);
        console.log("IS_LOGGED_IN: ", isLoggedIn);
      }
    };

    checkUser();
  }, [isLoaded, isSignedIn]);

  return (
    <UserContext.Provider
      value={{
        isLoggedIn,
        setIsLoggedIn,
        isSearching,
        setIsSearching,
        dbLogin,
        logout,
      }}
    >
      {children}
    </UserContext.Provider>
  );
};
