import React from "react";

function WorldWide() {
  return (
    <section className="h-[90vh] w-full">
      <div className="w-full h-fit py-12 flex flex-col justify-center items-center">
        <h4 className="text-xl font-bold border border-gray-950 px-6 py-1 rounded-2xl">
          Easy to Prepare
        </h4>
        <h1 className="mt-5 font-bold grid itc text-center text-4xl ">
          <span className="text-red-600">Carefully crafted</span>
          <span>tested by millions worldwide</span>
        </h1>
        <span className="my-4 h-1 w-20 flex bg-green-600 rounded-3xl" />
        <p className="max-w-md text-center text-x font-semibolds">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Molestias
          fugit labore magni ratione mollitia ex ea autem.
        </p>
      </div>
    </section>
  );
}

export default WorldWide;
