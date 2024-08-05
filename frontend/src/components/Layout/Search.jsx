import React from "react";
import { useAuth } from "../../contexts/userContext";
import clsx from "clsx";

function Search() {
  const { isSearching } = useAuth();
  return (
    <div
      className={clsx(
        isSearching
          ? "absolute overflow-hidden h-[calc(100vh-4rem)] -translate-y-0 w-full left-0 right-0 top-[4rem] transform z-20 bg-gray-50 pt-32 mx-auto duration-700 ease-in-out"
          : "-translate-y-[100vh] duration-300 ease-in-out h-0"
      )}
    >
      <div className="w-full px-16 xl:container flex flex-col items-center justify-center border-t border-b border-green-950">
        <h1 className="text-stroke stroke-slate-500 text-[calc(10rem+2.5vw)] xl:text-[calc(12.4rem+4vw)] whitespace-nowrap">
          No Results
        </h1>
      </div>
    </div>
  );
}

export default Search;
