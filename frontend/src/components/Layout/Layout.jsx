import React, { useEffect, useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Search from "./Search";

function Layout({ children }) {
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const root = document.querySelector("#root");

    root.setAttribute(
      "class",
      "flex flex-col justify-between min-h-screen smooth-scroll"
    );
    setLoading(false);
  }, []);

  if (loading) return null;

  return (
    <>
      <Header />
      {/* <Search /> */}
      <main>{children}</main>
      <Footer />
    </>
  );
}

export default Layout;
