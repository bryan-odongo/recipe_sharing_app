import React from "react";

function Footer() {
  return (
    <footer className="w-full h-fit">
      <div className="w-full max-w-4xl xl:max-w-[73rem] mx-auto">
        <p className="py-8 font-semibold">
          All rights reserved &copy; 1900 - {new Date().getFullYear()}
        </p>
      </div>
    </footer>
  );
}

export default Footer;
