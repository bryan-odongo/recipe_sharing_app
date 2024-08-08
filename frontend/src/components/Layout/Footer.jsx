import React from "react";
import { BiLink } from "react-icons/bi";

function Footer() {
  return (
    <footer className="w-full h-fit bg-slate-50 fixed inset-x-0 bottom-0 z-10">
      <div className="w-full text-sm max-w-4xl xl:max-w-[73rem] mx-auto flex justify-between">
        <p className="py-4 font-semibold">
          All rights reserved &copy; 1900 - {new Date().getFullYear()} (WIP)
        </p>
        <p className="py-4 font-semibold inline-flex items-center justify-center space-x-1 underline underline-offset-4">
          <span>Terms & Conditions</span> <BiLink />
        </p>
      </div>
    </footer>
  );
}

export default Footer;
